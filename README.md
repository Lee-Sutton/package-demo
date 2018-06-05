# Hitchhiker's guide to python
- With Lam's work in machine learning we're likely going to be using 
python for machine learning
- Today I wanted to talk a little bit about python best practices including setting up a project and 

## Installing python
- If you haven't already installed python you can install python in a few ways
- Anaconda (reccomended) https://www.anaconda.com/download
- Through package management (homebrew, apt-get, pacman, etc.) http://docs.python-guide.org/en/latest/ 
- Go for python3

## Installing packages
- pip (comes with python)
- pip can be used to install packages from pypi (or any package with a setup.py)

## Managing dependencies
- Lots of information out there
- virtual envs, conda envs, pipenv
- pipenv is the official reccomended way to manage python dependencies for package_name project (https://docs.pipenv.org/)

## Pipenv
- We're all familiar with npm
- pip and pipenv serve similar purposes
- Running

```bash
pip install [package_name]
```

- is like running:

```bash
npm -g install [package_name]
```

- Whereas if you run:

```bash
pipenv install [package_name]
```

- It's like running:

```bash
npm install --save [package_name]
```

## Pipenv example
- Let's create a new project as an example
- We first need to install pipenv

```bash
pip install pipenv
```

```bash
mkdir ml-project
cd ml-project
pipenv install requests
```

- This creates a pipfile and a pipfile.lock which contains your projects dependencies
- the pipfile *should* be checked into your vcs

## How does pipfile work?
- Creates it's python in the project directory (virtual-environment)
- This python has it's set of installed packages seperate from your system python
- To activate this virtual-environment run:

```bash
pipenv shell
```

- leave the virtual-environment with

```bash
exit
```

- You can see the path to the python virtual-environment by running 
```bash
pipenv --venv
```

- Kenneth Rietz is the creator of pipenv. He gives a nice demo here: https://docs.pipenv.org/

## Creating your own python package
- Any directory containing an \_\_init\_\_.py file is considered a python package
- You really shouldn't include any code in these files (a little bit is ok)

- Within the directory you'll have python files
- each python file is a module
- you can import modules using the import syntax
- important note you cannot include - in filenames in python, you must use _ instead

## Running scripts
- You can run a python script as follows
```bash
python [filename].py
```

- This will run all the 'top level statements'

```python
import test_package
print('this will run')

def test_function():
	print('this will not run')
```

- Python has a unique feature it allows you to run parts of the file only if the script is run

```python
def main():
	print('this will only run if called from the command line')

if __name__ == '__main__':
	main()

```

- the main function above will only run if invoked as follows:

```bash
python [filename].py
```

- it will not run if the file is imported

## Setup.py
- The setup.py file specifies how the project is installed (similar to package.json)
- it also allows you to define entry points if you want to create a command line application
- I've created an example application if you want to check it out here: 

## Pep8, flake8, and pylint
- official style guide for python code (please follow it)

## Pytest
- Pytest is a unit test runner
- From the website "The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries."
- Python comes with a built in test runner but pytest is much more popular
- pytest makes writing tests very easy
- it looks for files with *test* in the name
- within the file it looks for functions/classes with test or Test in the name

```python
def test_add():
	assert 3 + 3 == 6
```
