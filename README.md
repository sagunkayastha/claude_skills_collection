# Claude Skills Collection

A curated collection of Claude agent skills from various sources, assembled for my specific use case.

Skills are organized by domain, sourced from [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) and [Orchestra Research AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs). Only relevant categories are included — bioinformatics, clinical, cheminformatics, and other domain-specific skills have been intentionally excluded.

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

### [agent-frameworks](./agent-frameworks)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [autogpt](./agent-frameworks/autogpt/SKILL.md) | Autonomous AI agent platform for building and deploying continuous agents |
| [crewai](./agent-frameworks/crewai/SKILL.md) | Multi-agent orchestration framework for autonomous AI collaboration |
| [langchain](./agent-frameworks/langchain/SKILL.md) | Framework for building LLM-powered applications with agents, chains, and RAG |
| [llamaindex](./agent-frameworks/llamaindex/SKILL.md) | Data framework for building LLM applications with RAG and document indexing |

### [data-processing](./data-processing)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [huggingface-tokenizers](./data-processing/huggingface-tokenizers/SKILL.md) | Fast Rust-based tokenizers for research and production |
| [nemo-curator](./data-processing/nemo-curator/SKILL.md) | GPU-accelerated data curation for LLM training |
| [ray-data](./data-processing/ray-data/SKILL.md) | Scalable data processing for ML workloads with streaming execution |
| [sentencepiece](./data-processing/sentencepiece/SKILL.md) | Language-independent tokenizer with BPE and Unigram support |

### [distributed-training](./distributed-training)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [accelerate](./distributed-training/accelerate/SKILL.md) | Simplest distributed training API for PyTorch |
| [deepspeed](./distributed-training/deepspeed/SKILL.md) | ZeRO optimization stages for distributed training |
| [megatron-core](./distributed-training/megatron-core/SKILL.md) | Large language model training (2B-462B params) with NVIDIA Megatron-Core |
| [pytorch-fsdp2](./distributed-training/pytorch-fsdp2/SKILL.md) | PyTorch FSDP2 (fully_shard) distributed training |
| [ray-train](./distributed-training/ray-train/SKILL.md) | Distributed training orchestration across clusters |

### [emerging-techniques](./emerging-techniques)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [knowledge-distillation](./emerging-techniques/knowledge-distillation/SKILL.md) | Compress large language models from teacher to student |
| [long-context](./emerging-techniques/long-context/SKILL.md) | Extend context windows with RoPE, YaRN, ALiBi |
| [model-merging](./emerging-techniques/model-merging/SKILL.md) | Merge fine-tuned models using mergekit |
| [model-pruning](./emerging-techniques/model-pruning/SKILL.md) | Reduce LLM size with Wanda and other pruning techniques |
| [moe-training](./emerging-techniques/moe-training/SKILL.md) | Mixture of Experts model training |
| [speculative-decoding](./emerging-techniques/speculative-decoding/SKILL.md) | Accelerate LLM inference with speculative decoding and Medusa heads |

### [evaluation-benchmarks](./evaluation-benchmarks)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [bigcode-evaluation-harness](./evaluation-benchmarks/bigcode-evaluation-harness/SKILL.md) | Evaluate code generation models across HumanEval, MBPP, MultiPL-E |
| [lm-evaluation-harness](./evaluation-benchmarks/lm-evaluation-harness/SKILL.md) | Evaluate LLMs across 60+ academic benchmarks (MMLU, GSM8K, etc.) |
| [nemo-evaluator](./evaluation-benchmarks/nemo-evaluator/SKILL.md) | Evaluate LLMs across 100+ benchmarks from 18+ harnesses |

### [fine-tuning-training](./fine-tuning-training)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [axolotl](./fine-tuning-training/axolotl/SKILL.md) | Fine-tune LLMs with YAML configs, 100+ models, LoRA/QLoRA |
| [llama-factory](./fine-tuning-training/llama-factory/SKILL.md) | Fine-tune LLMs with WebUI, 100+ models support |
| [peft](./fine-tuning-training/peft/SKILL.md) | Parameter-efficient fine-tuning with LoRA, QLoRA, 25+ methods |
| [unsloth](./fine-tuning-training/unsloth/SKILL.md) | Fast fine-tuning — 2-5x faster, 50-80% less memory |

