# Source Code Directory

This directory contains reusable Python modules for the project.

## Structure

```
src/
├── __init__.py
├── data/           # Data loading and processing
├── features/       # Feature engineering
├── models/         # Model implementations
└── visualization/  # Plotting and visualization utilities
```

## Usage

Import modules in your notebooks:

```python
from src.data import loader
from src.features import engineer
from src.models import train_model
from src.visualization import plotter
```

## Guidelines

1. **Keep functions focused** - Single responsibility principle
2. **Write docstrings** - Document all public functions
3. **Add type hints** - Improve code clarity
4. **Write tests** - For all public functions
5. **Follow PEP 8** - Maintain code style consistency

## Example Module

```python
# src/data/loader.py
"""Data loading utilities."""

import pandas as pd
from pathlib import Path

def load_csv(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Load CSV file and return DataFrame.
    
    Args:
        filepath: Path to CSV file
        **kwargs: Additional arguments for pd.read_csv
        
    Returns:
        DataFrame with loaded data
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath, **kwargs)
```

## Testing

Write tests in `tests/` directory:

```python
# tests/test_loader.py
from src.data.loader import load_csv

def test_load_csv():
    df = load_csv('tests/fixtures/sample.csv')
    assert df is not None
    assert len(df) > 0
```
