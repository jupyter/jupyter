"""
AI Scholarship Module

Tools for ingesting, organizing, and synthesizing AI-generated research outputs
from multiple platforms (Perplexity, Claude, GPT, Grok) in recursive workflows.
"""

from .ingestion import ScholarshipIngester
from .synthesis import ScholarshipSynthesizer
from .workflow import MultiPlatformOrchestrator

__all__ = [
    'ScholarshipIngester',
    'ScholarshipSynthesizer',
    'MultiPlatformOrchestrator',
]
