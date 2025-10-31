"""
Unit tests for data loading utilities.

Run with: pytest tests/
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.loader import load_csv, get_data_info, save_processed_data


class TestDataLoader:
    """Tests for data loading functions."""
    
    def test_get_data_info(self):
        """Test getting data information."""
        # Create sample DataFrame
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [1.0, 2.0, None, 4.0, 5.0],
            'C': ['a', 'b', 'c', 'd', 'e']
        })
        
        info = get_data_info(df)
        
        # Check returned structure
        assert 'shape' in info
        assert 'columns' in info
        assert 'missing_values' in info
        assert 'duplicates' in info
        
        # Check values
        assert info['shape'] == (5, 3)
        assert len(info['columns']) == 3
        assert info['missing_values']['B'] == 1
        assert info['duplicates'] == 0
    
    def test_get_data_info_with_duplicates(self):
        """Test get_data_info with duplicate rows."""
        df = pd.DataFrame({
            'A': [1, 2, 1, 2],
            'B': [1, 2, 1, 2]
        })
        
        info = get_data_info(df)
        assert info['duplicates'] == 2


class TestDataSaver:
    """Tests for data saving functions."""
    
    def test_save_processed_data_csv(self, tmp_path):
        """Test saving DataFrame as CSV."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        
        # Save to temporary directory
        output_path = save_processed_data(
            df, 
            'test_data.csv',
            output_dir=tmp_path,
            index=False
        )
        
        # Check file was created
        assert output_path.exists()
        
        # Check content
        loaded_df = pd.read_csv(output_path)
        pd.testing.assert_frame_equal(df, loaded_df)


# Run tests with: pytest tests/test_data_loader.py -v
