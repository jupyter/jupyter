# Recursive Research Framework

**Literary-Computational Scholarship Through Iterative Text Atomization**

This repository implements a three-layer recursive research architecture for literary analysis combining computational text processing with multi-platform AI scholarship synthesis.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     LITERARY CORPUS                          │
│         (Odyssey, Metamorphoses, Beowulf, etc.)             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              PRIMARY LAYER: Text Atomization                 │
│  • N-gram frequency analysis (unigrams → trigrams+)         │
│  • Entropy measurements (Shannon, normalized)               │
│  • Glyph fusion mappings (symbolic transformation)          │
│  • Compression ratios & lexical diversity                   │
│                                                              │
│  Output: Daily Markdown + JSON archives                     │
│  Location: /data/processed/atomization/                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│            SECONDARY LAYER: AI Scholarship                   │
│  Multi-platform orchestration:                              │
│    1. Perplexity → Research contextual scholarship          │
│    2. Claude → Analyze & synthesize frameworks              │
│    3. GPT/Grok → Generate creative variations               │
│                                                              │
│  Output: Structured Markdown + metadata JSON                │
│  Location: /output/scholarship/                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│          TERTIARY LAYER: Jupyter Synthesis                   │
│  • Cross-layer pattern analysis                             │
│  • Entropy trend visualization                              │
│  • Multi-platform research comparison                       │
│  • Thematic mapping & citation networks                     │
│  • Recursive refinement loops                               │
│                                                              │
│  Output: Synthesis reports & visualizations                 │
│  Location: /output/synthesis/ & notebooks/                  │
└─────────────────────────────────────────────────────────────┘
                       │
                       ▼
               ITERATIVE REFINEMENT
          (Breadth-and-Depth Method)
```

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd jvpiter-inquiry-labors

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

### 2. Run Your First Atomization

Navigate to `notebooks/recursive_research/01_text_atomization_workflow.ipynb` and execute cells sequentially.

**What it does:**
- Loads a literary text excerpt
- Extracts n-grams (frequent word sequences)
- Calculates entropy metrics (complexity measures)
- Generates glyph fusion mappings (symbolic representations)
- Exports daily outputs (Markdown report + JSON archive)

### 3. Ingest AI Scholarship

Use the scholarship ingestion tools to structure research from AI platforms:

```python
from scholarship import ScholarshipIngester, AISource
from pathlib import Path

ingester = ScholarshipIngester(Path('output/scholarship'))

ingester.ingest_research(
    content="Your AI-generated research content...",
    source=AISource.PERPLEXITY,
    query="Homeric formulae and computational analysis",
    title="Formulaic Expression in Homer",
    tags=['homer', 'oral tradition', 'n-grams'],
    citations=[...]
)
```

### 4. Synthesize Across Layers

Open `notebooks/recursive_research/02_ai_scholarship_synthesis.ipynb` to:
- Visualize entropy trends across atomization runs
- Compare AI research outputs by platform
- Extract frequently cited sources
- Generate comprehensive synthesis reports

## Module Reference

### `src/atomization/`

**Core atomization engine for recursive text analysis.**

#### `atomizer.py` - Main Atomization Interface
```python
from atomization import TextAtomizer

atomizer = TextAtomizer(
    text="Your literary text...",
    title="Odyssey - Book 1",
    metadata={'author': 'Homer', 'translator': 'Fagles'}
)

results = atomizer.atomize(
    ngram_range=(1, 3),  # unigrams through trigrams
    top_n=20,
    calculate_entropy=True,
    map_glyphs=True
)

# Export daily outputs
atomizer.export_daily_output(Path('data/processed/atomization'))
```

#### `ngrams.py` - N-gram Extraction
```python
from atomization import NGramExtractor

extractor = NGramExtractor(text)
bigrams = extractor.extract_ngrams(n=2, top_n=20)
diversity = extractor.get_ngram_diversity(n=2)
```

#### `entropy.py` - Information-Theoretic Analysis
```python
from atomization import EntropyAnalyzer

analyzer = EntropyAnalyzer(text)
shannon = analyzer.shannon_entropy(unit='words')
normalized = analyzer.normalized_entropy()
compression = analyzer.compression_ratio()
diversity = analyzer.lexical_diversity()
```

#### `glyphs.py` - Symbolic Transformation
```python
from atomization import GlyphFusionMapper

