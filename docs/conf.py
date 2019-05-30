#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GluonTS documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 19 15:29:41 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import sys
import os, subprocess
import shlex
import recommonmark
import sphinx_gallery
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
curr_path = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
sys.path.insert(0, os.path.join(curr_path, '..'))


# -- General configuration ------------------------------------------------

# Version information.
import gluonts as ts
version = ts.__version__
release = ts.__version__

# General information about the project.
project = 'GluonTS'
copyright = '2018, Amazon'
author = 'Amazon'
github_doc_root = 'http://gluon-ts.mxnet.io/{}/'.format(str(version))

# add markdown parser
CommonMarkParser.github_doc_root = github_doc_root
source_parsers = {
    '.md': CommonMarkParser
}

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx_autorun',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

nbsphinx_kernel_name = 'python3'
nbsphinx_allow_errors = True
nbsphinx_timeout = 1200
html_sourcelink_suffix = ''

html_context = {
    'display_github': True,
    'github_user': 'awslabs',
    'github_repo': 'gluon-ts',
    'github_version': 'master',
    'conf_py_path': '/docs/',
    'last_updated': False,
    'commit': True
}

nbsphinx_prolog = """
{% set paths = env.docname.split('/') %}

.. only:: html

    :download:`[Download] <{{ "../%s.zip"|format(paths[1]) }}>`
"""
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.ipynb', '.md']

# generate autosummary even if no references
autosummary_generate = True

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/gluon-logo.svg'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/gluon.ico'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'examples/*/*/**.rst', 'model_zoo/*/*/**.rst',
                    'model_zoo/word_embeddings/tools/extern/*/**.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'mxtheme'
html_theme_path = ['mxtheme']
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links' : [
        ('Install', 'install', False, ''),
        ('API', 'api/index', False, ''),
        ('Community', 'community/index', False, ''),
        ('Contribute', 'community/contribute', False, ''),
        ('GitHub', 'https://github.com/awslabs/gluon-ts/', True, 'fab fa-github'),
    ],

    # custom layout
    'fixed_drawer' : True,
    'fixed_header' : True,
    'header_waterfall' : True,
    'header_scroll': True,

    # Render footer (Default: True)
    'show_footer': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'GluonTSdoc'


# -- Options for LaTeX output ---------------------------------------------

# latex_elements = {
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'GluonTS.tex', 'GluonTS Documentation', 'Amazon', 'manual')
# ]

intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'mxnet': ('https://mxnet.apache.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('http://matplotlib.org/', None),
}

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'gluonts', 'GluonTS Documentation', [author], 1)]

from sphinx_gallery.sorting import ExplicitOrder

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'GluonTS',
        'GluonTS Documentation',
        author,
        'GluonTS',
        'One line description of project.',
        'Miscellaneous',
    )
]

def setup(app):
    import mxtheme
    app.add_directive('card', mxtheme.CardDirective)

    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_doc_ref': True
            }, True)
    app.add_transform(AutoStructify)
    app.add_javascript('google_analytics.js')


sphinx_gallery_conf = {
    'backreferences_dir': 'gen_modules/backreferences',
    'doc_module': ('gluonts', 'mxnet', 'numpy'),
'reference_url': {
    'gluonts': None,
    'numpy': 'http://docs.scipy.org/doc/numpy-1.9.1'},
    'examples_dirs': [],
    'gallery_dirs': [],
    'subsection_order': ExplicitOrder([]),
    'find_mayavi_figures': False,
    'filename_pattern': '.py',
    'expected_failing_examples': []
}

# Napoleon settings
napoleon_use_ivar = True

# linkcheck settings
import multiprocessing
linkcheck_ignore = [r'http[s]://apache-mxnet.s3*']
linkcheck_retries = 3
linkcheck_workers = int(multiprocessing.cpu_count() / 2)