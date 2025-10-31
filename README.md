# Jupyter Inquiry Labors - Template Repository

*Read this in other languages: [English](README.md), [Español](README.es-ES.md), [Português](README.pt-BR.md), [Français](README.fr-FR.md)*

A comprehensive template repository for Jupyter-based data science and analysis projects. This template provides a standardized structure, ready-to-use notebook templates, and best practices for organizing your data science work.

## 🚀 Quick Start

### Using This Template

1. Click the "Use this template" button on GitHub to create your own repository
2. Clone your new repository:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

3. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Start Jupyter:
   ```bash
   jupyter notebook
   ```

## 📁 Repository Structure

```
├── notebooks/              # Jupyter notebooks
│   ├── templates/         # Reusable notebook templates
│   ├── examples/          # Example notebooks
│   └── README.md          # Notebook documentation
├── data/                  # Data files (gitignored)
│   ├── raw/              # Original data
│   ├── processed/        # Cleaned data
│   └── external/         # External sources
├── src/                   # Reusable Python modules
│   ├── data/             # Data processing
│   ├── features/         # Feature engineering
│   ├── models/           # Model code
│   └── visualization/    # Plotting utilities
├── output/                # Generated outputs (gitignored)
│   ├── figures/          # Plots and visualizations
│   ├── models/           # Trained models
│   └── reports/          # Analysis reports
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── requirements.txt       # Python dependencies
```

## 📓 Notebook Templates

This repository includes four comprehensive notebook templates:

1. **Basic Python Template** - General-purpose Python notebook with standard structure
2. **Data Analysis Template** - Complete data analysis workflow with EDA and statistics
3. **Machine Learning Template** - Full ML pipeline from preprocessing to evaluation
4. **Visualization Template** - Comprehensive guide to creating various plot types

See [`notebooks/README.md`](notebooks/README.md) for detailed information on each template.

## 📚 Documentation

- **[Template Guide](TEMPLATE_GUIDE.md)** - Comprehensive guide to using this template
- **[Branching Strategy](BRANCHING_STRATEGY.md)** - Creating notebook-specific branches while keeping main generic
- **[Notebooks README](notebooks/README.md)** - Documentation for notebook templates
- **[Data README](data/README.md)** - Data management guidelines
- **[Source Code README](src/README.md)** - Guidelines for reusable modules

## 🛠️ Features

- **Standardized Structure** - Consistent organization across projects
- **Ready-to-Use Templates** - Four comprehensive notebook templates
- **Best Practices** - Built-in guidelines for data science workflows
- **Reusable Modules** - Structure for extracting common code
- **Documentation** - Comprehensive docs and examples
- **Git-Ready** - Pre-configured `.gitignore` for data science projects

## 📖 Usage Example

```bash
# Copy a template
cp notebooks/templates/02_data_analysis_template.ipynb notebooks/my_analysis.ipynb

# Start working in Jupyter
jupyter notebook notebooks/my_analysis.ipynb
```

## 🌿 Creating Specialized Branches

This template is designed to stay **generic and reusable** in the `main` branch. For domain-specific work (e.g., physical product development, financial modeling), create specialized branches:

```bash
# Create a domain-specific branch
git checkout -b domain/physical-product-development

# Add specialized notebooks and utilities
cp notebooks/templates/02_data_analysis_template.ipynb \
   notebooks/product_lifecycle_analysis.ipynb

# Customize for your specific domain
# Commit and push your specialized branch
git add .
git commit -m "Add product lifecycle development notebooks"
git push origin domain/physical-product-development
```

**Key Benefits:**
- ✅ Keep `main` clean and generic for reuse
- ✅ Create unlimited specialized branches for different domains
- ✅ Merge template improvements from `main` into domain branches
- ✅ Share the generic template without domain-specific clutter

See **[BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md)** for complete guide and examples.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the BSD License - see the [LICENSE](LICENSE) file for details.

---

## Original Jupyter Metapackage Documentation

This repository is built on top of the Jupyter metapackage for installation and documents

## Documentation structure

This documentation uses the [Sphinx](https://sphinx-doc.org) documentation engine.

The documentation is located in the `docs/source` folder. When you build the documentation, it will be placed in the `docs/build` folder.
It is written in a combination of [reStructuredText](https://docutils.sourceforge.io/rst.html) and [MyST Markdown](https://myst-parser.readthedocs.io/).

## Build the documentation locally

There are a few ways to build the documentation; see below for instructions:

### Build the documentation automatically with `nox`

The easiest way to build the documentation locally is by using the [`nox` command line tool](https://nox.thea.codes/). This tool makes it easy to automate commands in a repository, and we have included a `docs` command to quickly install the dependencies and build the documentation.

To build and preview the site locally, follow these steps:

1. **Clone this repository**.

   ```console
   $ git clone https://github.com/jupyter/jupyter
   $ cd jupyter
   ```
2. **Install `nox`**

   ```console
   $ pip install nox
   ```
3. **Run the `docs` command**

   ```console
   $ nox -s docs
   ```

This will install the needed dependencies in a virtual environment using `pip`.
It will then place the documentation in the `docs/build/html` folder.
You may explore these HTML files in order to preview the site.

#### Create a live server to automatically preview changes

There is another `nox` command that will do the above, and also create a live server that watches your source files for changes, and auto-builds the website any time a change is made.

To start this live server, use the following `nox` command:

```console
$ nox -s docs-live
```

When the build is finished, go to the URL that is displayed. It should show a live preview of your documentation.

To stop serving the website, press **`Ctrl`**-`C` in your terminal

### Build the documentation manually

To build the documentation manually, follow these steps:

First, install [the `miniconda` Python distribution](https://conda.io/miniconda.html).

Next, navigate to the `/docs` directory and create a `conda` environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
source activate jupyter_docs
```

**Build the docs** using Sphinx with the following commands:

```bash
make clean
make html
```

The docs will be built in `build/html`. They can be viewed by opening `build/html/index.html` or starting an HTTP server and navigating to `0.0.0.0:8000` in your web browser.

```bash
python3 -m http.server
```

## Releasing the jupyter metapackage

Anyone with push access to this repo can make a release
of the Jupyter metapackage (this happens very rarely).
We use [tbump][] to publish releases.

tbump updates version numbers and publishes the `git tag` of the version.
[Our GitHub Actions](https://github.com/jupyter/jupyter/actions)
then build the releases and publish them to PyPI.

The steps involved:

1. Install tbump: `pip install tbump`
2. Tag and publish the release `tbump $NEW_VERSION`.

That's it!

[tbump]: https://github.com/your-tools/tbump
