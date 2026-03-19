# Claude Skills Collection

A curated collection of Claude agent skills from various sources, assembled for my specific use case.

Skills are organized by domain and sourced primarily from [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills). Only relevant categories are included — bioinformatics, clinical, cheminformatics, and other domain-specific skills have been intentionally excluded.

## Categories

- **data-analysis-visualization** — Matplotlib, Seaborn, Plotly, GeoPandas, NetworkX, SymPy, and more
- **engineering-simulation** — MATLAB, SimPy, Dask, Polars, Vaex, FluidSim
- **financial-research** — SEC filings, FRED, Alpha Vantage, hedge fund data
- **infrastructure-platforms** — Modal, DNAnexus, LatchBio, OMERO, Opentrons, Telegram notifications (notify)
- **machine-learning-ai** — PyTorch Lightning, Transformers, scikit-learn, SHAP, PyMC, and more
- **medical-imaging-pathology** — pydicom, histolab, PathML
- **protein-engineering-design** — ESM, Glycoengineering, Adaptyv
- **regulatory-standards** — ISO 13485
- **research-methodology** — Brainstorming, hypothesis generation, grant writing, critical thinking
- **scientific-communication** — Literature review, scientific writing, slides, posters, citation management
- **scientific-databases** — UniProt, PDB, PubChem, ChEMBL, Ensembl, gnomAD, and more

## Updating

Run `update_skills.sh` to check for new skills from K-Dense and download any that aren't already included. Excluded categories are hardcoded in the script and will never be pulled.

```bash
bash update_skills.sh
```

## Sources

- [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) — primary source for most skills
- [autoraysearch](https://github.com/sagunkayastha/autoraysearch) — autonomous PyTorch model tuning on Ray clusters (`custom/autoraysearch`)
- [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — complete programmatic API for Google NotebookLM (`scientific-communication/notebooklm`)
- custom — one-way Telegram phone notifications via a local Python script (`infrastructure-platforms/notify`)
