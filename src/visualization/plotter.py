"""
Visualization utilities for common plotting tasks.

This module provides helper functions for creating consistent,
publication-quality visualizations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, Tuple, List


def setup_plot_style(style: str = 'seaborn-v0_8-whitegrid') -> None:
    """
    Set up consistent plotting style for all visualizations.
    
    Args:
        style: Matplotlib style to use
        
    Example:
        >>> setup_plot_style()
        >>> plt.plot([1, 2, 3], [1, 2, 3])
        >>> plt.show()
    """
    plt.style.use(style)
    sns.set_palette('husl')
    
    # Set default figure size
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14


def plot_distribution(
    data: pd.Series,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    bins: int = 30,
    figsize: Tuple[int, int] = (10, 6)
) -> plt.Figure:
    """
    Create a distribution plot with histogram and KDE.
    
    Args:
        data: Data to plot
        title: Plot title
        xlabel: X-axis label
        bins: Number of histogram bins
        figsize: Figure size
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> fig = plot_distribution(df['column'], title='Distribution of Column')
        >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Histogram
    ax.hist(data.dropna(), bins=bins, alpha=0.7, edgecolor='black', density=True)
    
    # KDE
    data.plot(kind='density', ax=ax, linewidth=2)
    
    ax.set_title(title or f'Distribution of {data.name}')
    ax.set_xlabel(xlabel or data.name)
    ax.set_ylabel('Density')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(
    df: pd.DataFrame,
    figsize: Tuple[int, int] = (10, 8),
    title: str = 'Correlation Matrix'
) -> plt.Figure:
    """
    Create a correlation heatmap for numerical columns.
    
    Args:
        df: DataFrame containing numerical data
        figsize: Figure size
        title: Plot title
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> fig = plot_correlation_heatmap(df)
        >>> plt.show()
    """
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.heatmap(
        correlation,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8},
        ax=ax
    )
    
    ax.set_title(title)
    plt.tight_layout()
    return fig


def save_figure(
    fig: plt.Figure,
    filename: str,
    output_dir: str = 'output/figures',
    dpi: int = 300,
    formats: List[str] = ['png']
) -> List[str]:
    """
    Save a figure in multiple formats.
    
    Args:
        fig: Matplotlib figure to save
        filename: Base filename (without extension)
        output_dir: Directory to save to
        dpi: Resolution for raster formats
        formats: List of formats to save (e.g., ['png', 'pdf'])
        
    Returns:
        List of saved file paths
        
    Example:
        >>> fig = plt.figure()
        >>> plt.plot([1, 2, 3])
        >>> paths = save_figure(fig, 'my_plot', formats=['png', 'pdf'])
    """
    from pathlib import Path
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    saved_paths = []
    for fmt in formats:
        filepath = output_dir / f"{filename}.{fmt}"
        fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
        saved_paths.append(str(filepath))
    
    return saved_paths
