# Claude Skills Collection

A curated collection of Claude agent skills from various sources, assembled for my specific use case.

Skills are organized by domain and sourced primarily from [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills). Only relevant categories are included — bioinformatics, clinical, cheminformatics, and other domain-specific skills have been intentionally excluded.

## Structure

### [custom](./custom)
| Skill | Description |
|-------|-------------|
| [autoraysearch](./custom/autoraysearch/SKILL.md) | Autonomous PyTorch model tuning on Ray clusters |
| [youtube_sum](./custom/youtube_sum/SKILL.md) | Transcribe YouTube videos with faster-whisper (GPU-accelerated) |

### [data-analysis-visualization](./data-analysis-visualization)
| Skill | Description |
|-------|-------------|
| [datacommons-client](./data-analysis-visualization/datacommons-client/SKILL.md) | Data Commons API for public datasets |
| [exploratory-data-analysis](./data-analysis-visualization/exploratory-data-analysis/SKILL.md) | Comprehensive EDA on scientific data |
| [geomaster](./data-analysis-visualization/geomaster/SKILL.md) | Geospatial science and remote sensing |
| [geopandas](./data-analysis-visualization/geopandas/SKILL.md) | Geospatial vector data with GeoPandas |
| [matplotlib](./data-analysis-visualization/matplotlib/SKILL.md) | Low-level plotting with full customization |
| [networkx](./data-analysis-visualization/networkx/SKILL.md) | Graph creation, analysis, and visualization |
| [plotly](./data-analysis-visualization/plotly/SKILL.md) | Interactive visualization |
| [scientific-visualization](./data-analysis-visualization/scientific-visualization/SKILL.md) | Publication-ready figures |
| [seaborn](./data-analysis-visualization/seaborn/SKILL.md) | Statistical visualization with pandas integration |
| [statistical-analysis](./data-analysis-visualization/statistical-analysis/SKILL.md) | Statistical test selection and reporting |
| [sympy](./data-analysis-visualization/sympy/SKILL.md) | Symbolic mathematics |

### [engineering-simulation](./engineering-simulation)
| Skill | Description |
|-------|-------------|
| [dask](./engineering-simulation/dask/SKILL.md) | Distributed computing for larger-than-RAM data |
| [fluidsim](./engineering-simulation/fluidsim/SKILL.md) | Computational fluid dynamics simulation |
| [matlab](./engineering-simulation/matlab/SKILL.md) | MATLAB and GNU Octave numerical computing |
| [polars](./engineering-simulation/polars/SKILL.md) | Fast in-memory DataFrame library |
| [simpy](./engineering-simulation/simpy/SKILL.md) | Discrete-event simulation |
| [vaex](./engineering-simulation/vaex/SKILL.md) | Large tabular data processing |

### [financial-research](./financial-research)
| Skill | Description |
|-------|-------------|
| [alpha-vantage](./financial-research/alpha-vantage/SKILL.md) | Real-time and historical stock market data |
| [edgartools](./financial-research/edgartools/SKILL.md) | SEC EDGAR filings and financial data |
| [fred-economic-data](./financial-research/fred-economic-data/SKILL.md) | Federal Reserve economic data (FRED) |
| [hedgefundmonitor](./financial-research/hedgefundmonitor/SKILL.md) | OFR hedge fund data |
| [usfiscaldata](./financial-research/usfiscaldata/SKILL.md) | U.S. Treasury fiscal data |

### [infrastructure-platforms](./infrastructure-platforms)
| Skill | Description |
|-------|-------------|
| [get-available-resources](./infrastructure-platforms/get-available-resources/SKILL.md) | Discover compute resources at session start |
| [modal](./infrastructure-platforms/modal/SKILL.md) | Serverless cloud Python execution |

