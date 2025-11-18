"""
Unit tests for text atomization modules.
"""

import pytest
from pathlib import Path
import json
import tempfile

from src.atomization import (
    TextAtomizer,
    NGramExtractor,
    EntropyAnalyzer,
    GlyphFusionMapper
)


# Sample text for testing
SAMPLE_TEXT = """
Sing to me of the man, Muse, the man of twists and turns
driven time and again off course, once he had plundered
the hallowed heights of Troy. Many cities of men he saw and learned their minds,
many pains he suffered, heartsick on the open sea.
"""


class TestNGramExtractor:
    """Test n-gram extraction functionality."""

    def test_extract_unigrams(self):
        extractor = NGramExtractor(SAMPLE_TEXT)
        unigrams = extractor.extract_ngrams(n=1, top_n=5)

        assert len(unigrams) <= 5
        assert all(isinstance(item, tuple) for item in unigrams)
        assert all(len(item) == 2 for item in unigrams)  # (ngram, frequency)

        # Most common word should be frequent
        top_word, freq = unigrams[0]
        assert freq >= 2

    def test_extract_bigrams(self):
        extractor = NGramExtractor(SAMPLE_TEXT)
        bigrams = extractor.extract_ngrams(n=2, top_n=10)

        assert len(bigrams) <= 10
        # Bigrams should have spaces
        assert all(' ' in bg[0] for bg in bigrams)

    def test_extract_trigrams(self):
        extractor = NGramExtractor(SAMPLE_TEXT)
        trigrams = extractor.extract_ngrams(n=3, top_n=10)

        assert len(trigrams) <= 10
        # Trigrams should have 2 spaces (3 words)
        assert all(tg[0].count(' ') == 2 for tg in trigrams)

    def test_ngram_diversity(self):
        extractor = NGramExtractor(SAMPLE_TEXT)
        diversity = extractor.get_ngram_diversity(n=2)

        assert 0.0 <= diversity <= 1.0

    def test_empty_text(self):
        extractor = NGramExtractor("")
        ngrams = extractor.extract_ngrams(n=1)

        assert len(ngrams) == 0


