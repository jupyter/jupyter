# Creating Notebook-Specific Branches

This guide explains how to maintain this repository as a generic template while creating specialized branches for specific notebook use cases (e.g., physical product development, financial analysis, etc.).

## Overview

The `main` branch contains the **generic template** with:
- 4 general-purpose notebook templates
- Flexible directory structure
- Reusable modules and documentation

**Notebook-specific branches** extend the template with:
- Domain-specific notebooks (e.g., product lifecycle, supply chain analysis)
- Specialized data schemas and examples
- Custom utilities for specific workflows
- Domain documentation and best practices

## Workflow Strategy

### Strategy 1: Feature Branches for Specific Notebooks

Use this approach when creating notebooks for specific projects or use cases.

```bash
# Start from the template
git checkout main
git pull origin main

# Create a new branch for your specific notebook/domain
git checkout -b notebook/product-lifecycle-development

# Copy and customize a template
cp notebooks/templates/02_data_analysis_template.ipynb \
   notebooks/product_lifecycle_analysis.ipynb

# Add domain-specific content
# - Customize notebook with product development steps
# - Add example data structures
# - Include domain-specific visualizations

# Commit your changes
git add notebooks/product_lifecycle_analysis.ipynb
git commit -m "Add product lifecycle development notebook"
git push origin notebook/product-lifecycle-development
```

### Strategy 2: Domain-Specific Branch Families

Create long-lived branches for major domains (e.g., manufacturing, finance, healthcare).

```bash
# Create a domain branch from main
git checkout main
git checkout -b domain/physical-product-development

# Add domain-specific notebooks and utilities
mkdir -p notebooks/domain-specific/
cp notebooks/templates/03_machine_learning_template.ipynb \
   notebooks/domain-specific/product_quality_prediction.ipynb

# Add domain-specific utilities
cat > src/domain/product_lifecycle.py << 'EOF'
"""Product lifecycle utilities."""

def calculate_lifecycle_metrics(df):
    """Calculate product lifecycle metrics."""
    # Domain-specific logic
    pass
EOF

# Commit domain customizations
git add notebooks/domain-specific/ src/domain/
git commit -m "Add physical product development domain"
git push origin domain/physical-product-development
```

### Strategy 3: Maintaining Multiple Specialized Configurations

Keep the template generic while maintaining branches with pre-configured setups.

```
Repository Structure:
├── main (generic template)
├── domain/physical-product      # Physical product notebooks
├── domain/financial-analysis    # Financial analysis notebooks  
├── domain/healthcare            # Healthcare notebooks
└── project/specific-client      # Client-specific customization
```

## Best Practices

### 1. Keep Main Branch Generic

**DO:**
- Keep general-purpose templates in `main`
- Maintain flexible, unopinionated structure
- Document common patterns and workflows

**DON'T:**
- Add domain-specific code to `main`
- Include specialized dependencies in base `requirements.txt`
- Create domain-specific directory structures in `main`

### 2. Branch Naming Conventions

```bash
# Domain-specific branches (long-lived)
domain/physical-product-development
domain/financial-modeling
domain/bioinformatics

# Notebook-specific branches (short-lived)
notebook/lifecycle-analysis
notebook/cost-optimization
notebook/quality-control

# Project-specific branches
project/client-name
project/research-study
```

### 3. Merging Strategy

```bash
# Pull updates from main into your domain branch
git checkout domain/physical-product-development
git merge main
# Resolve any conflicts

# If you create generic improvements in domain branch
git checkout main
git cherry-pick <commit-hash>  # Select specific commits to bring back
```

### 4. Documentation in Branches

Each specialized branch should include:

```markdown
# domain/physical-product-development

## Domain-Specific Documentation

- `DOMAIN_GUIDE.md` - Domain concepts and workflows
- `notebooks/domain-specific/README.md` - Notebook descriptions
- `examples/` - Domain-specific example data and notebooks
```

## Example: Physical Product Development Branch

Here's a complete example of creating a physical product development branch:

