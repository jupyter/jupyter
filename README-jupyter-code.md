# Jupyter Code: SWOT Water Depth Analysis

This README explains how to open and run the SWOT Water Depth analysis notebook and work with the associated raster data.

## Files
- Notebook: SWOT_Water_Depth_Analysis_Public.ipynb
- Raster DEM: CooperLiDAR_DEM_25m_EPSG4283.tif
- AUS Geoid: au_ga_AUSGeoid09_V1.01.tif

## Prerequisites
- Python 3.9+
- JupyterLab or Jupyter Notebook

Recommended Python packages:
- numpy, pandas, matplotlib
- geopandas, rasterio, shapely, pyproj

## Quick Setup
### Option A: Virtual environment + pip
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```
Open SWOT_Water_Depth_Analysis_Public.ipynb from the file browser and run cells.

### Option B: System Jupyter
If you already have Jupyter installed, simply start it in the repository directory:
```bash
jupyter lab
```

### Option C: Conda environment (reproducible)
Create and use the pre-defined environment with conda-forge packages:
```bash
conda env create -f environment-swot.yml
conda activate swot
jupyter lab
```

## Data Notes
- Ensure the TIFF files are present in the repository root.
- If your analysis requires additional vector data (e.g., shapefiles), place them alongside the notebook and update any file paths in the notebook accordingly.

## Tips
- Use a new kernel after changing environments to avoid package conflicts.
- If geopandas/rasterio installation fails on Linux due to GDAL/GEOS dependencies, consider using conda:
```bash
conda create -n swot python=3.10 jupyterlab geopandas rasterio shapely pyproj -y
conda activate swot
jupyter lab
```

## Troubleshooting
- File not found: verify paths in the notebook match actual file locations.
- CRS/Projection issues: use pyproj to transform coordinates; check the EPSG codes in raster metadata.
- Memory errors: work with smaller AOIs or resample rasters before processing.
