# Vantage-Template Repo for Python Package

A Cookiecutter for creating a python project.

## Usage

 1. Install [cookiecutter][1]

        pip install cookiecutter

 2. Go to the place where you want to create a project and

 3. Run cookiecutter against this repo

        cookiecutter https://github.com/Vantage-AI/vantage-template

## Documentation

### Install all project requirements

    pip install -r requirements.txt


### Generating updated documentation

Documentation is automatically generated using [Sphinx][2]. After adding new files to your package, be sure to run the following commands to generate updated documentation:

``` bash
> cd docs
> sphinx-apidoc -f -o source/  ../your/project/path
> make html
```

Your updated documentation can then be found in `docs/build/html/index.html`.

### ReadTheDocs.org

If you want to display your documentation on [ReadTheDocs.org][3], sign up for an account, import[4] your project and fill out your GitHub details.

### Pre-commit hooks

- Use pre-commit to automate checks for each commit, see their [website](https://pre-commit.com/) for more info.
- Configuration is in */.pre-commit-config.yaml*.
- For installation:
    1. run ```pip install pre-commit``` (or ```pip install env\requirements.txt```) in your environment.
    2. run ```pre-commit install``` in this repo.
    3. Now with each commit, pre-commit is automatically executed.        

[1]: https://github.com/audreyr/cookiecutter
[2]: https://www.sphinx-doc.org/
[3]: https://readthedocs.org/
[4]: https://readthedocs.org/dashboard/import/
