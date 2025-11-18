"""
Entropy Analysis for Text Complexity

Implements information-theoretic measurements for literary text analysis.
"""

import math
from collections import Counter
from typing import List
import zlib


class EntropyAnalyzer:
    """Analyze text entropy and complexity metrics."""

    def __init__(self, text: str):
        """
        Initialize analyzer with source text.

        Args:
            text: Source text to analyze
        """
        self.text = text
        self.words = text.lower().split()
        self.chars = list(text.lower())

    def shannon_entropy(self, unit: str = 'words') -> float:
        """
        Calculate Shannon entropy.

        Measures the average information content per unit (character or word).
        Higher entropy indicates more unpredictability/complexity.

        Args:
            unit: 'words' or 'chars' for analysis unit

        Returns:
            Shannon entropy in bits
        """
        if unit == 'words':
            elements = self.words
        elif unit == 'chars':
            elements = self.chars
        else:
            raise ValueError("unit must be 'words' or 'chars'")

        if not elements:
            return 0.0

        # Count frequencies
        counter = Counter(elements)
        total = len(elements)

        # Calculate entropy: H = -Σ p(x) log₂ p(x)
        entropy = 0.0
        for count in counter.values():
            probability = count / total
            entropy -= probability * math.log2(probability)

        return entropy

    def normalized_entropy(self, unit: str = 'words') -> float:
        """
        Calculate normalized entropy (0-1).

        Normalizes Shannon entropy by the maximum possible entropy
        for the given vocabulary size.

        Args:
            unit: 'words' or 'chars' for analysis unit

        Returns:
            Normalized entropy between 0 and 1
        """
        entropy = self.shannon_entropy(unit)

        if unit == 'words':
            vocab_size = len(set(self.words))
        else:
            vocab_size = len(set(self.chars))

        if vocab_size <= 1:
            return 0.0

        max_entropy = math.log2(vocab_size)
        return entropy / max_entropy if max_entropy > 0 else 0.0

    def compression_ratio(self) -> float:
        """
        Calculate compression ratio using zlib.

        Measures text compressibility as a proxy for redundancy/predictability.
        Lower ratios indicate more repetitive/predictable text.

        Returns:
            Ratio of compressed size to original size (0-1)
        """
        if not self.text:
            return 0.0

        original_bytes = self.text.encode('utf-8')
        compressed_bytes = zlib.compress(original_bytes)

        return len(compressed_bytes) / len(original_bytes)

    def lexical_diversity(self) -> float:
        """
        Calculate type-token ratio (lexical diversity).

        Measures vocabulary richness as the ratio of unique words to total words.

        Returns:
            Lexical diversity ratio (0-1)
        """
        if not self.words:
            return 0.0

        unique_words = len(set(self.words))
        total_words = len(self.words)

        return unique_words / total_words

    def word_entropy_distribution(self, top_n: int = 20) -> List[tuple]:
        """
        Calculate per-word contribution to entropy.

        Args:
            top_n: Number of top words to return

        Returns:
            List of (word, entropy_contribution) tuples
        """
        if not self.words:
            return []

        counter = Counter(self.words)
        total = len(self.words)

        word_entropies = []
        for word, count in counter.items():
            probability = count / total
            contribution = -probability * math.log2(probability)
            word_entropies.append((word, contribution))

        # Sort by entropy contribution (descending)
        word_entropies.sort(key=lambda x: x[1], reverse=True)
        return word_entropies[:top_n]
