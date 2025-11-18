"""
Core Text Atomization Engine

Implements recursive text decomposition methodology for literary-computational analysis.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from collections import Counter

from .ngrams import NGramExtractor
from .entropy import EntropyAnalyzer
from .glyphs import GlyphFusionMapper


class TextAtomizer:
    """
    Primary atomization engine for recursive text analysis.

    Processes literary texts through multiple analytical lenses:
    - Lexical decomposition (n-grams)
    - Information-theoretic measurement (entropy)
    - Symbolic mapping (glyph fusion)

    Supports iterative refinement through daily runs and comparative analysis.
    """

    def __init__(self, text: str, title: str = "Untitled", metadata: Optional[Dict[str, Any]] = None):
        """
        Initialize atomizer with source text.

        Args:
            text: Source text to analyze
            title: Title/identifier for the text
            metadata: Optional metadata (author, source, date, etc.)
        """
        self.text = text
        self.title = title
        self.metadata = metadata or {}
        self.timestamp = datetime.now()

        # Initialize analyzers
        self.ngram_extractor = NGramExtractor(text)
        self.entropy_analyzer = EntropyAnalyzer(text)
        self.glyph_mapper = GlyphFusionMapper()

        # Storage for analysis results
        self.results = {}

    def atomize(self,
                ngram_range: tuple = (1, 3),
                top_n: int = 20,
                calculate_entropy: bool = True,
                map_glyphs: bool = True) -> Dict[str, Any]:
        """
        Execute full atomization pipeline.

        Args:
            ngram_range: Tuple of (min_n, max_n) for n-gram extraction
            top_n: Number of top n-grams to extract per size
            calculate_entropy: Whether to calculate entropy metrics
            map_glyphs: Whether to generate glyph fusion mappings

        Returns:
            Dictionary containing all analysis results
        """
        results = {
            'metadata': {
                'title': self.title,
                'timestamp': self.timestamp.isoformat(),
                'text_length': len(self.text),
                'word_count': len(self.text.split()),
                **self.metadata
            }
        }

        # N-gram analysis
        results['ngrams'] = {}
        for n in range(ngram_range[0], ngram_range[1] + 1):
            ngrams = self.ngram_extractor.extract_ngrams(n, top_n=top_n)
            results['ngrams'][f'{n}-grams'] = [
                {'text': ng, 'frequency': freq}
                for ng, freq in ngrams
            ]

        # Entropy analysis
        if calculate_entropy:
            results['entropy'] = {
                'shannon_entropy': self.entropy_analyzer.shannon_entropy(),
                'normalized_entropy': self.entropy_analyzer.normalized_entropy(),
                'compression_ratio': self.entropy_analyzer.compression_ratio(),
                'lexical_diversity': self.entropy_analyzer.lexical_diversity()
            }

        # Glyph fusion mapping
        if map_glyphs:
            # Extract significant patterns for glyph mapping
            top_bigrams = [bg[0] for bg in self.ngram_extractor.extract_ngrams(2, top_n=10)]
            results['glyph_fusions'] = self.glyph_mapper.create_fusion_map(top_bigrams)

        self.results = results
        return results

    def export_json(self, output_path: Path) -> None:
        """Export atomization results to JSON."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

    def export_markdown(self, output_path: Path) -> None:
        """Export atomization results to Markdown format."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        md_lines = [
            f"# Text Atomization: {self.title}",
            f"\n**Date:** {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
            f"\n## Metadata",
            f"- **Text Length:** {self.results['metadata']['text_length']} characters",
            f"- **Word Count:** {self.results['metadata']['word_count']} words",
        ]

        # Add custom metadata
        for key, value in self.metadata.items():
            md_lines.append(f"- **{key.title()}:** {value}")

        # N-grams section
        if 'ngrams' in self.results:
            md_lines.append("\n## N-gram Analysis\n")
            for ngram_type, ngrams in self.results['ngrams'].items():
                md_lines.append(f"### Top {ngram_type}")
                for item in ngrams[:10]:  # Top 10 for readability
                    md_lines.append(f"- `{item['text']}` — frequency: {item['frequency']}")
                md_lines.append("")

        # Entropy section
        if 'entropy' in self.results:
            md_lines.append("## Entropy Metrics\n")
            for metric, value in self.results['entropy'].items():
                md_lines.append(f"- **{metric.replace('_', ' ').title()}:** {value:.4f}")

        # Glyph fusions
        if 'glyph_fusions' in self.results:
            md_lines.append("\n## Glyph Fusion Mappings\n")
            for fusion in self.results['glyph_fusions'][:10]:
                md_lines.append(f"- `{fusion['pattern']}` → `{fusion['glyph']}` ({fusion['type']})")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_lines))

    def export_daily_output(self, base_dir: Path, date: Optional[datetime] = None) -> tuple:
        """
        Export to daily Markdown + JSON archive (primary layer format).

        Args:
            base_dir: Base directory for outputs
            date: Date for the output (defaults to atomizer timestamp)

        Returns:
            Tuple of (markdown_path, json_path)
        """
        date = date or self.timestamp
        date_str = date.strftime('%Y-%m-%d')

        # Daily markdown
        md_path = base_dir / f"output_{date_str}.md"
        self.export_markdown(md_path)

        # Consolidated JSON archive
        json_path = base_dir / "all_outputs.json"

        # Append to existing archive or create new
        archive = []
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                archive = json.load(f)

        archive.append({
            'date': date_str,
            **self.results
        })

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(archive, f, indent=2, ensure_ascii=False)

        return md_path, json_path
