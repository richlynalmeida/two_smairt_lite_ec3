from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from utils.mixins import MixinsModel

# App: core
# Desc: (no description provided)
class CompanyItem(MixinsModel):
    company_item_id = models.AutoField(primary_key=True, db_column='company_item_id', verbose_name='Company Item ID')
    company_category_id = models.ForeignKey('core.CompanyCategory', on_delete=models.RESTRICT,
                                            db_column='company_category_id', verbose_name='Company Category ID',
                                            related_name='cc_j_ci')
    company_item_code = models.CharField(max_length=10, verbose_name='Company Item Code', help_text="10-letter company code")
    company_item_title = models.CharField(max_length=255, verbose_name='Company Item Title')
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Company E-mail')
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$",
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    business_phone = models.CharField(validators=[phone_regex], max_length=16, verbose_name='Business Phone')
    fax_number = models.CharField(validators=[phone_regex], max_length=16, blank=True, null=True,
                                  verbose_name='Fax Number')
    address1 = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Address Line 2')
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True, verbose_name='ZIP/Postal Code')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='City')
    state_province = models.CharField(max_length=50, blank=True, null=True, verbose_name='State/Province')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Country')
    web_page = models.URLField(max_length=250, blank=True, null=True, verbose_name='Web Page')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        db_table = 'company_item'
        app_label = 'core'
        verbose_name_plural = "Organization / Company Item"
        ordering = ['company_item_code']

    def __str__(self):
        return f"{self.company_item_code} - {self.company_item_title}"

    def __repr__(self):
        return "<CompanyItem {}>".format(f"{self.company_item_code} - {self.company_item_title}")

    def __label__(self):
        return f"{self.company_item_code} - {self.company_item_title}"
