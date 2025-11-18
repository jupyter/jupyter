# Recursive Research Notebooks

**Jupyter notebooks for three-layer literary-computational analysis**

## Notebooks

### 01_text_atomization_workflow.ipynb
**Primary Layer: Text Atomization**

Recursive text decomposition methodology:
- Load literary corpora (Odyssey, Metamorphoses, etc.)
- Extract n-grams (unigrams → trigrams+)
- Calculate entropy metrics (Shannon, compression ratio)
- Generate glyph fusion mappings
- Export daily Markdown + JSON archives

**Outputs**: `data/processed/atomization/`

---

### 02_ai_scholarship_synthesis.ipynb
**Tertiary Layer: Multi-Platform Synthesis**

Cross-layer integration:
- Visualize atomization trends (entropy, lexical diversity)
- Analyze AI research by platform (Perplexity, Claude, GPT)
- Compare thematic patterns across scholarship
- Extract citation networks
- Generate synthesis reports

**Inputs**:
- Primary layer: `data/processed/atomization/all_outputs.json`
- Secondary layer: `output/scholarship/*/`

**Outputs**: `output/synthesis/`

---

## Execution Order

### First-Time Setup
1. Run `01_text_atomization_workflow.ipynb` to generate initial atomization data
2. Manually ingest AI scholarship using examples in notebook 02
3. Run `02_ai_scholarship_synthesis.ipynb` to synthesize layers

### Daily Workflow
1. Load new text excerpt in notebook 01
2. Execute atomization pipeline
3. Review outputs in `data/processed/atomization/output_YYYY-MM-DD.md`
4. Feed atomization results to AI platforms (Perplexity → Claude → GPT)
5. Ingest AI outputs using `scholarship.ScholarshipIngester`
6. Re-run synthesis notebook to update visualizations

## Breadth-and-Depth Strategy

### Breadth Phase (Days 1-61)
- Process *Odyssey* excerpts daily
- Keep parameters constant (same ngram_range, top_n)
- Build baseline entropy distribution
- Identify stable n-gram patterns

**Goal**: Establish "surface map" of Homeric formulae

### Depth Phase ("Test Pits")
- Days 15, 30, 45: Insert *Metamorphoses* excerpts
- Days 20, 40, 60: Insert *Beowulf* excerpts
- Days 25, 50: Insert *Divine Comedy* cantos

**Goal**: Compare cross-work patterns, identify genre-specific vs. universal patterns

### Remapping Phase (Days 62+)
- Synthesize breadth + depth findings
- Refine glyph fusion logic based on patterns
- Adjust entropy thresholds
- Develop comparative frameworks

## Customization

### Add Custom Analysis

Create new cells or notebooks extending the framework:

```python
# Example: Track specific motifs across works
from atomization import TextAtomizer

motif_terms = ['homecoming', 'journey', 'return', 'nostos']

for work in ['odyssey', 'aeneid', 'divine_comedy']:
    atomizer = TextAtomizer(load_text(work), title=work)
    results = atomizer.atomize()

    # Filter n-grams for motif terms
    motif_ngrams = [
        ng for ng in results['ngrams']['2-grams']
        if any(term in ng['text'] for term in motif_terms)
    ]

    print(f"{work}: {len(motif_ngrams)} motif-related bigrams")
```

### Export Custom Visualizations

```python
import matplotlib.pyplot as plt
from pathlib import Path

# Create visualization
fig, ax = plt.subplots(figsize=(12, 6))
# ... plotting code ...

# Save to output
output_path = Path('output/synthesis/figures/custom_plot.png')
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
```

## Dependencies

All notebooks require packages from `requirements.txt`:
- `jupyter`, `jupyterlab`
- `numpy`, `pandas`
- `matplotlib`, `seaborn`, `plotly`
- `scikit-learn`

Install: `pip install -r requirements.txt`

## Tips

### Performance
- Start with small text excerpts (200-500 words)
- Use `top_n=20` for initial explorations (increase to 50+ for detailed analysis)
- Generate visualizations incrementally (don't recompute entire archive each run)

### Organization
- Use consistent date formats in atomization exports
- Tag AI scholarship with descriptive, searchable keywords
- Create separate notebooks for specific research questions

### Reproducibility
- Restart kernel and run all cells before finalizing
- Include markdown cells explaining methodology
- Save notebook outputs to track analysis evolution

## Troubleshooting

**"Module not found" errors**:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent / 'src'))
```

**Visualizations not showing**:
```python
%matplotlib inline
```

**JSON file not found**:
- Verify you've run atomization notebook first
- Check file path: `data/processed/atomization/all_outputs.json`

**Empty scholarship directory**:
- Use ingestion examples in notebook 02 to add research items
- Manually create `.md` files in `output/scholarship/perplexity/` etc.

## Next Steps

After completing these notebooks:
1. Create custom workflows for your research questions
2. Develop specialized visualizations
3. Extend modules in `src/atomization/` and `src/scholarship/`
4. Contribute patterns back to template notebooks
