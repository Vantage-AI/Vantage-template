# Vantage-Template Repo for Python Package
A Cookiecutter for creating a python project.

## Usage

 1. Install [cookiecutter][1]

        pip install cookiecutter

 2. Go to the place where you want to create a project and

 3. Run cookiecutter against this repo

        cookiecutter https://github.com/Vantage-AI/vantage-template

#### pre-commit hooks
- Use pre-commit to automate checks for each commit, see their [website](https://pre-commit.com/) for more info.
- Configuration is in */.pre-commit-config.yaml*.
- For installation:
    1. run ```pip install pre-commit``` (or ```pip install env\requirements.txt```) in your environment.
    2. run ```pre-commit install``` in this repo.
    3. Now with each commit, pre-commit is automatically executed.        

[1]: https://github.com/audreyr/cookiecutter
