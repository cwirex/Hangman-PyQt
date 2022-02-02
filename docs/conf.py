import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# update modules:  sphinx-apidoc -o . ..
# create html: .\make.bat html

# -- Project information -----------------------------------------------------

project = 'Hangman'
copyright = '2022, Mateusz Ocwieja'
author = 'Mateusz Ocwieja'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']