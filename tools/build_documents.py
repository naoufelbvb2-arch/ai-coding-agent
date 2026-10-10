"""Reproducible documentation build; no agent runtime or production implementation."""
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
for name in ['source_catalogue','compose_l0','compose_l1','compose_l2','compose_remaining',
             'complete_fca_links','retain_invariants','build_evidence','interface_report','architecture_manifest']:
    subprocess.run([sys.executable,str(ROOT/'tools'/(name+'.py'))],cwd=ROOT,check=True)
