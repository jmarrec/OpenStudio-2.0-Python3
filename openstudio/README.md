## Placing the Files in the right folder

In This folder, place:

* all the source files (`.so`) from `./build/Products/python` (eg. `_openstudioairflow.so`)
* all the .py files from `./build/python_wrapper/generated_sources` (eg. `openstudioairflow.py`)

## Fixing the relative imports

Since Python3, implicit relative imports are no longer working. So there's a need to fix the default generated python files to have the right import (until OpenStudio fixes this - still an issue as of `OpenStudio 2.0.2`)

To do so, you can run `../fix_python3_imports.py` (root folder of this repo)

## Using the bindings

`cd ..` (to go to the root folder)


    $python
    
    >>> import openstudio
    >>> # Create a model, and add an AirLoopHVAC
    >>> m = openstudio.model.Model()
    >>> air_loop = openstudio.model.AirLoopHVAC(m)
    >>> # Set the design supply air flow rate to 10000 CFM
    >>> air_loop.setDesignSupplyAirFlowRate(openstudio.convert(10000, "CFM", "m^3/s").get())