### [inference-serving](./inference-serving)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [llama-cpp](./inference-serving/llama-cpp/SKILL.md) | LLM inference on CPU, Apple Silicon, and consumer GPUs |
| [sglang](./inference-serving/sglang/SKILL.md) | Fast structured generation with RadixAttention prefix caching |
| [tensorrt-llm](./inference-serving/tensorrt-llm/SKILL.md) | NVIDIA TensorRT optimized LLM inference |
| [vllm](./inference-serving/vllm/SKILL.md) | High throughput LLM serving with PagedAttention |

### [mechanistic-interpretability](./mechanistic-interpretability)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [nnsight](./mechanistic-interpretability/nnsight/SKILL.md) | Interpret and manipulate neural network internals |
| [pyvene](./mechanistic-interpretability/pyvene/SKILL.md) | Causal interventions on PyTorch models |
| [saelens](./mechanistic-interpretability/saelens/SKILL.md) | Train and analyze Sparse Autoencoders (SAEs) |
| [transformer-lens](./mechanistic-interpretability/transformer-lens/SKILL.md) | Mechanistic interpretability research on transformers |

### [ml-paper-writing](./ml-paper-writing)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [ml-paper-writing](./ml-paper-writing/SKILL.md) | ML paper writing with LaTeX templates for 10 major venues (NeurIPS, ICML, ICLR, AAAI, ACL, etc.) |

### [mlops](./mlops)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [mlflow](./mlops/mlflow/SKILL.md) | Track experiments, manage model registry, deploy models |
| [swanlab](./mlops/swanlab/SKILL.md) | Open-source experiment tracking |
| [tensorboard](./mlops/tensorboard/SKILL.md) | Visualize training metrics and debug models |
| [weights-and-biases](./mlops/weights-and-biases/SKILL.md) | ML experiment tracking with real-time visualization |

### [model-architecture](./model-architecture)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [litgpt](./model-architecture/litgpt/SKILL.md) | Train LLMs with Lightning AI's LitGPT, 20+ architectures |
| [mamba](./model-architecture/mamba/SKILL.md) | State-space model with O(n) complexity, 5x faster inference |
| [nanogpt](./model-architecture/nanogpt/SKILL.md) | Educational GPT implementation in ~300 lines |
| [rwkv](./model-architecture/rwkv/SKILL.md) | RNN+Transformer hybrid with O(n) inference, infinite context |
| [torchtitan](./model-architecture/torchtitan/SKILL.md) | PyTorch-native distributed LLM pretraining with 4D parallelism |

### [multimodal](./multimodal)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [audiocraft](./multimodal/audiocraft/SKILL.md) | Audio generation: text-to-music (MusicGen) and text-to-audio |
| [blip-2](./multimodal/blip-2/SKILL.md) | Vision-language pre-training bridging image encoders and LLMs |
| [clip](./multimodal/clip/SKILL.md) | OpenAI CLIP — zero-shot image classification, image-text matching |
| [cosmos-policy](./multimodal/cosmos-policy/SKILL.md) | NVIDIA Cosmos Policy for robot simulation environments |
| [llava](./multimodal/llava/SKILL.md) | Visual instruction tuning and image understanding |
| [openpi](./multimodal/openpi/SKILL.md) | Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) |
| [openvla-oft](./multimodal/openvla-oft/SKILL.md) | OpenVLA-OFT robot action prediction fine-tuning |
| [segment-anything](./multimodal/segment-anything/SKILL.md) | Foundation model for zero-shot image segmentation |
| [stable-diffusion](./multimodal/stable-diffusion/SKILL.md) | Text-to-image generation with Stable Diffusion |
| [whisper](./multimodal/whisper/SKILL.md) | OpenAI speech recognition — 99 languages, transcription, translation |

### [observability](./observability)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [langsmith](./observability/langsmith/SKILL.md) | LLM observability: tracing, evaluation, monitoring |
| [phoenix](./observability/phoenix/SKILL.md) | Open-source AI observability for LLM tracing and evaluation |