mapper = GlyphFusionMapper(glyph_set='geometric')
fusions = mapper.create_fusion_map(['wine-dark sea', 'rosy-fingered dawn'])
encoded = mapper.encode_text(original_text)
```

### `src/scholarship/`

**Multi-platform AI research orchestration and synthesis.**

#### `ingestion.py` - Structured Research Storage
```python
from scholarship import ScholarshipIngester, AISource

ingester = ScholarshipIngester(base_dir)
path = ingester.ingest_research(
    content="Research content",
    source=AISource.CLAUDE,
    query="Analyze recursive patterns in Divine Comedy",
    tags=['dante', 'recursion', 'structure']
)

# Batch ingestion
ingester.ingest_batch([{...}, {...}])

# Generate searchable index
index = ingester.create_index(output_path='index.json')
```

#### `synthesis.py` - Cross-Platform Analysis
```python
from scholarship import ScholarshipSynthesizer

synthesizer = ScholarshipSynthesizer(scholarship_dir)

# Thematic analysis
themes = synthesizer.analyze_by_theme(tags=['homer', 'virgil'])

# Source comparison
comparison = synthesizer.compare_sources(['homecoming', 'nostos'])

# Citation extraction
frequent_cites = synthesizer.extract_citations(min_frequency=2)

# Generate report
report = synthesizer.generate_synthesis_report(output_path='report.md')
```

#### `workflow.py` - Multi-Platform Orchestration
```python
from scholarship import MultiPlatformOrchestrator

orchestrator = MultiPlatformOrchestrator()

# Generate workflow template
orchestrator.generate_workflow_file(
    workflow_name='literary_analysis',
    output_path='workflow.md',
    params={'topic': 'homecoming', 'work': 'Odyssey'}
)

# Available workflows:
# - 'literary_analysis': Research → Analysis → Generation
# - 'text_atomization': Research → Analysis → Generation → Refinement
```

## Recursive Process Methodologies

### Breadth-and-Depth Method

Combines surface mapping with focused exploration:

1. **Breadth Phase**: 61 identical runs on *Odyssey* excerpts
   - Establishes baseline entropy patterns
   - Identifies stable n-gram distributions
   - Maps recurring glyph fusions

2. **Depth Phase**: "Test pits" with variant texts
   - *Metamorphoses* (transformation motifs)
   - *Canterbury Tales* (narrative frames)
   - *Finnegans Wake* (linguistic recursion)

3. **Remapping**: Synthesize cross-work patterns
   - Compare entropy deltas
   - Identify universal vs. work-specific patterns
   - Refine glyph fusion logic

### Recursive Frame Analysis

Track distinctions and contextual frames across works:

```python
# Example: Homecoming motifs across epic traditions
works = ['Odyssey', 'Aeneid', 'Divine Comedy', 'Ulysses']

for work in works:
    # Atomize text
    atomizer = TextAtomizer(load_text(work), title=work)
    results = atomizer.atomize()

    # Extract homecoming n-grams
    homecoming_terms = ['home', 'return', 'journey', 'nostos']
    relevant_ngrams = filter_ngrams(results, homecoming_terms)

    # Compare entropy signatures
    compare_entropy(work, results['entropy'])
```

## Multi-Platform AI Workflows

### Sequential Orchestration Pattern

**Perplexity → Claude → GPT** (not parallel—each builds on previous)

#### 1. Perplexity: Contextual Research
- Query: "Homeric formulae and computational text analysis"
- Output: Citations, scholarly context, key debates
- Ingest: `AISource.PERPLEXITY`, tags: `['homer', 'formulae']`

#### 2. Claude: Strategic Synthesis
- Input: Perplexity research + atomization data
- Query: "Analyze patterns in research findings, map frameworks"
- Output: Conceptual structures, analytical frameworks
- Ingest: `AISource.CLAUDE`, tags: `['synthesis', 'frameworks']`

#### 3. GPT/Grok: Creative Generation
- Input: Claude analysis
- Query: "Generate alternative glyph mappings, experimental visualizations"
- Output: Creative variations, alternative interpretations
- Ingest: `AISource.GPT`, tags: `['creative', 'experimental']`

### Automation with n8n

```
[Trigger: Daily 9am]
    ↓
[Perplexity API] → Research query
    ↓
[Parse Citations] → Save JSON
    ↓
[Claude API] → Analyze research + atomization data
    ↓
[GPT API] → Generate variations
    ↓
[Jupyter Execute] → Update synthesis notebook
    ↓
