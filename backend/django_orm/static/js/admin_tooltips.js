document.addEventListener('DOMContentLoaded', function() {
  const tooltips = {
    '01 – Define Feasibility Cases': 'Create/edit the top-level feasibility case (objectives, assumptions).',
    '02 – Scope the Case (Select Components)': 'Attach project components/scope to the feasibility case.',
    '03 – Configure Estimate Models': 'Set up estimating structure, categories, and methods.',
    '04 – Map Components to Estimate Model': 'Bind scope items to the cost model for calculations.',
    '05 – Define Quanta & Inputs (EMQ)': 'Enter quantities, UOM, and cost drivers at a granular level.',
    '06 – Link Price Sources & Benchmarks': 'Reference WUPA/vendor/benchmark unit rates.',
    '07 – Generate WUPA Snapshot (Immutable)': 'Capture an as-of unit-rate snapshot for auditability.',
    '08 – Build Estimate Scenarios': 'Assemble versioned what-if scenarios from your inputs.',
    '09 – Rollup & Metrics (Read-Only)': 'Review totals, KPIs, spreads (P50/P90), sensitivity.',
    '10 – Freeze Scenario (Baseline)': 'Lock the baseline version for comparisons.',
    '11 – Compare Scenarios & Deltas': 'Side-by-side variance and narrative review.',
    '12 – Publish / Export (Share Results)': 'Export to PDF/CSV/EDMS and stamp provenance.'
  };

  const sidebar = document.querySelector('#nav-sidebar');
  if (!sidebar) return;

  sidebar.querySelectorAll('a').forEach(a => {
    const text = (a.textContent || '').trim();
    if (tooltips[text]) a.setAttribute('title', tooltips[text]);
  });
});
