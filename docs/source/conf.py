# Configuration file for the Sphinx documentation builder.
import os
import sys

sys.path.insert(0, os.path.abspath('../../'))  # ensure that can find smart package

import smart


# -- Project information

project = 'SMART'
copyright = '2025, Chen Qiyi'
author = 'Chen Qiyi'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    "sphinx.ext.napoleon", 
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'nbsphinx'
]

# -- Mock the package that is hard to install in the RTD environment.
autodoc_mock_imports =[
    "torch",                
    "torch_geometric",     
    "scanpy",               
    "muon",                 
    "harmony",             
    "rpy2",                
    "numba",                
    "scikit-learn",         
    "matplotlib",           
    "pandas",               
    "numpy",                
    "lumache",              
]

autosummary_generate = True
autodoc_typehints = "description"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


source_suffix = '.rst'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
