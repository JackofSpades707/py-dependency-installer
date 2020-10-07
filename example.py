from dependency_installer import dependency_installer

dependency_installer() 
# This will read the scripts import statements
# and check if imports are working
# if imports fail, it will pip install imports
# before the imports are called in the script

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

