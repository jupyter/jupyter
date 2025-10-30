# Data Directory

This directory contains all data files for the project.

## Structure

- `raw/` - Original, immutable data files
- `processed/` - Cleaned and transformed data ready for analysis
- `external/` - Data from third-party sources

## Guidelines

1. **Never commit large data files** - Data files are ignored by git
2. **Document data sources** - Include README or data dictionary
3. **Keep raw data immutable** - Always process to new files
4. **Use consistent naming** - `YYYY-MM-DD-description.csv`

## Data Management

### Adding New Data

```bash
# Place original data in raw/
cp source_data.csv data/raw/

# Process and save to processed/
python scripts/process_data.py
```

### Data Documentation

For each dataset, document:
- Source and origin
- Date acquired
- Description of fields
- Any preprocessing done
- Known issues or limitations

Create a `data_dictionary.md` file describing all fields.

## Example Structure

```
data/
├── raw/
│   ├── 2024-10-30-customer-data.csv
│   └── 2024-10-30-transaction-data.csv
├── processed/
│   ├── cleaned-customer-data.csv
│   └── aggregated-transactions.csv
└── external/
    └── industry-benchmarks.csv
```