### [machine-learning-ai](./machine-learning-ai)
| Skill | Description |
|-------|-------------|
| [aeon](./machine-learning-ai/aeon/SKILL.md) | Time series machine learning |
| [pufferlib](./machine-learning-ai/pufferlib/SKILL.md) | High-performance reinforcement learning |
| [pymc](./machine-learning-ai/pymc/SKILL.md) | Bayesian modeling |
| [pymoo](./machine-learning-ai/pymoo/SKILL.md) | Multi-objective optimization |
| [pytorch-lightning](./machine-learning-ai/pytorch-lightning/SKILL.md) | Structured deep learning with PyTorch |
| [scikit-learn](./machine-learning-ai/scikit-learn/SKILL.md) | Classical machine learning |
| [scikit-survival](./machine-learning-ai/scikit-survival/SKILL.md) | Survival analysis |
| [shap](./machine-learning-ai/shap/SKILL.md) | Model interpretability with SHAP |
| [stable-baselines3](./machine-learning-ai/stable-baselines3/SKILL.md) | Production-ready RL algorithms |
| [statsmodels](./machine-learning-ai/statsmodels/SKILL.md) | Statistical models |
| [timesfm-forecasting](./machine-learning-ai/timesfm-forecasting/SKILL.md) | Zero-shot time series forecasting |
| [torch-geometric](./machine-learning-ai/torch-geometric/SKILL.md) | Graph neural networks (PyG) |
| [transformers](./machine-learning-ai/transformers/SKILL.md) | Pre-trained models via HuggingFace |
| [umap-learn](./machine-learning-ai/umap-learn/SKILL.md) | UMAP dimensionality reduction |

### [research-methodology](./research-methodology)
| Skill | Description |
|-------|-------------|
| [autoresearch](./research-methodology/autoresearch/SKILL.md) | Autonomous goal-directed research iteration |
| [consciousness-council](./research-methodology/consciousness-council/SKILL.md) | Multi-perspective deliberation |
| [dhdna-profiler](./research-methodology/dhdna-profiler/SKILL.md) | Cognitive pattern extraction |
| [hypothesis-generation](./research-methodology/hypothesis-generation/SKILL.md) | Structured hypothesis formulation |
| [market-research-reports](./research-methodology/market-research-reports/SKILL.md) | Comprehensive market research reports |
| [offer-k-dense-web](./research-methodology/offer-k-dense-web/SKILL.md) | Web-enhanced research session kickoff |
| [research-grants](./research-methodology/research-grants/SKILL.md) | Competitive grant proposal writing |
| [research-lookup](./research-methodology/research-lookup/SKILL.md) | Current research information lookup |
| [scholar-evaluation](./research-methodology/scholar-evaluation/SKILL.md) | Systematic scholarly work evaluation |
| [scientific-brainstorming](./research-methodology/scientific-brainstorming/SKILL.md) | Creative research ideation |
| [scientific-critical-thinking](./research-methodology/scientific-critical-thinking/SKILL.md) | Evidence quality evaluation |
| [what-if-oracle](./research-methodology/what-if-oracle/SKILL.md) | Structured What-If scenario analysis |

### [scientific-communication](./scientific-communication)
| Skill | Description |
|-------|-------------|
| [art](./scientific-communication/art/SKILL.md) | Visual content system |
| [arxiv-database](./scientific-communication/arxiv-database/SKILL.md) | Search and retrieve arXiv preprints |
| [bgpt-paper-search](./scientific-communication/bgpt-paper-search/SKILL.md) | Scientific paper search |
| [biorxiv-database](./scientific-communication/biorxiv-database/SKILL.md) | bioRxiv preprint search |
| [citation-management](./scientific-communication/citation-management/SKILL.md) | Academic citation management |
| [docx](./scientific-communication/docx/SKILL.md) | Word document creation and editing |
| [excalidraw-diagram](./scientific-communication/excalidraw-diagram/SKILL.md) | Excalidraw diagram generation |
| [generate-image](./scientific-communication/generate-image/SKILL.md) | AI image generation and editing |
| [infographics](./scientific-communication/infographics/SKILL.md) | Professional infographic creation |
| [latex-posters](./scientific-communication/latex-posters/SKILL.md) | Research posters in LaTeX |
| [literature-review](./scientific-communication/literature-review/SKILL.md) | Systematic literature reviews |
| [markdown-mermaid-writing](./scientific-communication/markdown-mermaid-writing/SKILL.md) | Markdown and Mermaid diagrams |
| [markitdown](./scientific-communication/markitdown/SKILL.md) | Convert documents to Markdown |
| [notebooklm](./scientific-communication/notebooklm/SKILL.md) | Google NotebookLM programmatic API |
| [open-notebook](./scientific-communication/open-notebook/SKILL.md) | Self-hosted NotebookLM alternative |
| [openalex-database](./scientific-communication/openalex-database/SKILL.md) | Scholarly literature via OpenAlex |
| [paper-2-web](./scientific-communication/paper-2-web/SKILL.md) | Convert academic papers to web pages |
| [parallel-web](./scientific-communication/parallel-web/SKILL.md) | Parallel web search and extraction |
| [pdf](./scientific-communication/pdf/SKILL.md) | PDF creation and manipulation |
| [peer-review](./scientific-communication/peer-review/SKILL.md) | Structured manuscript review |
| [perplexity-search](./scientific-communication/perplexity-search/SKILL.md) | AI-powered web search |
| [pptx](./scientific-communication/pptx/SKILL.md) | PowerPoint file creation and editing |
| [pptx-posters](./scientific-communication/pptx-posters/SKILL.md) | Research posters via HTML/CSS |
| [pubmed-database](./scientific-communication/pubmed-database/SKILL.md) | PubMed literature search |
| [pyzotero](./scientific-communication/pyzotero/SKILL.md) | Zotero reference management |
| [scientific-schematics](./scientific-communication/scientific-schematics/SKILL.md) | Publication-quality scientific diagrams |
| [scientific-slides](./scientific-communication/scientific-slides/SKILL.md) | Research talk slide decks |
| [scientific-writing](./scientific-communication/scientific-writing/SKILL.md) | Deep research and academic writing |
| [venue-templates](./scientific-communication/venue-templates/SKILL.md) | LaTeX templates for journals/conferences |
| [xlsx](./scientific-communication/xlsx/SKILL.md) | Spreadsheet file handling |

