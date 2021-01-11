# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from urllib.parse import urljoin
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Next Gen Technical Best Practices'
copyright = '2021, Next Gen Architects'
author = 'Rahul Goel'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    "sphinx.ext.autosectionlabel",
    'sphinx.ext.autosummary',
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.imgconverter",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The master toctree document.
master_doc = "index"

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/overrides.css",
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/img/logo.jpg"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/img/logo.jpg"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "style_nav_header_background": "white",
    "navigation_depth": -1,
    "display_version": True
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``["localtoc.html", "relations.html", "sourcelink.html",
# "searchbox.html"]``.
#
html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "blueprintsdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    #
    # "papersize": "letterpaper",

    # The font size ("10pt", "11pt" or "12pt").
    #
    # "pointsize": "10pt",

    # Additional stuff for the LaTeX preamble.
    #
    # "preamble": "",

    # Latex figure (float) alignment
    #
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Docs-Template.tex",
        u"NeXtGen",
        u"Best Practices/Design Standards by NeXtGen Architects",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "docs-template",
        u"docs-template Documentation",
        [author],
        1,
    ),
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "docs-template",
        u"docs-template Documentation",
        author,
        "docs-template",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ""

# A unique identification for the text.
#
# epub_uid = ""

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------
# Display todo lists
todo_include_todos = False

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    "members": None,
}

# You can use the mock imports to include the dependencies of your API
# This is taken from hux-blueprints
autodoc_mock_imports = [
    "ujson",
    "pyspark",
    "mmh3",
    "xgboost",
    "pandas",
    "scikit-learn",
    "numpy",
    "sklearn"
]

# -- Options for autosummary -------------------------------------------------
autosummary_generate = True
autosummary_generate_overwrite = True


# -- Options for autosectionlabel --------------------------------------------

# Prefix each section label with the name of the document it is in
autosectionlabel_prefix_document = True
# Limit the depth that autogenerated refs are created for
autosectionlabel_maxdepth = 3


# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "xgboost": ("https://xgboost.readthedocs.io/en/stable/", None),
}


# -- Options for the linkcheck builder ---------------------------------------

linkcheck_retries = 5
linkcheck_timeout = 30  # seconds
linkcheck_workers = 30  # threads


def entire_domain(host):
    return r"http.?://" + re.escape(host) + r"($|/.*)"


linkcheck_ignore = [
    r"https://github.com/DeloitteHux/",
    r"https://.*\.mgnt-xspdev.in($|/.*)",
    r"http(s)?://localhost.*",
]


# -- Options for extlinks ----------------------------------------------------

extlinks = {
    k: (urljoin(url, "%s.html"), None)
    for k, (url, _) in intersphinx_mapping.items()
}
extlinks.update(
    github=("https://github.com/%s", None),
    hux=("https://github.com/DeloitteHux/%s", None),
    pypi=("https://pypi.org/project/%s/", None),
    python=("https://docs.python.org/3/%s", None),
    rtd=("https://%s.readthedocs.io", None),
    sentry=("https://docs.sentry.io/%s/?platform=python", None),
    wiki=("https://en.wikipedia.org/wiki/%s", None),
    youtube=("https://www.youtube.com/watch?v=%s", None),
)


# -- Options for sphinxcontrib-spelling --------------------------------------

spelling_word_list_filename = "spelling-wordlist.txt"