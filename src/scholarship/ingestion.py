"""
AI Scholarship Ingestion

Structured ingestion and storage of AI-generated research outputs.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum


class AISource(Enum):
    """Supported AI platforms for scholarship generation."""
    PERPLEXITY = "perplexity"
    CLAUDE = "claude"
    GPT = "gpt"
    GROK = "grok"
    OTHER = "other"


class ScholarshipIngester:
    """
    Ingest and organize AI-generated scholarship.

    Supports multi-platform research workflows with structured metadata,
    citation tracking, and thematic organization.
    """

    def __init__(self, base_dir: Path):
        """
        Initialize ingester with base directory.

        Args:
            base_dir: Base directory for scholarship storage
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories for each AI source
        for source in AISource:
            (self.base_dir / source.value).mkdir(exist_ok=True)

    def ingest_research(self,
                       content: str,
                       source: AISource,
                       query: str,
                       title: Optional[str] = None,
                       citations: Optional[List[Dict[str, str]]] = None,
                       tags: Optional[List[str]] = None,
                       metadata: Optional[Dict[str, Any]] = None) -> Path:
        """
        Ingest AI-generated research output.

        Args:
            content: Research content (markdown-formatted)
            source: AI platform source
            query: Original query/prompt
            title: Optional title for the research
            citations: Optional list of citation dictionaries
            tags: Optional thematic tags
            metadata: Optional additional metadata

        Returns:
            Path to saved research file
        """
        timestamp = datetime.now()
        date_str = timestamp.strftime('%Y-%m-%d')
        time_str = timestamp.strftime('%H%M%S')

        # Generate filename
        title_slug = self._slugify(title or query)
        filename = f"{date_str}_{time_str}_{title_slug}.md"

        # Construct research document
        doc_lines = [
            f"# {title or query}",
            f"\n**Source:** {source.value.title()}",
            f"**Date:** {timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
            f"\n## Query\n\n{query}",
            f"\n## Research Output\n\n{content}"
        ]

        # Add citations if provided
        if citations:
            doc_lines.append("\n## Citations\n")
            for i, citation in enumerate(citations, 1):
                title_cite = citation.get('title', 'Untitled')
                url = citation.get('url', '')
                author = citation.get('author', '')

                if author:
                    doc_lines.append(f"{i}. {author}. *{title_cite}*. {url}")
                else:
                    doc_lines.append(f"{i}. *{title_cite}*. {url}")

        # Add tags
        if tags:
            doc_lines.append(f"\n## Tags\n\n{', '.join(tags)}")

        # Save markdown file
        output_path = self.base_dir / source.value / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(doc_lines))

        # Save metadata JSON
        meta_path = output_path.with_suffix('.json')
        meta = {
            'title': title or query,
            'source': source.value,
            'query': query,
            'timestamp': timestamp.isoformat(),
            'tags': tags or [],
            'citations': citations or [],
            'file': filename,
            **(metadata or {})
        }

        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta, f, indent=2)

        return output_path

    def ingest_batch(self, research_items: List[Dict[str, Any]]) -> List[Path]:
        """
        Ingest multiple research outputs at once.

        Args:
            research_items: List of research dictionaries (same format as ingest_research kwargs)

        Returns:
            List of paths to saved research files
        """
        paths = []

        for item in research_items:
            # Extract source, converting string to enum if needed
            source = item.get('source')
            if isinstance(source, str):
                source = AISource(source)

            path = self.ingest_research(
                content=item.get('content', ''),
                source=source,
                query=item.get('query', ''),
                title=item.get('title'),
                citations=item.get('citations'),
                tags=item.get('tags'),
                metadata=item.get('metadata')
            )
            paths.append(path)

        return paths

    def create_index(self, output_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Create searchable index of all ingested research.

        Args:
            output_path: Optional path to save index JSON

        Returns:
            Index dictionary
        """
        index = {
            'generated': datetime.now().isoformat(),
            'total_items': 0,
            'by_source': {},
            'by_tag': {},
            'items': []
        }

        # Scan all metadata files
        for source_dir in self.base_dir.iterdir():
            if not source_dir.is_dir():
                continue

            source_name = source_dir.name
            index['by_source'][source_name] = []

            for meta_file in source_dir.glob('*.json'):
                with open(meta_file, 'r', encoding='utf-8') as f:
                    meta = json.load(f)

                index['items'].append(meta)
                index['by_source'][source_name].append(meta['file'])

                # Index by tags
                for tag in meta.get('tags', []):
                    if tag not in index['by_tag']:
                        index['by_tag'][tag] = []
                    index['by_tag'][tag].append(meta['file'])

                index['total_items'] += 1

        # Save index if path provided
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(index, f, indent=2)

        return index

    @staticmethod
    def _slugify(text: str, max_length: int = 50) -> str:
        """Convert text to filename-safe slug."""
        import re

        # Convert to lowercase and replace spaces/special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-')

        return slug[:max_length]