### [scientific-databases](./scientific-databases)
| Skill | Description |
|-------|-------------|
| [alphafold-database](./scientific-databases/alphafold-database/SKILL.md) | AlphaFold protein structure predictions |
| [bindingdb-database](./scientific-databases/bindingdb-database/SKILL.md) | Drug-target binding affinity data |
| [brenda-database](./scientific-databases/brenda-database/SKILL.md) | Enzyme database (BRENDA) |
| [chembl-database](./scientific-databases/chembl-database/SKILL.md) | Bioactive molecules and drug discovery |
| [drugbank-database](./scientific-databases/drugbank-database/SKILL.md) | Comprehensive drug information |
| [ena-database](./scientific-databases/ena-database/SKILL.md) | European Nucleotide Archive |
| [ensembl-database](./scientific-databases/ensembl-database/SKILL.md) | Ensembl genome database |
| [gene-database](./scientific-databases/gene-database/SKILL.md) | NCBI Gene database |
| [geo-database](./scientific-databases/geo-database/SKILL.md) | NCBI GEO gene expression data |
| [gnomad-database](./scientific-databases/gnomad-database/SKILL.md) | gnomAD population variant data |
| [gtex-database](./scientific-databases/gtex-database/SKILL.md) | GTEx tissue expression data |
| [gwas-database](./scientific-databases/gwas-database/SKILL.md) | GWAS Catalog SNP-trait associations |
| [hmdb-database](./scientific-databases/hmdb-database/SKILL.md) | Human Metabolome Database |
| [interpro-database](./scientific-databases/interpro-database/SKILL.md) | InterPro protein families and domains |
| [jaspar-database](./scientific-databases/jaspar-database/SKILL.md) | Transcription factor binding sites |
| [metabolomics-workbench-database](./scientific-databases/metabolomics-workbench-database/SKILL.md) | NIH Metabolomics Workbench |
| [opentargets-database](./scientific-databases/opentargets-database/SKILL.md) | Target-disease associations |
| [pdb-database](./scientific-databases/pdb-database/SKILL.md) | RCSB Protein Data Bank |
| [primekg](./scientific-databases/primekg/SKILL.md) | Precision Medicine Knowledge Graph |
| [pubchem-database](./scientific-databases/pubchem-database/SKILL.md) | PubChem compound database |
| [uniprot-database](./scientific-databases/uniprot-database/SKILL.md) | UniProt protein database |
| [uspto-database](./scientific-databases/uspto-database/SKILL.md) | USPTO patent and trademark search |
| [zinc-database](./scientific-databases/zinc-database/SKILL.md) | ZINC purchasable compound database |

## Updating

Run `update_skills.sh` to check for new skills from K-Dense and download any that aren't already included.

```bash
bash update_skills.sh
```

Excluded skills are listed in [`excluded.conf`](./excluded.conf), grouped by category. To re-enable a skill, comment out its line — it will be picked up on the next run.

## Sources

- [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) — primary source for most skills
- custom — autonomous PyTorch model tuning on Ray clusters, derived from autoresearch (`custom/autoraysearch`)
- [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — complete programmatic API for Google NotebookLM (`scientific-communication/notebooklm`)
- custom — YouTube video transcription with faster-whisper and interactive Claude workflow (`custom/youtube_sum`)
