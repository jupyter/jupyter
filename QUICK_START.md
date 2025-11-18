# Quick Start: Recursive Research Framework

**Logic-Driven Literary Analysis Pipeline**

## Immediate Next Actions

### 1. Create Pull Request

Visit: https://github.com/ivi374forivi/jvpiter-inquiry-labors/pull/new/claude/recursive-research-formats-016PkruEDgzD5dZ3rTajvDgU

- Title: "Implement Recursive Research Framework for Literary-Computational Scholarship"
- Body: Copy from `PR_DESCRIPTION.md`

### 2. Execute First Analysis (5 minutes)

```bash
cd /home/user/jvpiter-inquiry-labors
jupyter lab
```

Open: `notebooks/recursive_research/01_text_atomization_workflow.ipynb`

**Expected Output:**
- N-gram patterns from Odyssey opening
- Entropy metrics (Shannon, lexical diversity)
- Glyph fusion mappings
- Daily exports in `data/processed/atomization/`

### 3. Begin Daily Iteration

**Breadth Phase (Days 1-61):**

```python
from atomization import TextAtomizer
from pathlib import Path

# Load daily Odyssey excerpt
with open('data/raw/corpora/odyssey_book1_lines1-50.txt') as f:
    text = f.read()

# Atomize
atomizer = TextAtomizer(text, title=f"Odyssey Day {day_number}")
results = atomizer.atomize(ngram_range=(1, 3), top_n=20)

# Export
atomizer.export_daily_output(Path('data/processed/atomization'))

# Log entropy for tracking
print(f"Day {day_number}: Entropy = {results['entropy']['shannon_entropy']:.4f}")
```

**Track**: Entropy convergence, stable n-gram patterns, formulaic repetition

### 4. Multi-Platform AI Workflow

**Sequential Pattern (Perplexity → Claude → GPT):**

```bash
# Step 1: Research query
Query Perplexity: "Homeric formulae computational analysis n-gram patterns"
→ Save citations, scholarly context

# Step 2: Ingest research
python3 << PYEOF
from scholarship import ScholarshipIngester, AISource
from pathlib import Path

ingester = ScholarshipIngester(Path('output/scholarship'))
ingester.ingest_research(
    content="""[Paste Perplexity output]""",
    source=AISource.PERPLEXITY,
    query="Homeric formulae computational analysis",
    tags=['homer', 'formulae', 'n-grams']
)
PYEOF

# Step 3: Analyze with Claude
Query Claude: "Analyze research findings + atomization data from output_2025-11-18.md"
→ Synthesize patterns, map frameworks

# Step 4: Ingest analysis
# (repeat ingestion with AISource.CLAUDE)

# Step 5: Generate with GPT/Grok
Query GPT: "Generate alternative glyph mappings based on analysis"
→ Creative variations

# Step 6: Synthesize
# Run notebook 02: ai_scholarship_synthesis.ipynb
```

## Logical Architecture Flow

```
INPUT: Literary Text
  ↓
  ├─ Tokenization (word-level)
  ├─ N-gram Extraction (1→3)
  ├─ Frequency Analysis
  ├─ Entropy Calculation
  └─ Glyph Mapping
  ↓
PRIMARY OUTPUT: JSON + Markdown
  ↓
  ├─ Feed to AI platforms
  ├─ Generate scholarly context
  └─ Synthesize patterns
  ↓
SECONDARY OUTPUT: AI Research
  ↓
  ├─ Load in Jupyter
  ├─ Visualize trends
  └─ Cross-platform comparison
  ↓
TERTIARY OUTPUT: Synthesis Report
  ↓
RECURSIVE REFINEMENT
  ↓
  ├─ Adjust parameters
  ├─ Test new corpora
  └─ Iterate methodology
```

## Validation Checkpoints

**Day 1:**
- [ ] Odyssey excerpt atomized
- [ ] Entropy baseline established
- [ ] Exports verified in `data/processed/atomization/`

**Week 1:**
- [ ] 7 daily atomizations complete
- [ ] Entropy trend visible
- [ ] Top n-grams stabilizing

**Week 2:**
- [ ] First "test pit" (*Metamorphoses* excerpt)
- [ ] Cross-work entropy comparison
- [ ] AI scholarship ingestion started

**Month 1:**
- [ ] 30 atomization runs
- [ ] Perplexity → Claude → GPT workflow tested
- [ ] Synthesis report generated

**Day 61:**
- [ ] Breadth phase complete
- [ ] Baseline entropy distribution established
- [ ] Stable formulaic patterns identified
- [ ] Ready for depth phase

## Testing Commands

```bash
# Verify installation
python3 -c "from atomization import TextAtomizer; print('✓ Atomization loaded')"
python3 -c "from scholarship import ScholarshipIngester; print('✓ Scholarship loaded')"

# Run tests
pytest tests/test_atomization.py -v

# Check outputs
ls -lh data/processed/atomization/
cat data/processed/atomization/output_*.md | head -20

# Verify JSON structure
python3 -m json.tool data/processed/atomization/all_outputs.json | head -30
```

## Logical Principles Applied

1. **Information Theory**: Shannon entropy quantifies text complexity
2. **Statistical Significance**: Frequency ranking identifies formulae
3. **Symbolic Abstraction**: Glyph fusion enables pattern compression
4. **Iterative Refinement**: Daily atomization builds comparative dataset
5. **Cross-Platform Synthesis**: Multiple AI perspectives reduce bias
6. **Reproducibility**: Structured exports enable validation

## Advanced Usage

**Custom N-gram Analysis:**
```python
from atomization import NGramExtractor

extractor = NGramExtractor(text)
diversity = extractor.get_ngram_diversity(n=2)  # Measure uniqueness
all_ngrams = extractor.extract_all_ngrams(min_n=1, max_n=5)
```

**Entropy Comparison:**
```python
from atomization import EntropyAnalyzer

odyssey_entropy = EntropyAnalyzer(odyssey_text).shannon_entropy()
metamorphoses_entropy = EntropyAnalyzer(metamorphoses_text).shannon_entropy()

delta = abs(odyssey_entropy - metamorphoses_entropy)
print(f"Entropy delta: {delta:.4f} bits")
```

**Custom Glyph Sets:**
```python
from atomization import GlyphFusionMapper

# Homeric themed glyphs
GlyphFusionMapper.GLYPH_SETS['homeric'] = ['⚡', '🌊', '🏛️', '⚔️', '🛡️']
mapper = GlyphFusionMapper(glyph_set='homeric')
```

---

**Status**: Framework operational. Logic validated. Ready for production iteration.

**Next**: Execute → Measure → Analyze → Refine → Repeat
