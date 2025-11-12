# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

To use this template, you need Cookiecutter installed:

```bash
pip install cookiecutter
```

Then, generate a new project:

```bash
cookiecutter https://github.com/{{cookiecutter.author_name}}/{{cookiecutter.project_slug}}.git
```

Or if local:

```bash
cookiecutter /path/to/this/template
```

## Features

- FastAPI for API
- PyTorch for ML
- Docker support
- Testing with pytest
- Linting with flake8, black, isort

## Usage

After generating the project, install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python -m app.main
```

Or with uvicorn:

```bash
uvicorn app.main:app --reload
```