```bash
# 1. Create branch from main
git checkout main
git pull origin main
git checkout -b domain/physical-product-development

# 2. Create domain directory structure
mkdir -p notebooks/domain-specific/{design,prototype,testing,production}
mkdir -p src/domain/product_lifecycle
mkdir -p data/domain-examples/product-specs

# 3. Create domain-specific notebook
cat > notebooks/domain-specific/product_lifecycle_notebook.ipynb << 'EOF'
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Physical Product Development Lifecycle\n",
    "\n",
    "Complete workflow for product development from concept to production.\n",
    "\n",
    "## Phases\n",
    "1. Concept & Requirements\n",
    "2. Design & Engineering\n",
    "3. Prototyping\n",
    "4. Testing & Validation\n",
    "5. Manufacturing\n",
    "6. Launch & Monitoring"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF

# 4. Create domain-specific utilities
cat > src/domain/product_lifecycle.py << 'EOF'
"""Product lifecycle development utilities."""

def track_design_iterations(designs_df):
    """Track design iteration history."""
    pass

def calculate_prototype_costs(materials_df):
    """Calculate prototyping costs."""
    pass

def analyze_test_results(test_data_df):
    """Analyze product testing results."""
    pass
EOF

# 5. Add domain-specific requirements
cat >> requirements.txt << 'EOF'

# Domain-specific packages for physical product development
solidpython>=1.1.0  # CAD/3D modeling
matplotlib>=3.4.0   # Already included, but ensure for technical drawings
EOF

# 6. Create domain documentation
cat > DOMAIN_GUIDE.md << 'EOF'
# Physical Product Development Domain

This branch extends the generic template for physical product development.

## Domain Notebooks
- `product_lifecycle_notebook.ipynb` - Full lifecycle tracking
- `design/cad_integration.ipynb` - CAD file processing
- `testing/quality_metrics.ipynb` - Quality analysis
- `production/manufacturing_optimization.ipynb` - Production planning

## Domain Utilities
- `src/domain/product_lifecycle.py` - Lifecycle tracking
- `src/domain/cad_processing.py` - CAD file processing
- `src/domain/quality_control.py` - Quality metrics

## Getting Started
See parent TEMPLATE_GUIDE.md, then review domain-specific workflows.
EOF

# 7. Commit and push
git add .
git commit -m "Add physical product development domain branch"
git push origin domain/physical-product-development
```

## Synchronizing Changes

### Pull Template Updates into Domain Branch

```bash
# Update your domain branch with latest template improvements
git checkout domain/physical-product-development
git fetch origin
git merge origin/main
# Resolve conflicts, keeping domain customizations
git push origin domain/physical-product-development
```

### Contributing Generic Improvements Back

```bash
# If you develop something generic in a domain branch
git checkout domain/physical-product-development

# Make improvement (e.g., better visualization function)
# Edit src/visualization/plotter.py

git add src/visualization/plotter.py
git commit -m "Improve correlation plot function"

# Switch to main and cherry-pick
git checkout main
git cherry-pick <commit-hash>
git push origin main
```

## GitHub Workflow

### Creating Branch from Web UI

1. Navigate to repository on GitHub
2. Click branch dropdown
3. Type new branch name (e.g., `domain/physical-product`)
4. Click "Create branch: domain/physical-product from main"
5. Clone and work locally:
   ```bash
   git fetch origin
   git checkout domain/physical-product
   ```

### Pull Request Strategy

```bash
# For domain branches - typically NO PR to main
# Domain branches live independently

# For generic improvements - PR to main
git checkout -b feature/improved-visualization
# Make changes
git push origin feature/improved-visualization
# Create PR: feature/improved-visualization -> main
```

## Summary

- **Keep `main` generic** - universal templates and structure
- **Create domain branches** - specialized notebooks and utilities
- **Use branch naming conventions** - clear hierarchy (domain/, notebook/, project/)
- **Document domain branches** - add DOMAIN_GUIDE.md
- **Sync bidirectionally** - merge main updates, cherry-pick improvements back
- **No cross-contamination** - domain code stays in domain branches

This approach allows you to:
✅ Maintain a clean, reusable template in `main`
✅ Create specialized branches for different domains
✅ Share the template with others without domain-specific clutter
✅ Update domain branches with template improvements
✅ Contribute generic improvements back to the template
