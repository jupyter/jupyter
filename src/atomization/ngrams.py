"""
N-gram Extraction and Analysis

Implements n-gram frequency analysis for recursive pattern detection in literary texts.
"""

from collections import Counter
from typing import List, Tuple
import re


class NGramExtractor:
    """Extract and analyze n-grams from text."""

    def __init__(self, text: str):
        """
        Initialize extractor with source text.

        Args:
            text: Source text to analyze
        """
        self.text = text
        self.words = self._tokenize(text)

    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into words.

        Uses simple whitespace splitting with punctuation handling.
        Preserves contractions and hyphenated words.
        """
        # Basic tokenization - can be enhanced with NLTK if needed
        tokens = re.findall(r"\b[\w']+\b|\S", text.lower())
        return tokens

    def extract_ngrams(self, n: int, top_n: int = 20) -> List[Tuple[str, int]]:
        """
        Extract n-grams of specified size.

        Args:
            n: Size of n-grams (1=unigrams, 2=bigrams, 3=trigrams, etc.)
            top_n: Number of top n-grams to return

        Returns:
            List of (ngram, frequency) tuples, sorted by frequency descending
        """
        if n < 1:
            raise ValueError("n must be >= 1")

        if len(self.words) < n:
            return []

        ngrams = []
        for i in range(len(self.words) - n + 1):
            ngram = ' '.join(self.words[i:i+n])
            ngrams.append(ngram)

        counter = Counter(ngrams)
        return counter.most_common(top_n)

    def extract_all_ngrams(self, min_n: int = 1, max_n: int = 3, top_n: int = 20) -> dict:
        """
        Extract multiple n-gram sizes at once.

        Args:
            min_n: Minimum n-gram size
            max_n: Maximum n-gram size
            top_n: Number of top n-grams per size

        Returns:
            Dictionary mapping n-gram size to list of (ngram, frequency) tuples
        """
        results = {}
        for n in range(min_n, max_n + 1):
            results[n] = self.extract_ngrams(n, top_n)
        return results

    def get_ngram_diversity(self, n: int) -> float:
        """
        Calculate diversity ratio for n-grams.

        Returns:
            Ratio of unique n-grams to total n-grams (0-1)
        """
        if len(self.words) < n:
            return 0.0

        total_ngrams = len(self.words) - n + 1
        ngrams = [' '.join(self.words[i:i+n]) for i in range(total_ngrams)]
        unique_ngrams = len(set(ngrams))

        return unique_ngrams / total_ngrams if total_ngrams > 0 else 0.0
