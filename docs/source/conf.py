# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Moodle Proctoring Plugin - User Guide'
copyright = '2025, Take2 Technologies'
author = 'Yogesh Sharma'

release = '4.2.9'
version = '4.2.9'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Custome CSS
html_static_path = ['_source']
html_css_files = ['custom.css']
