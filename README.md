# Spyder Plugin Cookiecutter

[![Linux tests](https://github.com/spyder-ide/spyder5-plugin-cookiecutter/workflows/Linux%20tests/badge.svg)](https://github.com/spyder-ide/spyder5-plugin-cookiecutter/actions?query=workflow%3A%22Linux+tests%22)

## Installation

Make sure you have [cookiecutter](https://cookiecutter.readthedocs.io/) installed on your working environment.

### With pip

```bash
pip install cookiecutter
```

### With conda

```bash
conda install cookiecutter
```

## Usage

Running the cookiecutter.

```bash
cookiecutter https://github.com/spyder-ide/spyder5-plugin-cookiecutter
```

You can use the default values for quick testing, press enter until finished.
You should see something like:

```bash
full_name [Spyder Bot]:
email [spyder.python@gmail.com]:
github_username [spyder-bot]:
github_org [spyder-ide]:
project_name [Spyder Boilerplate]:
project_short_description [Boilerplate needed to create a Spyder Plugin.]:
project_pypi_name [spyder-boilerplate]:
project_package_name [spyder_boilerplate]:
pypi_username [spyder-bot]:
Select plugin_type:
1 - Spyder Dockable Plugin
2 - Spyder Plugin
Choose from 1, 2 [1]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

## Installing the Spyder plugin

After the cookiecutter has been created, install it for local development with:

```bash
cd spyder-boilerplate
python setup.py develop
```

Now if you run Spyder from master you should see a new Dockable Plugin appear.
