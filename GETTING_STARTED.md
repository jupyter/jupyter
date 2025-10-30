# Getting Started with Your New Project

Welcome! You've created a new project from the Jupyter Inquiry Labors template. Follow these steps to get started:

## Initial Setup

### 1. Update Repository Information

- [ ] Update `README.md` with your project name and description
- [ ] Update `setup.py` with your project details
- [ ] Review and update `LICENSE` if needed

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install project in development mode (optional)
pip install -e .
```

### 3. Configure Git

```bash
# Set your git user info if not already set
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create .env file for local settings (don't commit this)
echo "venv/" >> .gitignore
```

## Quick Start Tasks

### Start Your First Analysis

1. **Copy a template notebook**:
   ```bash
   cp notebooks/templates/02_data_analysis_template.ipynb notebooks/2024-10-30-initial-analysis.ipynb
   ```

2. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

3. **Open your new notebook** and start coding!

### Organize Your Data

1. **Add your data files**:
   ```bash
   # Place original data in raw/
   cp /path/to/your/data.csv data/raw/
   ```

2. **Document your data** in `data/README.md`

### Create Reusable Code

1. **Add utility functions** to `src/` modules:
   ```python
   # src/data/loader.py
   def load_my_data():
       # Your code here
       pass
   ```

2. **Use in notebooks**:
   ```python
   from src.data.loader import load_my_data
   data = load_my_data()
   ```

## Project Customization

### Update Package Information

Edit `setup.py`:
```python
setup_args = dict(
    name='your-project-name',
    version='0.1.0',
    description='Your project description',
    author='Your Name',
    author_email='your.email@example.com',
    # ... update other fields
)
```

### Add Project-Specific Dependencies

Edit `requirements.txt`:
```
# Add your specific packages
your-package>=1.0.0
```

Then reinstall:
```bash
pip install -r requirements.txt
```

### Customize Directory Structure

Add project-specific directories as needed:
```bash
mkdir -p scripts
mkdir -p config
mkdir -p logs
```

## Next Steps

### Development Workflow

1. **Create a new branch** for each feature:
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. **Make your changes** and commit regularly:
   ```bash
   git add .
   git commit -m "Add: description of changes"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin feature/my-new-feature
   ```

4. **Create a Pull Request** for review

### Best Practices

- [ ] Write tests for your code
- [ ] Document your functions and modules
- [ ] Keep notebooks focused and well-organized
- [ ] Use version control regularly
- [ ] Review the [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) for best practices

## Resources

- [Template Guide](TEMPLATE_GUIDE.md) - Comprehensive usage guide
- [Notebooks README](notebooks/README.md) - Template documentation
- [Contributing Guide](CONTRIBUTING.md) - How to contribute

## Cleanup

Once you're set up, you can delete this file:
```bash
rm GETTING_STARTED.md
git commit -m "Remove getting started guide"
```

## Need Help?

- Check the documentation in each directory
- Review the example notebooks in `notebooks/examples/`
- Open an issue in the original template repository for template-related questions

Happy analyzing! 🎉
