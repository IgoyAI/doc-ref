# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx_rtd_theme

# If your project modules are in a different directory, you might need to
# add that directory to sys.path here. For example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'gm-docs-ref'
copyright = '2025, GM_TEAM, Yogi P.'
author = 'GM_TEAM, Yogi P.'
release = '0.0'

# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = []
language = 'english'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
