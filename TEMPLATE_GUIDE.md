# Project Template - Jupyter Inquiry Labors

This repository serves as a template for Jupyter-based data science and analysis projects. It provides a standardized structure and ready-to-use notebook templates.

## Quick Start

### Using this as a Template Repository

1. **On GitHub**: Click "Use this template" button to create a new repository
2. **Clone your new repository**:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

3. **Set up your environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

## Repository Structure

```
project-root/
├── notebooks/              # Jupyter notebooks
│   ├── templates/         # Template notebooks (reusable)
│   │   ├── 01_basic_python_template.ipynb
│   │   ├── 02_data_analysis_template.ipynb
│   │   ├── 03_machine_learning_template.ipynb
│   │   └── 04_visualization_template.ipynb
│   ├── examples/          # Example notebooks
│   └── README.md          # Notebooks documentation
│
├── data/                  # Data files (not tracked by git)
│   ├── raw/              # Original, immutable data
│   ├── processed/        # Cleaned, transformed data
│   └── external/         # External data sources
│
├── src/                   # Source code for reusable modules
│   ├── __init__.py
│   ├── data/             # Data processing scripts
│   ├── features/         # Feature engineering
│   ├── models/           # Model implementations
│   └── visualization/    # Plotting utilities
│
├── output/                # Generated outputs (not tracked)
│   ├── figures/          # Generated graphics and figures
│   ├── models/           # Trained models
│   └── reports/          # Generated analysis reports
│
├── tests/                 # Unit tests
│   └── test_*.py
│
├── docs/                  # Project documentation
│   └── source/
│
├── .github/               # GitHub configuration
│   ├── workflows/        # CI/CD workflows
│   └── ISSUE_TEMPLATE/   # Issue templates
│
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── setup.py             # Package installation
├── README.md            # Project README
└── LICENSE              # License file
```

## Notebook Templates

### Available Templates

1. **Basic Python Template** - General-purpose Python notebook
2. **Data Analysis Template** - Comprehensive data analysis workflow
3. **Machine Learning Template** - Full ML pipeline
4. **Visualization Template** - Various visualization techniques

See `notebooks/README.md` for detailed information on each template.

### Using Templates

To start a new analysis:

```bash
# Copy a template
cp notebooks/templates/02_data_analysis_template.ipynb notebooks/my_analysis.ipynb

# Or create from Jupyter interface
# 1. Open Jupyter
# 2. Navigate to templates
# 3. Open desired template
# 4. File > Make a Copy
# 5. Move copy to notebooks/ root
```

## Setting Up a New Project

### 1. Create Project Structure

```bash
# Create necessary directories
mkdir -p data/{raw,processed,external}
mkdir -p output/{figures,models,reports}
mkdir -p src/{data,features,models,visualization}
mkdir -p tests
```

### 2. Set Up Python Environment

Create `requirements.txt`:
```
jupyter>=1.0.0
notebook>=6.4.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
plotly>=5.0.0
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure Jupyter

Create/edit `~/.jupyter/jupyter_notebook_config.py`:
```python
c.NotebookApp.notebook_dir = '/path/to/your/project'
c.NotebookApp.open_browser = True
```

## Best Practices

### Project Organization

1. **Keep notebooks focused** - One analysis per notebook
2. **Use meaningful names** - Date-prefixed: `2024-01-15-initial-analysis.ipynb`
3. **Document thoroughly** - Add markdown cells explaining your work
4. **Version control** - Commit regularly with clear messages

### Data Management

1. **Never commit data files** - Use `.gitignore`
2. **Document data sources** - Include origin and update dates
3. **Keep raw data immutable** - Process to `processed/` folder
4. **Use relative paths** - Makes project portable

### Code Quality

1. **Extract reusable code** - Move to `src/` modules
2. **Write tests** - Ensure code reliability
3. **Follow style guides** - PEP 8 for Python
4. **Document functions** - Use docstrings

### Collaboration

1. **Clear README** - Explain project purpose and setup
2. **Requirements file** - Document all dependencies
3. **Reproducible results** - Set random seeds
4. **Code reviews** - Review changes before merging

## Workflow Example

### Starting a New Analysis

1. **Copy appropriate template**:
   ```bash
   cp notebooks/templates/02_data_analysis_template.ipynb \
      notebooks/2024-10-30-customer-analysis.ipynb
   ```

2. **Update notebook metadata**:
   - Title
   - Author
   - Date
   - Objective

3. **Load and explore data**:
   ```python
   import pandas as pd
   df = pd.read_csv('data/raw/dataset.csv')
   ```

4. **Follow template structure**:
   - Data loading
   - Exploration
   - Cleaning
   - Analysis
   - Visualization
   - Conclusions

5. **Save outputs**:
   ```python
   # Save processed data
   df.to_csv('data/processed/cleaned_data.csv', index=False)
   
   # Save figures
   plt.savefig('output/figures/analysis_plot.png', dpi=300)
   ```

6. **Commit your work**:
   ```bash
   git add notebooks/2024-10-30-customer-analysis.ipynb
   git commit -m "Add customer analysis notebook"
   git push
   ```

## Advanced Features

### Custom Modules

Create reusable code in `src/`:

```python
# src/data/loader.py
def load_dataset(filepath):
    """Load and perform basic cleaning."""
    import pandas as pd
    df = pd.read_csv(filepath)
    return df

# In notebook:
from src.data.loader import load_dataset
df = load_dataset('data/raw/dataset.csv')
```

### Automated Testing

```python
# tests/test_data_loader.py
import pytest
from src.data.loader import load_dataset

def test_load_dataset():
    df = load_dataset('tests/fixtures/sample.csv')
    assert df is not None
    assert len(df) > 0
```

Run tests:
```bash
pytest tests/
```

### Documentation Generation

Use Sphinx for documentation:
```bash
cd docs
make html
```

## Common Tasks

### Adding New Template

1. Create notebook in `notebooks/templates/`
2. Follow naming convention: `##_name_template.ipynb`
3. Include all necessary sections
4. Add documentation to `notebooks/README.md`

### Updating Dependencies

```bash
# Update requirements.txt
pip freeze > requirements.txt

# Or manually list key dependencies
pip list --format=freeze > requirements.txt
```

### Exporting Notebooks

```bash
# To HTML
jupyter nbconvert --to html notebook.ipynb

# To PDF (requires LaTeX)
jupyter nbconvert --to pdf notebook.ipynb

# To Python script
jupyter nbconvert --to script notebook.ipynb
```

## Troubleshooting

### Jupyter Won't Start
```bash
# Try resetting
jupyter notebook --generate-config
jupyter notebook list
jupyter notebook stop 8888
```

### Kernel Issues
```bash
# List kernels
jupyter kernelspec list

# Install kernel
python -m ipykernel install --user --name=myenv
```

### Import Errors
```bash
# Ensure package is installed
pip install package-name

# Or install in development mode
pip install -e .
```

## Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- [Best Practices for Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this template.

## License

This template is provided under the BSD License. See [LICENSE](LICENSE) for details.
