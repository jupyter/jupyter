"""
Glyph Fusion Mapping

Symbolic transformation layer for mapping textual patterns to abstract glyphs.
Supports recursive pattern compression and visual representation.
"""

from typing import List, Dict, Any
import hashlib


class GlyphFusionMapper:
    """
    Create symbolic mappings for text patterns.

    Transforms frequent n-grams and patterns into compact glyph representations,
    enabling visualization and compression of recursive textual structures.
    """

    # Symbolic glyph sets for different pattern types
    GLYPH_SETS = {
        'geometric': ['◯', '△', '□', '◇', '☆', '✦', '✧', '⬡', '⬢', '⬣'],
        'alchemical': ['🜁', '🜂', '🜃', '🜄', '🜅', '🜆', '🜇', '🜈', '🜉', '🜊'],
        'runic': ['ᚠ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚱ', 'ᚲ', 'ᚷ', 'ᚹ', 'ᚺ', 'ᚾ'],
        'astronomical': ['☉', '☽', '☿', '♀', '♂', '♃', '♄', '♅', '♆', '♇'],
        'abstract': ['◐', '◑', '◒', '◓', '◔', '◕', '●', '○', '◎', '◉'],
    }

    def __init__(self, glyph_set: str = 'geometric'):
        """
        Initialize mapper with glyph set.

        Args:
            glyph_set: Name of glyph set to use ('geometric', 'alchemical', etc.)
        """
        if glyph_set not in self.GLYPH_SETS:
            raise ValueError(f"Unknown glyph set: {glyph_set}")

        self.glyph_set = glyph_set
        self.glyphs = self.GLYPH_SETS[glyph_set]
        self.fusion_map = {}

    def pattern_to_glyph(self, pattern: str, index: int = None) -> str:
        """
        Map a text pattern to a glyph.

        Args:
            pattern: Text pattern to map
            index: Optional explicit index into glyph set

        Returns:
            Glyph symbol
        """
        if index is not None:
            return self.glyphs[index % len(self.glyphs)]

        # Use hash of pattern for consistent mapping
        hash_val = int(hashlib.md5(pattern.encode()).hexdigest(), 16)
        return self.glyphs[hash_val % len(self.glyphs)]

    def create_fusion_map(self, patterns: List[str]) -> List[Dict[str, Any]]:
        """
        Create fusion mappings for multiple patterns.

        Args:
            patterns: List of text patterns to map

        Returns:
            List of fusion mapping dictionaries
        """
        fusions = []

        for i, pattern in enumerate(patterns):
            glyph = self.pattern_to_glyph(pattern, index=i)

            fusion = {
                'pattern': pattern,
                'glyph': glyph,
                'type': self.glyph_set,
                'index': i,
                'hash': hashlib.md5(pattern.encode()).hexdigest()[:8]
            }

            fusions.append(fusion)
            self.fusion_map[pattern] = glyph

        return fusions

    def encode_text(self, text: str) -> str:
        """
        Encode text using fusion map.

        Replaces mapped patterns with their glyph representations.

        Args:
            text: Text to encode

        Returns:
            Text with patterns replaced by glyphs
        """
        encoded = text

        # Sort patterns by length (descending) to handle longer matches first
        sorted_patterns = sorted(self.fusion_map.keys(), key=len, reverse=True)

        for pattern in sorted_patterns:
            glyph = self.fusion_map[pattern]
            encoded = encoded.replace(pattern, glyph)

        return encoded

    def decode_text(self, encoded_text: str) -> str:
        """
        Decode glyph-encoded text back to original patterns.

        Args:
            encoded_text: Text with glyph encodings

        Returns:
            Text with glyphs replaced by original patterns
        """
        decoded = encoded_text

        # Reverse mapping
        reverse_map = {v: k for k, v in self.fusion_map.items()}

        for glyph, pattern in reverse_map.items():
            decoded = decoded.replace(glyph, pattern)

        return decoded

    def visualize_fusion_map(self) -> str:
        """
        Create visual representation of fusion map.

        Returns:
            Formatted string showing pattern → glyph mappings
        """
        lines = [f"Glyph Fusion Map ({self.glyph_set}):", "=" * 50]

        for pattern, glyph in self.fusion_map.items():
            lines.append(f"  {pattern:30} → {glyph}")

        return '\n'.join(lines)
