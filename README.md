# Colaboradados Webpage Django

## Running

### Requirements
- Pipenv

### Setup
- On project root, do the following:
- Install project dependencies:
  `pipenv install --dev`
- Create a copy of ``.env.example``:  
  `cp .env.example .env`
- Fill ``.env`` file with the necessary variables.
- Run the migrations:  
  `./manage.py migrate`


### Running the project
- Open a command line window and go to the project's directory.
- `pipenv shell`
- `./manage.py runserver`

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.
