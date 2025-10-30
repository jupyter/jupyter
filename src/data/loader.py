"""
Data loading utilities for common data formats.

This module provides simple, reusable functions for loading
various data formats commonly used in data science projects.
"""

import pandas as pd
from pathlib import Path
from typing import Optional, Union


def load_csv(
    filepath: Union[str, Path],
    encoding: str = 'utf-8',
    **kwargs
) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        filepath: Path to the CSV file
        encoding: File encoding (default: 'utf-8')
        **kwargs: Additional arguments passed to pd.read_csv
        
    Returns:
        DataFrame containing the loaded data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        
    Example:
        >>> df = load_csv('data/raw/dataset.csv')
        >>> df = load_csv('data/raw/dataset.csv', sep=';', decimal=',')
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath, encoding=encoding, **kwargs)


def load_excel(
    filepath: Union[str, Path],
    sheet_name: Union[str, int] = 0,
    **kwargs
) -> pd.DataFrame:
    """
    Load an Excel file into a pandas DataFrame.
    
    Args:
        filepath: Path to the Excel file
        sheet_name: Name or index of sheet to load (default: 0)
        **kwargs: Additional arguments passed to pd.read_excel
        
    Returns:
        DataFrame containing the loaded data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        
    Example:
        >>> df = load_excel('data/raw/dataset.xlsx')
        >>> df = load_excel('data/raw/dataset.xlsx', sheet_name='Sheet2')
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)


def save_processed_data(
    df: pd.DataFrame,
    filename: str,
    output_dir: Union[str, Path] = 'data/processed',
    **kwargs
) -> Path:
    """
    Save a DataFrame to the processed data directory.
    
    Args:
        df: DataFrame to save
        filename: Name of the output file (should include extension)
        output_dir: Directory to save to (default: 'data/processed')
        **kwargs: Additional arguments passed to to_csv or to_excel
        
    Returns:
        Path to the saved file
        
    Example:
        >>> save_processed_data(df, 'cleaned_data.csv', index=False)
        >>> save_processed_data(df, 'analysis_results.xlsx', index=False)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = output_dir / filename
    
    if filepath.suffix == '.csv':
        df.to_csv(filepath, **kwargs)
    elif filepath.suffix in ['.xlsx', '.xls']:
        df.to_excel(filepath, **kwargs)
    else:
        raise ValueError(f"Unsupported file format: {filepath.suffix}")
    
    return filepath


def get_data_info(df: pd.DataFrame) -> dict:
    """
    Get a summary of DataFrame information.
    
    Args:
        df: DataFrame to analyze
        
    Returns:
        Dictionary containing data summary
        
    Example:
        >>> info = get_data_info(df)
        >>> print(f"Shape: {info['shape']}")
        >>> print(f"Missing values: {info['missing_values']}")
    """
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum(),
        'duplicates': df.duplicated().sum()
    }
