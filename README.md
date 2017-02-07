# OpenStudio-2.0-Python3
How to building OpenStudio 2.0 on Mac, and get the Python 3 bindings to work

## Building OpenStudio 2.0.2 on Mac

There is a specific README file: [Building_OS2.0_on_Mac](Building_OS2.0_on_Mac.md)

## Building the Python 3 bindings, and making them work

### In CCMake

(Still building `./openstudiocore/`)

After enabling `BUILD_PYTHON_BINDINGS=ON` then configuring (`[c]`), enabling advanced mode (`[t]`).

I've pointed the python variables to my Python 3.5 virtual environment:

    //Path to a program.
    PYTHON_EXECUTABLE:FILEPATH=/Users/julien/Virtualenvs/py35/bin/python
    
    //Path to a file.
    PYTHON_INCLUDE_DIR:PATH=/Users/julien/Virtualenvs/py35/include/python3.5m
    
    //Path to a library.
    PYTHON_LIBRARY:FILEPATH=/Users/julien/Virtualenvs/py35/lib/python3.5/config-3.5m/libpython3.5.dylib
    
    //Path to a library.
    PYTHON_LIBRARY_DEBUG:FILEPATH=PYTHON_LIBRARY_DEBUG-NOTFOUND

Configure, then generate (`[g]`).

`make -j XX` where XX = number of cores. This will generate the bindings.

### Making them work

There's a problem with the relative imports not working anymore in python 3, and I also provide an `__init__.py` file that should most ressemble the Ruby (official) bindings.

Please refer to the [openstudio/README.md](openstudio/README.md) for more information.
