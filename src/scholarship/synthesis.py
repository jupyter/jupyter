"""
Scholarship Synthesis

Cross-platform synthesis and thematic analysis of AI-generated research.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from collections import defaultdict
from datetime import datetime


class ScholarshipSynthesizer:
    """
    Synthesize and analyze multi-platform research outputs.

    Identifies patterns, contradictions, and emergent themes across
    AI-generated scholarship from different platforms.
    """

    def __init__(self, scholarship_dir: Path):
        """
        Initialize synthesizer with scholarship directory.

        Args:
            scholarship_dir: Directory containing ingested research
        """
        self.scholarship_dir = Path(scholarship_dir)
        self.research_items = []
        self._load_research()

    def _load_research(self) -> None:
        """Load all research metadata from scholarship directory."""
        self.research_items = []

        for meta_file in self.scholarship_dir.rglob('*.json'):
            with open(meta_file, 'r', encoding='utf-8') as f:
                meta = json.load(f)

            # Load corresponding markdown content
            md_file = meta_file.with_suffix('.md')
            if md_file.exists():
                with open(md_file, 'r', encoding='utf-8') as f:
                    meta['content'] = f.read()

            self.research_items.append(meta)

    def analyze_by_theme(self, tags: Optional[List[str]] = None) -> Dict[str, List[Dict]]:
        """
        Group research by thematic tags.

        Args:
            tags: Optional list of specific tags to analyze (None = all tags)

        Returns:
            Dictionary mapping tags to research items
        """
        theme_map = defaultdict(list)

        for item in self.research_items:
            item_tags = item.get('tags', [])

            if tags:
                # Filter to specified tags
                relevant_tags = [t for t in item_tags if t in tags]
            else:
                relevant_tags = item_tags

            for tag in relevant_tags:
                theme_map[tag].append({
                    'title': item.get('title'),
                    'source': item.get('source'),
                    'timestamp': item.get('timestamp'),
                    'file': item.get('file')
                })

        return dict(theme_map)

    def compare_sources(self, query_keywords: List[str]) -> Dict[str, List[Dict]]:
        """
        Compare how different AI platforms addressed similar queries.

        Args:
            query_keywords: Keywords to match in queries

        Returns:
            Dictionary mapping sources to matching research items
        """
        source_map = defaultdict(list)

        for item in self.research_items:
            query = item.get('query', '').lower()

            # Check if any keyword appears in query
            if any(kw.lower() in query for kw in query_keywords):
                source = item.get('source')
                source_map[source].append({
                    'title': item.get('title'),
                    'query': item.get('query'),
                    'timestamp': item.get('timestamp'),
                    'file': item.get('file'),
                    'preview': item.get('content', '')[:200] + '...'
                })

        return dict(source_map)

    def extract_citations(self, min_frequency: int = 2) -> List[Dict[str, Any]]:
        """
        Extract frequently cited sources across research.

        Args:
            min_frequency: Minimum citation count to include

        Returns:
            List of citation dictionaries with frequency counts
        """
        citation_counts = defaultdict(int)
        citation_details = {}

        for item in self.research_items:
            for citation in item.get('citations', []):
                url = citation.get('url', '')
                if url:
                    citation_counts[url] += 1
                    if url not in citation_details:
                        citation_details[url] = citation

        # Filter by frequency and format results
        frequent_citations = []
        for url, count in citation_counts.items():
            if count >= min_frequency:
                citation = citation_details[url]
                frequent_citations.append({
                    **citation,
                    'frequency': count
                })

        # Sort by frequency
        frequent_citations.sort(key=lambda x: x['frequency'], reverse=True)
        return frequent_citations

    def generate_synthesis_report(self, output_path: Optional[Path] = None) -> str:
        """
        Generate comprehensive synthesis report.

        Args:
            output_path: Optional path to save report

        Returns:
            Formatted markdown report
        """
        report_lines = [
            "# AI Scholarship Synthesis Report",
            f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total Research Items:** {len(self.research_items)}",
        ]

        # Summary by source
        source_counts = defaultdict(int)
        for item in self.research_items:
            source_counts[item.get('source')] += 1

        report_lines.append("\n## Research by Source\n")
        for source, count in sorted(source_counts.items()):
            report_lines.append(f"- **{source.title()}:** {count} items")

        # Summary by tag
        tag_counts = defaultdict(int)
        for item in self.research_items:
            for tag in item.get('tags', []):
                tag_counts[tag] += 1

        if tag_counts:
            report_lines.append("\n## Research by Theme\n")
            for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True):
                report_lines.append(f"- **{tag}:** {count} items")

        # Frequent citations
        frequent_cites = self.extract_citations(min_frequency=2)
        if frequent_cites:
            report_lines.append("\n## Frequently Cited Sources\n")
            for cite in frequent_cites[:10]:
                title = cite.get('title', 'Untitled')
                url = cite.get('url', '')
                freq = cite.get('frequency', 0)
                report_lines.append(f"- [{title}]({url}) — cited {freq} times")

        # Recent research
        sorted_items = sorted(self.research_items,
                             key=lambda x: x.get('timestamp', ''),
                             reverse=True)

        report_lines.append("\n## Recent Research (Last 10)\n")
        for item in sorted_items[:10]:
            title = item.get('title', 'Untitled')
            source = item.get('source', 'unknown')
            timestamp = item.get('timestamp', '')[:10]  # Date only
            report_lines.append(f"- **{title}** ({source.title()}, {timestamp})")

        report = '\n'.join(report_lines)

        # Save if path provided
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)

        return report

    def export_for_jupyter(self, output_path: Path) -> None:
        """
        Export research data in Jupyter-friendly format.

        Creates JSON structure optimized for notebook analysis.

        Args:
            output_path: Path to save JSON export
        """
        export_data = {
            'metadata': {
                'generated': datetime.now().isoformat(),
                'total_items': len(self.research_items),
                'sources': list(set(item.get('source') for item in self.research_items)),
            },
            'research': self.research_items
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
