# python-project-template

### Dev Tools
- [Pytest](https://docs.pytest.org/en/stable/) - Unit testing
- [Syrupy](https://github.com/tophat/syrupy) - Pytest snapshot plugin
- [Ruff](https://docs.astral.sh/ruff/) - An extremely fast Python linter and code formatter
- [PDM](https://pdm-project.org/en/latest/) - optional python dependency manager

- [VS Code Extensions](./.vscode/extensions.json)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
  - [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) - Data viewing, cleaning and preparation for tabular datasets
  - [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

format - `ruff format`
lint - `ruff check`
lint & fix - `ruff check --fix`

### Clone to local
```
git clone --depth 1 https://github.com/kylegl/python-project-template.git my-python-project
cd my-python-project

# setup venv in your project folder

# install dependencies
pip install .
```

### Checklist
When you use this template, follow this list
[] Change the name in `pyproject.toml`
[] Rename src/my_python_project
[] Cleanup README


### Development
Code formatting happens on save. To do manually
```
ruff format
```
To lint
```
ruff check
```
or lint & fix
```
ruff check -fix
```
To test
```
pytest # -vv (for verbose)
```
To update test snapshots
```
pytest --update-snapshots
```
