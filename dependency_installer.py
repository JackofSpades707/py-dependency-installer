#!/usr/bin/env python

import os
import re
import subprocess

def dependency_installer(path=None):
    def parse_module_name(import_statement):
        return import_statement.replace('import ', '').replace('from ', '')
    if path is None:
        path = __file__ # if path is None, we use the script calling the function
    with open(os.path.abspath(path)) as f:
        fd = f.read()
    modules = []
    regex = r"(?m)^(import [a-zA-Z0-9]+|^from [a-zA-Z0-9]+)"
    import_statements = re.findall(regex, fd)
    for import_statement in import_statements:
        modules.append(parse_module_name(import_statement))
    modules = list(set(modules))
    for module in modules:
        if f"{module}.py" not in os.listdir() or module not in os.listdir():
            # Check to see if module exists locally, if so, do not pip import module
            pip_import(module)

def pip_import(module, global_imports=False, verbose_output=False):
    try:
        if global_imports:
            exec(f"import {module}", globals())
        else:
            exec(f"import {module}")
    except ImportError:
        output = subprocess.Popen(f"python -m pip install {module}".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if "Successfully installed" in output[0].decode('utf-8'):
            if verbose_output:
                print(output[0].decode('utf-8'))
            print(f'[+] Installed {module}')
            if global_imports:
                pip_import(module)
        elif "ERROR" in output[1].decode('utf-8'):
            if verbose_output:
                print(output[1].decode('utf-8'))
            raise SystemExit(f"[-] Failed to install {module}")
        else:
            print("[?] Unknown Output")
            for i in output:
                print(i.decode('utf-8'))
