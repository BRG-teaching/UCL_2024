# UCL 2024
Form-finding of compression only shell structures

# Introduction to COMPAS

[📃 COMPAS docs](https://compas.dev)

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/), or miniconda if you prefer...
* [Visual Studio Code](https://code.visualstudio.com/) with the `Python` and `Pylance` extensions from Microsoft.
* [Rhino 7/8](https://www.rhino3d.com/download) (Optional)

## Installation

> **IMPORTANT**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using <code>conda</code>? Make sure to run this at least once:

    conda config --add channels conda-forge

Then create the workshop environment and install the dependencies:

    conda env create -f https://raw.githubusercontent.com/compas-Workshops/BFH24/main/env.yml TO BE UPDATED

> **IMPORTANT**: If you're on Windows, use `env_win.yml`. On Mac or Linux, use `env.yml`.

### Verify installation

Activate the environment

    conda activate ucl24

> **NOTE**: You should see that your prompt changed from `(base)` to `(ucl24)`

Run the verification command `python -m compas`:

    (ucl24) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 2.2.1
    Python: 3.12.4 (CPython)
    Extensions: ['compas', 'compas-viewer', 'compas-tna', 'compas-dr', 'compas-fd']

# Working in Rhino 8
If you have a Rhino 8 License you can directly pip install COMPAS and all the packages needed for this workshop in Rhino 8 and run the scripts from the Rhino 8 ScriptEditor.

> **Note:**
> 
> The installation procedures listed here are for using COMPAS with CPython in Rhino 8.


## Installation

Rhino 8 comes with its own CPython executable (Python 3.9). This procedure simply uses that executable and its associated `pip` to install COMPAS. The location of the executable is different on different platforms.

* Windows: `%USERPROFILE%\.rhinocode\py39-rh8\python.exe`
* macOS: `~/.rhinocode/py39-rh8/python3.9`

> **Note:**
> 
> If you already have an installation of COMPAS on your system, you can try finding the Rhino 8 Python executable by running the following in a terminal or command prompt:
> 
> ```bash
> python -m compas_rhino.print_python_path
> ```

### Update `pip`

Before installing `compas` with `pip`, it is highly recommended that you update `pip` itself.

```bash
$ ~/.rhinocode/py39-rh8/python3.9 -m pip install --upgrade pip
```

### Install from PyPI

For example, on Mac:

```bash
$ ~/.rhinocode/py39-rh8/python3.9 -m pip install compas
```

For example, on Windows:

```bash
$ ~/.rhinocode/py39-rh8/python.exe -m pip install compas
```

### Install from Source

```bash
$ cd path/to/compas
$ ~/.rhinocode/py39-rh8/python3.9 -m pip install -e .
```

### Verification

In Rhino 8, open the Python editor (just type ScriptEditor), open a new Python 3 editor tab, and type the following:

```python
import compas
print(compas.__version__)
```

If everything is installed correctly, this should print the version number of the installed COMPAS package.