[Export] → Markdown/JSON to repository
```

## File Structure Reference

```
jvpiter-inquiry-labors/
├── data/
│   ├── raw/corpora/              # Literary texts (git-ignored)
│   │   ├── odyssey_excerpt.txt
│   │   ├── metamorphoses_book1.txt
│   │   └── beowulf_grendel.txt
│   ├── processed/atomization/    # Atomization outputs
│   │   ├── output_2025-01-15.md  # Daily Markdown reports
│   │   ├── output_2025-01-16.md
│   │   └── all_outputs.json      # Consolidated archive
│   └── external/                 # Third-party datasets
│
├── output/
│   ├── scholarship/              # AI research ingestion
│   │   ├── perplexity/
│   │   │   ├── 2025-01-15_120000_homeric-formulae.md
│   │   │   └── 2025-01-15_120000_homeric-formulae.json
│   │   ├── claude/
│   │   └── gpt/
│   ├── synthesis/                # Cross-layer reports
│   │   └── synthesis_report.md
│   └── figures/                  # Visualizations
│
├── src/
│   ├── atomization/              # Text atomization modules
│   │   ├── __init__.py
│   │   ├── atomizer.py           # Main interface
│   │   ├── ngrams.py             # N-gram extraction
│   │   ├── entropy.py            # Entropy analysis
│   │   └── glyphs.py             # Glyph fusion
│   ├── scholarship/              # AI research modules
│   │   ├── __init__.py
│   │   ├── ingestion.py          # Research storage
│   │   ├── synthesis.py          # Cross-platform analysis
│   │   └── workflow.py           # Orchestration templates
│   └── data/loader.py            # Data loading utilities
│
├── notebooks/
│   ├── recursive_research/
│   │   ├── 01_text_atomization_workflow.ipynb
│   │   └── 02_ai_scholarship_synthesis.ipynb
│   └── templates/                # Reusable templates
│
├── tests/
│   └── test_atomization.py       # Unit tests (add yours)
│
└── RECURSIVE_RESEARCH_GUIDE.md   # This file
```

## Example Workflows

### Daily Atomization Routine

```python
from atomization import TextAtomizer
from pathlib import Path
from datetime import datetime

# Load day's text excerpt
with open('data/raw/corpora/odyssey_book5.txt') as f:
    text = f.read()

# Atomize
atomizer = TextAtomizer(
    text=text,
    title=f"Odyssey Book 5 - {datetime.now().strftime('%Y-%m-%d')}",
    metadata={'book': 5, 'lines': '1-300'}
)

results = atomizer.atomize(ngram_range=(1, 4), top_n=30)

# Export
output_dir = Path('data/processed/atomization')
atomizer.export_daily_output(output_dir)

print(f"Atomization complete. Entropy: {results['entropy']['shannon_entropy']:.3f}")
```

### Multi-Work Comparison

```python
from atomization import TextAtomizer
import matplotlib.pyplot as plt

works = {
    'Odyssey': 'data/raw/corpora/odyssey_excerpt.txt',
    'Aeneid': 'data/raw/corpora/aeneid_excerpt.txt',
    'Divine Comedy': 'data/raw/corpora/inferno_excerpt.txt'
}

entropies = {}

for title, path in works.items():
    with open(path) as f:
        text = f.read()

    atomizer = TextAtomizer(text, title=title)
    results = atomizer.atomize()

    entropies[title] = results['entropy']['shannon_entropy']

# Visualize
plt.bar(entropies.keys(), entropies.values())
plt.title('Shannon Entropy Across Epic Traditions')
plt.ylabel('Entropy (bits)')
plt.show()
```

### Full Three-Layer Pipeline

```python
from atomization import TextAtomizer
from scholarship import ScholarshipIngester, ScholarshipSynthesizer, AISource
from pathlib import Path

# LAYER 1: Atomize text
text = open('odyssey.txt').read()
atomizer = TextAtomizer(text, title="Odyssey Complete")
atomization_results = atomizer.atomize()
atomizer.export_daily_output(Path('data/processed/atomization'))

# LAYER 2: Ingest AI research
ingester = ScholarshipIngester(Path('output/scholarship'))

# (Manually run Perplexity query, paste result)
perplexity_output = """..."""
ingester.ingest_research(
    content=perplexity_output,
    source=AISource.PERPLEXITY,
    query="Homeric oral formulae computational analysis",
    tags=['homer', 'formulae', 'computational']
)

