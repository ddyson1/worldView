# Conda Environment Setup

## Compatible Versions

- **Python**: 3.10, 3.11, or 3.12 (we recommend **3.11**)
- **Django**: 5.2.x (currently using 5.2.9)

## Quick Setup

### Option 1: Using environment.yml (Recommended)

```bash
# Create environment from file
conda env create -f environment.yml

# Activate the environment
conda activate worldview-news

# Verify installation
python --version
django-admin --version
```

### Option 2: Manual Setup

```bash
# Create a new conda environment with Python 3.11
conda create -n worldview-news python=3.11 -y

# Activate the environment
conda activate worldview-news

# Install dependencies
pip install -r requirements.txt

# Verify installation
python --version
django-admin --version
```

## Initialize the Database

After activating your environment:

```bash
# Run migrations
python manage.py migrate

# Load sample financial news sources
python manage.py loaddata news/fixtures/initial_data.json

# Create admin user
python manage.py createsuperuser

# Fetch some news
python manage.py fetch_news

# Start the development server
python manage.py runserver
```

## Managing the Environment

```bash
# Activate environment
conda activate worldview-news

# Deactivate environment
conda deactivate

# List all conda environments
conda env list

# Remove environment (if needed)
conda env remove -n worldview-news

# Update environment from file
conda env update -f environment.yml --prune
```

## Adding New Dependencies

When you install new packages:

```bash
# Activate environment
conda activate worldview-news

# Install via pip
pip install package-name

# Update requirements.txt
pip freeze | grep package-name >> requirements.txt

# Or update environment.yml manually
```

## Python Version Compatibility

Django 5.2 requirements:
- ✅ Python 3.10 - Fully supported
- ✅ Python 3.11 - **Recommended** (best performance)
- ✅ Python 3.12 - Fully supported (latest)
- ❌ Python 3.9 or earlier - Not supported

## Troubleshooting

**Issue**: `conda: command not found`
```bash
# Install Miniconda or Anaconda first
# Download from: https://docs.conda.io/en/latest/miniconda.html
```

**Issue**: Environment creation fails
```bash
# Update conda first
conda update -n base -c defaults conda

# Try creating again
conda env create -f environment.yml
```

**Issue**: Django import errors
```bash
# Ensure you're in the right environment
conda activate worldview-news

# Reinstall Django
pip install --force-reinstall Django>=5.2.0
```

## Development Workflow

```bash
# 1. Activate environment (do this first every time!)
conda activate worldview-news

# 2. Make sure you're in the project directory
cd /path/to/worldView

# 3. Run your Django commands
python manage.py runserver
python manage.py fetch_news
python manage.py shell

# 4. When done, deactivate
conda deactivate
```
