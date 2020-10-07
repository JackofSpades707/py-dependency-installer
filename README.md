# py-dependency-installer

## example
```
from dependency_installer import dependency_installer

dependency_installer() 

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
```

## dependency_installer([path])
* `dependency_installer()` will read the script that calls the function, parses all import/from statements, verifies all import statements, and if any imports fail, it will pip install them automatically for you. (it does this by calling `pip_import`)
* optional `path` argument to specify an external file to process imports from

## pip_import(module, [global_imports, verbose_output])
* This will attempt to import the `module` variable
* If the import statement fails, it will automatically pip install the module for you
* if optional `global_imports` is set to True (false by default) it will import the module globally (the same as a normal import statement)
* if optional `verbose_output` is set to True (false by default) it will print pips output to the console/terminal