### [optimization-quantization](./optimization-quantization)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [awq](./optimization-quantization/awq/SKILL.md) | 4-bit weight quantization with 3x speedup |
| [bitsandbytes](./optimization-quantization/bitsandbytes/SKILL.md) | 8-bit/4-bit quantization for 50-75% memory reduction |
| [flash-attention](./optimization-quantization/flash-attention/SKILL.md) | Optimized transformer attention — 2-4x speedup, 10-20x memory savings |
| [gguf](./optimization-quantization/gguf/SKILL.md) | GGUF format and llama.cpp quantization for CPU/GPU inference |
| [gptq](./optimization-quantization/gptq/SKILL.md) | Post-training 4-bit quantization with minimal accuracy loss |
| [hqq](./optimization-quantization/hqq/SKILL.md) | Half-Quadratic Quantization without calibration data |

### [post-training-rlhf](./post-training-rlhf)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [grpo-rl-training](./post-training-rlhf/grpo-rl-training/SKILL.md) | GRPO/RL fine-tuning with TRL for reasoning tasks |
| [miles](./post-training-rlhf/miles/SKILL.md) | Enterprise-grade RL training |
| [openrlhf](./post-training-rlhf/openrlhf/SKILL.md) | High-performance RLHF with Ray+vLLM acceleration |
| [simpo](./post-training-rlhf/simpo/SKILL.md) | Simple Preference Optimization — reference-free DPO alternative |
| [slime](./post-training-rlhf/slime/SKILL.md) | LLM post-training with Megatron+SGLang |
| [torchforge](./post-training-rlhf/torchforge/SKILL.md) | PyTorch-native agentic RL (Meta) |
| [trl-fine-tuning](./post-training-rlhf/trl-fine-tuning/SKILL.md) | SFT, DPO, PPO, GRPO for LLM alignment with TRL |
| [verl](./post-training-rlhf/verl/SKILL.md) | Volcano Engine RL training for LLMs |

### [prompt-engineering](./prompt-engineering)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [dspy](./prompt-engineering/dspy/SKILL.md) | Declarative AI programming with automatic prompt optimization |
| [guidance](./prompt-engineering/guidance/SKILL.md) | Control LLM output with regex/grammars, guarantee valid JSON/XML |
| [instructor](./prompt-engineering/instructor/SKILL.md) | Structured data extraction from LLMs with Pydantic validation |
| [outlines](./prompt-engineering/outlines/SKILL.md) | Guarantee valid JSON/XML/code structure during generation |

### [rag-retrieval](./rag-retrieval)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [chroma](./rag-retrieval/chroma/SKILL.md) | Open-source embedding database for AI applications |
| [faiss](./rag-retrieval/faiss/SKILL.md) | Facebook's efficient similarity search for dense vectors |
| [pinecone](./rag-retrieval/pinecone/SKILL.md) | Managed vector database for production AI |
| [qdrant](./rag-retrieval/qdrant/SKILL.md) | High-performance vector search for RAG and semantic search |
| [sentence-transformers](./rag-retrieval/sentence-transformers/SKILL.md) | State-of-the-art sentence and text embeddings |

### [safety-alignment](./safety-alignment)
*Source: [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs)*
| Skill | Description |
|-------|-------------|
| [constitutional-ai](./safety-alignment/constitutional-ai/SKILL.md) | Anthropic's method for training harmless AI through self-improvement |
| [llamaguard](./safety-alignment/llamaguard/SKILL.md) | Meta's moderation model for LLM input/output filtering |
| [nemo-guardrails](./safety-alignment/nemo-guardrails/SKILL.md) | NVIDIA runtime safety framework for LLM applications |
| [prompt-guard](./safety-alignment/prompt-guard/SKILL.md) | Meta's prompt injection and jailbreak detector |

## Updating

Run `update_skills.sh` to check for new skills from K-Dense and download any that aren't already included.

```bash
bash update_skills.sh
```

Excluded skills are listed in [`excluded.conf`](./excluded.conf), grouped by category. To re-enable a skill, comment out its line — it will be picked up on the next run.

## Sources

- [K-Dense AI Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) — scientific research, data analysis, databases, communication, and methodology skills
- [Orchestra Research AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT license) — AI/ML engineering skills: fine-tuning, inference, optimization, RAG, agents, distributed training, interpretability, safety, MLOps, multimodal, and more
- custom — autonomous PyTorch model tuning on Ray clusters, derived from autoresearch (`custom/autoraysearch`)
- [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — complete programmatic API for Google NotebookLM (`scientific-communication/notebooklm`)
- custom — YouTube video transcription with faster-whisper and interactive Claude workflow (`custom/youtube_sum`)
