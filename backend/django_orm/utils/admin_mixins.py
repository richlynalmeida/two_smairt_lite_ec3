# backend/django_orm/utils/admin_mixins.py
from django.utils.html import format_html
from decimal import Decimal, InvalidOperation
from django.utils.safestring import SafeString

class PrettyNumberMixin:
    """
    Admin-only helpers for formatting numbers, money, percentages,
    and a small volatility badge. Robust to string/SafeString inputs.
    """

    @staticmethod
    def _to_decimal(x):
        """Best-effort cast to Decimal, else return None."""
        if x is None:
            return None
        if isinstance(x, Decimal):
            return x
        if isinstance(x, (int, float)):
            return Decimal(str(x))
        # If it's a SafeString or normal str like "1234.56", try casting
        if isinstance(x, (str, SafeString)):
            try:
                return Decimal(x.replace(",", ""))
            except (InvalidOperation, AttributeError):
                return None
        # Unknown type
        return None

    @classmethod
    def fmt_money(cls, x):
        """
        Format a value as currency, e.g. 1200000 -> $1,200,000.00.
        Returns a plain string (not marked safe).
        """
        n = cls._to_decimal(x)
        return "" if n is None else f"${n:,.2f}"

    @classmethod
    def fmt_num(cls, x, digits=2):
        """Format a numeric value with grouping and fixed decimals."""
        n = cls._to_decimal(x)
        if n is None:
            return ""
        fmt = f"{{:,.{digits}f}}"
        return fmt.format(n)

    @staticmethod
    def fmt_pct(x, digits=1):
        """Format a decimal (already a percentage) as a string like 12.3%."""
        # Note: Here x is expected to be numeric/Decimal/float
        try:
            n = Decimal(str(x))
        except (InvalidOperation, TypeError, ValueError):
            return ""
        return f"{n:.{digits}f}%"

    @staticmethod
    def volatility_badge(p50, p90):
        """
        Badge indicating volatility between P50 and P90.
        - Green (<50%): low
        - Amber (50–150%): medium
        - Red (>150%): high
        """
        # Coerce defensively
        try:
            p50 = Decimal(str(p50))
            p90 = Decimal(str(p90))
        except (InvalidOperation, TypeError, ValueError):
            return ""

        if p50 <= 0 or p90 is None:
            return ""

        spread_pct = (p90 - p50) / p50 * 100

        if spread_pct < 50:
            color, label = "#16a34a", "low"
        elif spread_pct <= 150:
            color, label = "#f59e0b", "med"
        else:
            color, label = "#dc2626", "high"

        return format_html(
            '<span style="padding:2px 8px;border-radius:12px;'
            'background:{};color:white;font-weight:600;">{} ({:.1f}%)</span>',
            color,
            label,
            float(spread_pct),
        )
