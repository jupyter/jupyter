# Phase-Specific Task Checklists

**Quick Reference for Daily/Weekly Tasks**

---

## Phase 0: Initialization (Week 1)

### Day -7: Environment Setup
- [ ] Clone repository: `git clone <repo-url>`
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate: `source venv/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Test installation: `pytest tests/ -v`
- [ ] Verify 21/21 tests passing

### Day -6: Framework Validation
- [ ] Run batch atomization: `python scripts/batch_atomize_corpora.py`
- [ ] Check entropy values: Homer (6.79), Virgil (6.93), Joyce (6.99)
- [ ] Inspect `data/processed/atomization/batch/BATCH_REPORT.md`
- [ ] Verify JSON structure: `cat data/processed/atomization/batch/comparative_summary.json | jq`

### Day -5: Jupyter Setup
- [ ] Launch Jupyter: `jupyter lab`
- [ ] Open: `notebooks/recursive_research/01_text_atomization_workflow.ipynb`
- [ ] Execute all cells (Kernel → Restart & Run All)
- [ ] Verify visualizations render
- [ ] Check daily output: `ls data/processed/atomization/output_*.md`

### Day -4: Corpus Preparation
- [ ] Download Odyssey complete: Project Gutenberg #1727
- [ ] Split into 61 excerpts (~50 lines each)
- [ ] Save as: `data/raw/corpora/odyssey/excerpts/day_01.txt` through `day_61.txt`
- [ ] Create metadata for each: `day_XX.meta.json`
- [ ] Verify count: `ls data/raw/corpora/odyssey/excerpts/*.txt | wc -l` → 61

### Day -3: AI Platform Setup
- [ ] Perplexity account: https://www.perplexity.ai/
- [ ] Claude account: https://claude.ai/
- [ ] ChatGPT account: https://chat.openai.com/
- [ ] Test `ScholarshipIngester`:
  ```python
  from scholarship import ScholarshipIngester, AISource
  ingester = ScholarshipIngester(Path('output/scholarship'))
  ingester.ingest_research(content="Test", source=AISource.PERPLEXITY, query="Test")
  ```

### Day -2: Documentation Review
- [ ] Read: `RECURSIVE_RESEARCH_GUIDE.md` (30 min)
- [ ] Read: `LIFECYCLE_ROADMAP.md` (60 min)
- [ ] Review: `notebooks/recursive_research/README.md` (15 min)
- [ ] Bookmark: Corpus index, API docs

### Day -1: Baseline Measurement
- [ ] Randomly select 5 Odyssey excerpts
- [ ] Atomize each with identical parameters
- [ ] Calculate: mean_entropy, std_dev, range
- [ ] Document in: `BASELINE_METRICS.md`
- [ ] Expected: Mean ≈ 6.0-6.5 bits, Std Dev < 0.5

### Day 0: Launch Preparation
- [ ] Create: `RESEARCH_LOG.md`
- [ ] Calendar: Set daily 9am reminder "Atomize Odyssey excerpt"
- [ ] Prepare: `data/raw/corpora/odyssey/excerpts/day_01.txt` ready to load
- [ ] Review research questions
- [ ] Mental preparation: Commit to 61-day consistency

---

## Phase 1: Breadth Foundation (Days 1-61)

### Daily Routine (15 minutes/day)

#### Every Morning
- [ ] Load excerpt: `day_XX = Path('data/raw/corpora/odyssey/excerpts/day_XX.txt').read_text()`
- [ ] Atomize:
  ```python
  atomizer = TextAtomizer(day_XX, title=f"Odyssey Day {XX}")
  results = atomizer.atomize(ngram_range=(1,3), top_n=20)
  atomizer.export_daily_output(Path('data/processed/atomization/daily/'))
  ```
- [ ] Log in `RESEARCH_LOG.md`:
  ```markdown
  ## Day XX - YYYY-MM-DD
  - Entropy: X.XXXX bits
  - Lexical Diversity: 0.XXXX
  - Top trigram: 'text here' (Nx)
  - Notes: [Any observations]
  ```

### Weekly Review (Sundays, 30 minutes)

- [ ] Calculate week stats:
  ```python
  entropies = [6.12, 6.08, 6.15, 6.09, 6.13, 6.11, 6.10]
  import numpy as np
  print(f"Mean: {np.mean(entropies):.4f}")
  print(f"Std: {np.std(entropies):.4f}")
  ```
- [ ] Update: `WEEKLY_SUMMARY_WK_XX.md`
- [ ] Plot entropy trend (matplotlib)
- [ ] Identify: Top 5 recurring trigrams across week
- [ ] Prepare next week's excerpts

### Milestone Checkpoints

#### Day 7 (Week 1)
- [ ] Verify 7/7 atomizations complete
- [ ] Calculate mean entropy (expect: 6.0-6.5 bits)
- [ ] Identify ≥3 recurring trigrams
- [ ] Review for processing errors
- [ ] Decision: Continue or adjust parameters?

#### Day 21 (Week 3)
- [ ] Verify 21/21 complete
- [ ] Calculate 95% CI for entropy
- [ ] Count formulaic patterns (≥5 recurring ≥5x)
- [ ] Create: `21_DAY_ANALYSIS.md`
- [ ] Visualize: Entropy timeline plot

#### Day 35 (Week 5)
- [ ] Verify 35/35 complete
- [ ] Test convergence: Std dev < 0.3?
- [ ] Catalogue: Top 10 formulae
- [ ] Create: `MIDPOINT_REPORT.md`
- [ ] Update visualizations

#### Day 49 (Week 7)
- [ ] Verify 49/49 complete
- [ ] Statistical significance: t-test vs. baseline
- [ ] Formulaic inventory: 20+ patterns
- [ ] Create: `BREADTH_PHASE_PREVIEW.md`
- [ ] Plan depth phase test pits

#### Day 61 (Week 9) - PHASE COMPLETION
- [ ] Verify **61/61 complete** ✓
- [ ] Generate `BREADTH_PHASE_REPORT.md`
- [ ] Consolidate: `odyssey_baseline_61days.json`
- [ ] Create visualization suite (5+ plots)
- [ ] Notebook: `04_odyssey_baseline_analysis.ipynb`
- [ ] Validation gate checklist (see LIFECYCLE_ROADMAP.md)

---

## Phase 2: Depth Exploration (Days 62-120)

### Daily Routine (15 minutes/day, except test pits)

#### Regular Days (Odyssey continuation)
- [ ] Load excerpt: `day_XX.txt`
- [ ] Atomize (same parameters as Phase 1)
- [ ] Log in `RESEARCH_LOG.md`
- [ ] Note: "Odyssey continuation (post-breadth)"

#### Test Pit Days (30 minutes)

**Day 70: Metamorphoses #1**
- [ ] Load: `ovid_metamorphoses_excerpt1.txt`
- [ ] Atomize
- [ ] Compare to Odyssey baseline:
  ```python
  odyssey_mean = 6.15  # From Phase 1
  ovid_entropy = results['entropy']['shannon_entropy']
  delta = ovid_entropy - odyssey_mean
  print(f"Delta: {delta:.4f} bits")
  ```
- [ ] Document in: `TEST_PIT_DAY70_OVID.md`
- [ ] Note unique n-grams (transformation vocab)

**Day 77: Aeneid #1**
- [ ] Load: `virgil_aeneid_excerpt1.txt`
- [ ] Atomize + compare
- [ ] Document: `TEST_PIT_DAY77_VIRGIL.md`

**Day 84: Divine Comedy #1**
- [ ] Load: `dante_divinecomedy_excerpt1.txt`
- [ ] Atomize + compare
- [ ] Document: `TEST_PIT_DAY84_DANTE.md`
- [ ] Note terza rima structural impact

**Day 91: Beowulf #1**
- [ ] Load: `beowulf_excerpt1.txt`
- [ ] Atomize + compare
- [ ] Document: `TEST_PIT_DAY91_BEOWULF.md`
- [ ] Note alliterative formulae

**Day 98: Canterbury Tales #1**
- [ ] Load: `chaucer_canterbury_excerpt1.txt`
- [ ] Atomize + compare
- [ ] Document: `TEST_PIT_DAY98_CHAUCER.md`

**Day 105: Finnegans Wake #1**
- [ ] Load: `joyce_finnegans_excerpt1.txt`
- [ ] Atomize + compare
- [ ] Document: `TEST_PIT_DAY105_JOYCE.md`
- [ ] Expect entropy spike (≥6.8 bits)

**Days 112, 119**: Second round test pits

### Bi-Weekly Synthesis (Every 2 weeks)

- [ ] Review all test pits completed to date
- [ ] Update comparative matrix:
  | Work | Entropy | Δ vs Odyssey | Diversity | Unique N-grams |
  |------|---------|--------------|-----------|----------------|
- [ ] Update: `DEPTH_PHASE_PROGRESS.md`
- [ ] Prepare next test pits

### Milestone Checkpoints

#### Day 70 (First Test Pit)
- [ ] Ovid atomization complete
- [ ] Delta entropy calculated (expect ≥0.3 bits)
- [ ] Transformation vocabulary identified
- [ ] Comparison documented
- [ ] Decision: Test pit methodology validated?

#### Day 91 (Medieval Cluster)
- [ ] Dante + Beowulf complete
- [ ] Medieval entropy range established
- [ ] Structural impacts quantified (terza rima, alliteration)
- [ ] Create: `MEDIEVAL_PATTERNS_ANALYSIS.md`

#### Day 105 (Modernist Peak)
- [ ] Joyce atomization complete
- [ ] Entropy spike confirmed
- [ ] Multilingual patterns catalogued
- [ ] Create: `MODERNIST_COMPLEXITY_REPORT.md`

#### Day 120 (PHASE COMPLETION)
- [ ] 14 test pits complete (7 works × 2)
- [ ] Generate: `DEPTH_PHASE_REPORT.md`
- [ ] Consolidate: `comparative_120days.json`
- [ ] Notebook: `05_depth_phase_cross_work_analysis.ipynb`
- [ ] Statistical tests: ANOVA, t-tests
- [ ] Validation gate checklist

---

## Phase 3: AI Integration (Months 3-6)

### Month 3: Perplexity Research (Weekly tasks)

#### Week 13: Homeric Scholarship
- [ ] Query 1: "Homeric formulae computational analysis"
- [ ] Query 2: "Wine-dark sea oral tradition repetition"
- [ ] Query 3: "Shannon entropy oral vs written epic"
- [ ] Collect ≥15 citations
- [ ] Ingest all:
  ```python
  ingester.ingest_research(
      content=perplexity_output,
      source=AISource.PERPLEXITY,
      query="...",
      tags=['homer', 'oral-tradition', 'formulae'],
      citations=[...]
  )
  ```
- [ ] Create: `output/scholarship/perplexity/week13_summary.md`

#### Week 14: Roman Epic (repeat structure)
- [ ] 3 queries on Ovid/Virgil
- [ ] ≥15 citations
- [ ] Ingest with tags: `ovid`, `virgil`, `roman-epic`

#### Week 15: Medieval (repeat)
#### Week 16: Modernist (repeat)

### Month 4: Claude Synthesis (Weekly tasks)

#### Week 17: Breadth Synthesis
- [ ] Prepare prompt with Phase 1 data
- [ ] Paste `BREADTH_PHASE_REPORT.md` findings
- [ ] Include Perplexity Week 13 findings
- [ ] Submit to Claude
- [ ] Ingest response:
  ```python
  ingester.ingest_research(
      content=claude_output,
      source=AISource.CLAUDE,
      query="Synthesize 61-day Odyssey baseline with scholarship",
      tags=['synthesis', 'homer', 'frameworks']
  )
  ```
- [ ] Create: `output/scholarship/claude/week17_synthesis.md`

#### Week 18: Cross-Work Synthesis (repeat structure)
#### Week 19: Framework Development (repeat)
#### Week 20: Research Questions Refinement (repeat)

### Month 5: GPT Generation (Weekly tasks)

#### Week 21: Glyph Variations
- [ ] Prepare prompt with n-gram patterns
- [ ] Request 4 alternative glyph sets
- [ ] Submit to GPT
- [ ] Ingest response
- [ ] Document: `output/scholarship/gpt/week21_glyph_variations.md`

#### Week 22-24: (Repeat for experimental parameters, visualizations, cross-disciplinary)

### Month 6: Synthesis (Bi-weekly tasks)

#### Week 25: Notebook Development
- [ ] Create: `06_three_layer_synthesis.ipynb`
- [ ] Section 1: Primary layer data load
- [ ] Section 2: Secondary layer scholarship load
- [ ] Section 3: Cross-layer synthesis
- [ ] Section 4: Visualization suite
- [ ] Test: Execute all cells without errors

#### Week 26: Report Generation
- [ ] Draft: `PHASE3_AI_INTEGRATION_REPORT.md`
- [ ] Executive summary (1 page)
- [ ] Methodology (2 pages)
- [ ] Findings (5-10 pages)
- [ ] Validation gate checklist

---

## Phase 4: Advanced Analysis (Months 7-12)

### Month 7-8: Machine Learning (Bi-weekly sprints)

#### Sprint 1 (Weeks 27-28): Network Analysis
- [ ] Install NetworkX: `pip install networkx`
- [ ] Build n-gram co-occurrence matrix
- [ ] Apply Louvain community detection
- [ ] Calculate centrality metrics
- [ ] Visualize with Gephi or D3
- [ ] Document: `NETWORK_ANALYSIS_REPORT.md`

#### Sprint 2 (Weeks 29-30): Clustering
- [ ] Feature engineering (entropy vectors, n-gram freqs)
- [ ] K-means clustering (k=3: Classical, Medieval, Modern)
- [ ] Hierarchical clustering dendrogram
- [ ] PCA/t-SNE visualization
- [ ] Random forest classification
- [ ] Validate: ≥85% accuracy
- [ ] Document: `CLUSTERING_REPORT.md`

#### Sprint 3 (Weeks 31-32): Topic Modeling
- [ ] Expand corpus to full books
- [ ] Install gensim: `pip install gensim`
- [ ] Implement LDA (10-15 topics)
- [ ] Interpret topics (homecoming, transformation, etc.)
- [ ] Compare distributions across works
- [ ] Document: `TOPIC_MODELING_REPORT.md`

### Month 9-10: Temporal Analysis (Bi-weekly)

#### Sprint 4 (Weeks 33-36): Entropy Evolution
- [ ] Divide works into 100-line sections
- [ ] Track entropy: opening → middle → conclusion
- [ ] Plot entropy curves
- [ ] Test hypothesis: Openings have higher entropy
- [ ] Statistical validation (t-tests)
- [ ] Document: `TEMPORAL_EVOLUTION_REPORT.md`

#### Sprint 5 (Weeks 37-38): Markov Chains
- [ ] Build trigram Markov chains per work
- [ ] Generate synthetic text
- [ ] Compare synthetic vs. original entropy
- [ ] Calculate perplexity scores
- [ ] Validate: Homer shows lower perplexity (more formulaic)
- [ ] Document: `MARKOV_ANALYSIS_REPORT.md`

#### Sprint 6 (Weeks 39-40): Recurrence Analysis
- [ ] Install recurrence analysis library
- [ ] Generate recurrence plots per work
- [ ] Calculate RQA metrics
- [ ] Compare recurrence rates
- [ ] Validate: Joyce shows highest (circular structure)
- [ ] Document: `RECURRENCE_ANALYSIS_REPORT.md`

### Month 11-12: Validation (Bi-weekly)

#### Sprint 7 (Weeks 41-44): Cross-Linguistic
- [ ] Obtain Greek Odyssey, Latin Aeneid texts
- [ ] Atomize originals
- [ ] Compare with translations
- [ ] Calculate entropy deltas
- [ ] Test: Translation impact ≤10% deviation
- [ ] Document: `CROSS_LINGUISTIC_REPORT.md`

#### Sprint 8 (Weeks 45-48): Framework Testing
- [ ] Collect 3 new works (Milton, Sumerian epics, etc.)
- [ ] Apply Phase 3 frameworks
- [ ] Predict entropy, diversity, compression
- [ ] Calculate prediction error
- [ ] Validate: Error ≤15%
- [ ] Refine frameworks
- [ ] Document: `FRAMEWORK_VALIDATION_REPORT.md`

#### Sprint 9 (Weeks 49-52): Meta-Analysis
- [ ] Compile 200+ atomization runs
- [ ] Statistical meta-analysis
- [ ] Hypothesis testing (all research questions)
- [ ] Effect size calculations
- [ ] Visualization suite (20+ plots)
- [ ] Prepare dataset for Zenodo
- [ ] Document: `COMPREHENSIVE_META_ANALYSIS_REPORT.md`

---

## Phase 5: Publication (Months 12-18)

### Month 12-13: Manuscript Writing (4-week cycles)

#### Weeks 53-56: Paper 1
- [ ] Week 53: Draft introduction + methodology
- [ ] Week 54: Draft results + discussion
- [ ] Week 55: Revisions + figure preparation
- [ ] Week 56: Submit to journal (DSH or LLC)
- [ ] Create supplementary materials (Zenodo link, GitHub repo)

#### Weeks 57-60: Paper 2 (AI-assisted scholarship)
- [ ] (Repeat structure)

### Month 14-15: Conference Prep (4-week cycles)

#### Weeks 61-64: DH Conference
- [ ] Week 61: Draft abstract (300 words)
- [ ] Week 62: Submit abstract
- [ ] Week 63: Design poster (if accepted)
- [ ] Week 64: Prepare lightning talk (5 min)
- [ ] Create interactive demo

#### Weeks 65-68: ACL/NAACL
- [ ] Week 65: Draft extended abstract (4 pages)
- [ ] Week 66: Submit
- [ ] Week 67: Prepare slides (15-20)
- [ ] Week 68: Rehearse talk

### Month 16-17: Open Data Release

#### Weeks 69-72: GitHub Enhancement
- [ ] Clean all code
- [ ] Write comprehensive README
- [ ] Add badges (tests, docs, license)
- [ ] Create CITATION.cff
- [ ] Add example workflows (3-5 Jupyter notebooks)
- [ ] Document API (Sphinx autodoc)
- [ ] Create Docker container
- [ ] Set up GitHub Actions CI
- [ ] Create GitHub Pages site

#### Weeks 73-74: Zenodo Dataset
- [ ] Prepare complete dataset (JSON + CSV)
- [ ] Write data dictionary
- [ ] Create README for dataset
- [ ] Upload to Zenodo
- [ ] Obtain DOI
- [ ] Link from GitHub
- [ ] Announce on Twitter, mailing lists

#### Weeks 75-76: Documentation Website
- [ ] Set up Sphinx docs
- [ ] Configure Read the Docs
- [ ] Write getting started guide
- [ ] Document all modules (API reference)
- [ ] Add tutorial notebooks
- [ ] Create FAQ
- [ ] Publish at readthedocs.io

### Month 18: Community Building

#### Weeks 77-80: Workshop
- [ ] Week 77: Design workshop curriculum
- [ ] Week 78: Create materials (slides, notebooks, datasets)
- [ ] Week 79: Advertise (Twitter, mailing lists, DHNow)
- [ ] Week 80: Conduct workshop (half-day online)
- [ ] Create Slack channel for ongoing support

---

## Continuous Tasks (All Phases)

### Weekly
- [ ] Update `RESEARCH_LOG.md` (5 min/day × 7)
- [ ] Backup data to cloud (Google Drive, Dropbox)
- [ ] Commit to git: `git add . && git commit -m "Week XX updates"`
- [ ] Review progress vs. roadmap

### Monthly
- [ ] Review lifecycle roadmap
- [ ] Update milestones tracking
- [ ] Assess validation gate criteria
- [ ] Adjust timeline if needed
- [ ] Document lessons learned

### Quarterly
- [ ] Comprehensive progress review (1-2 hours)
- [ ] Update `LIFECYCLE_ROADMAP.md` if needed
- [ ] Share progress with advisors/collaborators
- [ ] Plan next quarter's priorities
- [ ] Celebrate milestones achieved!

---

**Document Version**: 1.0
**Last Updated**: 2025-11-18
**Status**: Living checklist (update as phases complete)