# (Manually run Claude analysis, paste result)
claude_output = """..."""
ingester.ingest_research(
    content=claude_output,
    source=AISource.CLAUDE,
    query="Synthesize Perplexity research with atomization patterns",
    tags=['synthesis', 'patterns']
)

# LAYER 3: Synthesize in Jupyter
# Open notebooks/recursive_research/02_ai_scholarship_synthesis.ipynb
# Execute cells to generate visualizations and reports
```

## Best Practices

### 1. Iterative Refinement
- Start with small text excerpts (100-500 words)
- Run daily atomizations to build archive
- Compare results across runs to identify stable patterns
- Gradually expand to full books/cantos

### 2. Thematic Tagging
- Use consistent tags across AI scholarship (`['homer', 'oral-tradition']`)
- Tag atomization runs by work/book/canto
- Enable cross-referencing through tags

### 3. Citation Tracking
- Always include URLs in AI research citations
- Track which sources appear across multiple platforms
- Use `extract_citations(min_frequency=2)` to find consensus sources

### 4. Version Control
- Commit daily atomization archives
- Track notebook changes in git
- Use branches for experimental analyses

### 5. Reproducibility
- Save raw text files in `data/raw/corpora/`
- Document preprocessing steps in notebooks
- Include metadata in all atomization runs

## Extending the Framework

### Custom N-gram Analysis

```python
from atomization.ngrams import NGramExtractor

class CustomNGramExtractor(NGramExtractor):
    def extract_epithets(self, top_n=10):
        """Extract Homeric epithets (adjective-noun bigrams)."""
        bigrams = self.extract_ngrams(2, top_n=100)

        # Simple heuristic: filter for adjective patterns
        epithets = [
            (bg, freq) for bg, freq in bigrams
            if self._is_epithet_pattern(bg)
        ]

        return epithets[:top_n]

    def _is_epithet_pattern(self, bigram):
        # Implement POS tagging or pattern matching
        adjectives = ['wine-dark', 'rosy-fingered', 'swift-footed']
        return any(adj in bigram for adj in adjectives)
```

### Custom Glyph Sets

```python
from atomization.glyphs import GlyphFusionMapper

# Add custom glyph set
GlyphFusionMapper.GLYPH_SETS['homeric'] = [
    '⚡', '🌊', '🏛️', '⚔️', '🛡️', '🏹', '🌅', '🍷', '🌙', '☀️'
]

mapper = GlyphFusionMapper(glyph_set='homeric')
```

### Custom Workflow Templates

```python
from scholarship.workflow import MultiPlatformOrchestrator, WorkflowStep, WorkflowStage

orchestrator = MultiPlatformOrchestrator()

orchestrator.register_workflow(
    'homeric_analysis',
    steps=[
        WorkflowStep(
            stage=WorkflowStage.RESEARCH,
            platform='perplexity',
            prompt_template="Research Homeric {theme} in {book}",
            expected_output='Scholarly context'
        ),
        # Add more steps...
    ]
)
```

## Troubleshooting

### Import Errors
```python
# Ensure src/ is in path
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent / 'src'))
```

### Empty Atomization Results
- Check text length (need >50 words for meaningful n-grams)
- Verify ngram_range values (start with (1, 3))
- Ensure text encoding is UTF-8

### Visualization Not Showing
```python
# Add to notebook
%matplotlib inline
import matplotlib.pyplot as plt
```

## Resources

### Computational Literary Analysis
- Franco Moretti - *Distant Reading*
- Matthew L. Jockers - *Macroanalysis*
- Ted Underwood - *Distant Horizons*

### Information Theory & Text
- Claude Shannon - *A Mathematical Theory of Communication*
- Cover & Thomas - *Elements of Information Theory*

### Digital Humanities
- [Programming Historian](https://programminghistorian.org/)
- [Distant Reading for European Literary History](https://www.distant-reading.net/)

### Python Text Analysis
- NLTK - Natural Language Toolkit
- spaCy - Industrial-strength NLP
- Gensim - Topic modeling

## Support

For questions, issues, or contributions:
- Open an issue in the GitHub repository
- Consult existing notebooks in `notebooks/recursive_research/`
- Review module docstrings: `help(TextAtomizer)`

## License

See LICENSE file for details.

---

**Forward-Backward Ethos**: Generative (AI) → Recursive (iterative) → Micro/Macro (atoms to universals)
