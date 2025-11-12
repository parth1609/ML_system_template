# ML System Cookiecutter Template

A Cookiecutter template for creating scalable ML systems with FastAPI, PyTorch, and more.

## Quickstart

Install Cookiecutter:

```bash
pip install cookiecutter
```

Generate a new project:

```bash
cookiecutter gh:parth1609/ML_system_template
```

Or from local path:

```bash
cookiecutter /path/to/ml_system_template
```

Follow the prompts to customize your project.

## What it includes

- FastAPI application structure
- ML model integration with PyTorch
- Docker and docker-compose setup
- Testing framework (pytest)
- Code quality tools (black, isort, flake8)
- UV for dependency management

## Project Structure

```
{{cookiecutter.project_slug}}/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── main.py
├── tests/
├── pyproject.toml
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.