class TestEntropyAnalyzer:
    """Test entropy analysis functionality."""

    def test_shannon_entropy_words(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        entropy = analyzer.shannon_entropy(unit='words')

        assert entropy > 0
        assert isinstance(entropy, float)

    def test_shannon_entropy_chars(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        entropy = analyzer.shannon_entropy(unit='chars')

        assert entropy > 0
        assert isinstance(entropy, float)

    def test_normalized_entropy(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        normalized = analyzer.normalized_entropy(unit='words')

        assert 0.0 <= normalized <= 1.0

    def test_compression_ratio(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        ratio = analyzer.compression_ratio()

        assert 0.0 < ratio < 1.0  # Compressed should be smaller

    def test_lexical_diversity(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        diversity = analyzer.lexical_diversity()

        assert 0.0 < diversity <= 1.0

    def test_word_entropy_distribution(self):
        analyzer = EntropyAnalyzer(SAMPLE_TEXT)
        distribution = analyzer.word_entropy_distribution(top_n=5)

        assert len(distribution) <= 5
        assert all(isinstance(item, tuple) for item in distribution)
        # Should be sorted by entropy contribution
        entropies = [item[1] for item in distribution]
        assert entropies == sorted(entropies, reverse=True)


class TestGlyphFusionMapper:
    """Test glyph fusion mapping functionality."""

    def test_pattern_to_glyph(self):
        mapper = GlyphFusionMapper(glyph_set='geometric')
        glyph = mapper.pattern_to_glyph('wine-dark sea')

        assert isinstance(glyph, str)
        assert glyph in mapper.glyphs

    def test_create_fusion_map(self):
        mapper = GlyphFusionMapper(glyph_set='geometric')
        patterns = ['wine-dark sea', 'rosy-fingered dawn', 'swift-footed Achilles']

        fusions = mapper.create_fusion_map(patterns)

        assert len(fusions) == len(patterns)
        assert all('pattern' in f for f in fusions)
        assert all('glyph' in f for f in fusions)
        assert all('type' in f for f in fusions)

    def test_encode_decode_text(self):
        mapper = GlyphFusionMapper(glyph_set='geometric')
        mapper.create_fusion_map(['the man', 'of the'])

        original = "the man of the city"
        encoded = mapper.encode_text(original)
        decoded = mapper.decode_text(encoded)

        assert encoded != original  # Should be transformed
        assert decoded == original  # Should roundtrip

    def test_invalid_glyph_set(self):
        with pytest.raises(ValueError):
            GlyphFusionMapper(glyph_set='nonexistent')


class TestTextAtomizer:
    """Test main atomization interface."""

    def test_initialization(self):
        atomizer = TextAtomizer(
            text=SAMPLE_TEXT,
            title="Test Text",
            metadata={'author': 'Homer'}
        )

        assert atomizer.text == SAMPLE_TEXT
        assert atomizer.title == "Test Text"
        assert atomizer.metadata['author'] == 'Homer'

    def test_atomize_basic(self):
        atomizer = TextAtomizer(SAMPLE_TEXT, title="Test")
        results = atomizer.atomize(
            ngram_range=(1, 2),
            top_n=10,
            calculate_entropy=True,
            map_glyphs=True
        )

        assert 'metadata' in results
        assert 'ngrams' in results
        assert 'entropy' in results
        assert 'glyph_fusions' in results

        # Check metadata
        assert results['metadata']['title'] == "Test"
        assert results['metadata']['word_count'] > 0

        # Check n-grams
        assert '1-grams' in results['ngrams']
        assert '2-grams' in results['ngrams']

        # Check entropy
        assert 'shannon_entropy' in results['entropy']
        assert 'lexical_diversity' in results['entropy']

    def test_export_json(self):
        atomizer = TextAtomizer(SAMPLE_TEXT, title="Test")
        atomizer.atomize()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / 'test_output.json'
            atomizer.export_json(output_path)

            assert output_path.exists()

            # Verify JSON is valid
            with open(output_path, 'r') as f:
                data = json.load(f)

            assert 'metadata' in data
            assert 'ngrams' in data

    def test_export_markdown(self):
        atomizer = TextAtomizer(SAMPLE_TEXT, title="Test")
        atomizer.atomize()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / 'test_output.md'
            atomizer.export_markdown(output_path)

            assert output_path.exists()

            # Verify markdown contains expected sections
            with open(output_path, 'r') as f:
                content = f.read()

            assert '# Text Atomization: Test' in content
            assert '## Metadata' in content
            assert '## N-gram Analysis' in content

    def test_export_daily_output(self):
        atomizer = TextAtomizer(SAMPLE_TEXT, title="Daily Test")
        atomizer.atomize()

        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir)
            md_path, json_path = atomizer.export_daily_output(base_dir)

            assert md_path.exists()
            assert json_path.exists()

            # Verify archive format
            with open(json_path, 'r') as f:
                archive = json.load(f)

            assert isinstance(archive, list)
            assert len(archive) == 1
            assert 'date' in archive[0]


class TestIntegration:
    """Integration tests for complete workflows."""

    def test_full_atomization_pipeline(self):
        """Test complete atomization workflow."""
        atomizer = TextAtomizer(
            text=SAMPLE_TEXT,
            title="Odyssey Excerpt",
            metadata={'author': 'Homer', 'book': 1}
        )

        results = atomizer.atomize(
            ngram_range=(1, 3),
            top_n=20,
            calculate_entropy=True,
            map_glyphs=True
        )

        # Verify all components
        assert len(results['ngrams']['1-grams']) > 0
        assert len(results['ngrams']['2-grams']) > 0
        assert len(results['ngrams']['3-grams']) > 0

        assert results['entropy']['shannon_entropy'] > 0
        assert 0 < results['entropy']['lexical_diversity'] <= 1

        assert len(results['glyph_fusions']) > 0

        # Export and verify
        with tempfile.TemporaryDirectory() as tmpdir:
            md_path, json_path = atomizer.export_daily_output(Path(tmpdir))

            # Both outputs should exist and be non-empty
            assert md_path.stat().st_size > 0
            assert json_path.stat().st_size > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
