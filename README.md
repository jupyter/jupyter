# Jupyter

Jupyter metapackage for installation and docs.

## Running the docs locally
First navigate to the `/docs` directory and create a `conda` environment:

```bash
conda env create -f environment.yml  
```  

Activate the environment:

```bash
source activate jupyter_docs  
```

Build the docs:

```bash
make clean  
make html
```

The docs will be built in `build/html`. They can be viewed by starting an HTTP server and navigating to `0.0.0.0:8000` in your web browser.
```bash
python3 -m http.server
```
