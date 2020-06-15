# {{cookiecutter.project_name}}

{{cookiecutter.project_name}} is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install {{cookiecutter.project_name}}.

```bash
conda env create -f environment.yaml
conda activate {{cookiecutter.project_slug}}
pip install -e .
```


{% if cookiecutter.example_code == 'true' %}
## Usage

```python
from {{cookiecutter.project_slug}}.example import say_hello

say_hello("Mike") # returns 'Hello, Mike!'
```
{% endif %}
## Tests
You can do pytests with the following commands:
```python
pytest tests
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)