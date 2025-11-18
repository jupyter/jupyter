#!/usr/bin/env python3
"""
Batch Atomization Script for Epic Literary Corpus

Processes all texts in data/raw/corpora/ through the atomization pipeline,
generating comparative analysis data for cross-work synthesis.

Usage:
    python scripts/batch_atomize_corpora.py
    python scripts/batch_atomize_corpora.py --works homer_odyssey virgil_aeneid
    python scripts/batch_atomize_corpora.py --ngram-max 5 --top-n 30
"""

import sys
from pathlib import Path
import json
import argparse
from datetime import datetime

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / 'src'))

from atomization import TextAtomizer


def load_corpus_index(corpora_dir: Path) -> dict:
    """Load corpus index file."""
    index_path = corpora_dir / 'CORPUS_INDEX.json'
    if not index_path.exists():
        raise FileNotFoundError(f"Corpus index not found: {index_path}")

    with open(index_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_metadata(metadata_path: Path) -> dict:
    """Load work metadata file."""
    if not metadata_path.exists():
        return {}

    with open(metadata_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def atomize_work(text_path: Path,
                 metadata_path: Path,
                 work_id: str,
                 ngram_max: int = 3,
                 top_n: int = 20) -> dict:
    """
    Atomize a single literary work.

    Args:
        text_path: Path to text file
        metadata_path: Path to metadata JSON
        work_id: Work identifier
        ngram_max: Maximum n-gram size
        top_n: Number of top n-grams to extract

    Returns:
        Atomization results dictionary
    """
    # Load text
    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Load metadata
    metadata = load_metadata(metadata_path)

    # Initialize atomizer
    atomizer = TextAtomizer(
        text=text,
        title=metadata.get('title', work_id),
        metadata={
            'work_id': work_id,
            'author': metadata.get('author'),
            'tradition': metadata.get('tradition'),
            'period': metadata.get('period'),
            'genre': metadata.get('genre'),
            'language': metadata.get('language'),
            **metadata
        }
    )

    # Execute atomization
    results = atomizer.atomize(
        ngram_range=(1, ngram_max),
        top_n=top_n,
        calculate_entropy=True,
        map_glyphs=True
    )

    return results, atomizer


def main():
    parser = argparse.ArgumentParser(
        description='Batch atomization of epic literary corpus'
    )
    parser.add_argument(
        '--works',
        nargs='*',
        help='Specific work IDs to process (default: all)'
    )
    parser.add_argument(
        '--ngram-max',
        type=int,
        default=3,
        help='Maximum n-gram size (default: 3)'
    )
    parser.add_argument(
        '--top-n',
        type=int,
        default=20,
        help='Number of top n-grams to extract (default: 20)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=None,
        help='Output directory (default: data/processed/atomization/batch/)'
    )

    args = parser.parse_args()

    # Set paths
    corpora_dir = project_root / 'data' / 'raw' / 'corpora'
    output_dir = args.output_dir or (project_root / 'data' / 'processed' / 'atomization' / 'batch')
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load corpus index
    print("=" * 70)
    print("BATCH ATOMIZATION: Epic Literary Corpus")
    print("=" * 70)

    corpus_index = load_corpus_index(corpora_dir)
    works = corpus_index['works']

    # Filter works if specified
    if args.works:
        works = [w for w in works if w['id'] in args.works]
        print(f"\nProcessing {len(works)} specified works: {args.works}")
    else:
        print(f"\nProcessing all {len(works)} works in corpus")

    # Process each work
    results_collection = []

    for work in works:
        work_id = work['id']
        text_path = corpora_dir / work['file']
        metadata_path = corpora_dir / work['metadata']

        print(f"\n{'─' * 70}")
        print(f"Processing: {work_id}")
        print(f"  File: {work['file']}")
        print(f"  Tradition: {work['tradition']} ({work['period']})")

        try:
            # Atomize
            results, atomizer = atomize_work(
                text_path,
                metadata_path,
                work_id,
                ngram_max=args.ngram_max,
                top_n=args.top_n
            )

            # Display key metrics
            print(f"  Words: {results['metadata']['word_count']}")
            print(f"  Shannon Entropy: {results['entropy']['shannon_entropy']:.4f} bits")
            print(f"  Lexical Diversity: {results['entropy']['lexical_diversity']:.4f}")
            print(f"  Compression Ratio: {results['entropy']['compression_ratio']:.4f}")

            # Show top trigram
            if results['ngrams'][f'{args.ngram_max}-grams']:
                top_ngram = results['ngrams'][f'{args.ngram_max}-grams'][0]
                print(f"  Top {args.ngram_max}-gram: '{top_ngram['text']}' ({top_ngram['frequency']}x)")

            # Export individual results
            work_output_dir = output_dir / work_id
            work_output_dir.mkdir(exist_ok=True)

            atomizer.export_markdown(work_output_dir / f"{work_id}.md")
            atomizer.export_json(work_output_dir / f"{work_id}.json")

            # Collect for comparative analysis
            results_collection.append({
                'work_id': work_id,
                'tradition': work['tradition'],
                'period': work['period'],
                'genre': work['genre'],
                'results': results
            })

            print(f"  ✓ Exported to {work_output_dir}")

        except Exception as e:
            print(f"  ✗ Error processing {work_id}: {e}")
            continue

    # Generate comparative summary
    print(f"\n{'=' * 70}")
    print("COMPARATIVE SUMMARY")
    print("=" * 70)

    summary_path = output_dir / 'comparative_summary.json'
    summary = {
        'generated': datetime.now().isoformat(),
        'total_works': len(results_collection),
        'parameters': {
            'ngram_max': args.ngram_max,
            'top_n': args.top_n
        },
        'works': []
    }

    # Entropy comparison
    print("\nEntropy Rankings (Shannon):")
    entropy_sorted = sorted(
        results_collection,
        key=lambda x: x['results']['entropy']['shannon_entropy'],
        reverse=True
    )

    for i, item in enumerate(entropy_sorted, 1):
        entropy = item['results']['entropy']['shannon_entropy']
        print(f"  {i}. {item['work_id']:25} → {entropy:.4f} bits ({item['tradition']})")

        summary['works'].append({
            'work_id': item['work_id'],
            'tradition': item['tradition'],
            'period': item['period'],
            'entropy': entropy,
            'lexical_diversity': item['results']['entropy']['lexical_diversity'],
            'compression_ratio': item['results']['entropy']['compression_ratio'],
            'word_count': item['results']['metadata']['word_count']
        })

    # Save summary
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Comparative summary: {summary_path}")

    # Generate Markdown report
    report_path = output_dir / 'BATCH_REPORT.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Batch Atomization Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Works Processed**: {len(results_collection)}\n\n")

        f.write("## Entropy Rankings\n\n")
        for i, item in enumerate(entropy_sorted, 1):
            ent = item['results']['entropy']
            f.write(f"### {i}. {item['work_id']}\n\n")
            f.write(f"- **Tradition**: {item['tradition']} ({item['period']})\n")
            f.write(f"- **Shannon Entropy**: {ent['shannon_entropy']:.4f} bits\n")
            f.write(f"- **Lexical Diversity**: {ent['lexical_diversity']:.4f}\n")
            f.write(f"- **Compression Ratio**: {ent['compression_ratio']:.4f}\n\n")

    print(f"✓ Markdown report: {report_path}")

    print(f"\n{'=' * 70}")
    print(f"✓ Batch atomization complete. Processed {len(results_collection)} works.")
    print(f"  Output directory: {output_dir}")
    print("=" * 70)


if __name__ == '__main__':
    main()
