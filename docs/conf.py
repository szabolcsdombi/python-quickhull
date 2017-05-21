#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sphinx_rtd_theme

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinxcontrib.napoleon']
templates_path = ['templates']

source_suffix = '.rst'
master_doc = 'index'

project = 'QuickHull'
copyright = '2017, Szabolcs Dombi'
author = 'Szabolcs Dombi'

version = '0.9.0'
release = '0.9.0'

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'
todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['static']
htmlhelp_basename = 'QuickHulldoc'

latex_elements = {}

latex_documents = [
    (master_doc, 'QuickHull.tex', 'QuickHull Documentation', 'Szabolcs Dombi', 'manual'),
]

man_pages = [
    (master_doc, 'QuickHull', 'QuickHull Documentation', [author], 1)
]

texinfo_documents = [
    (master_doc, 'QuickHull', 'QuickHull Documentation', author, 'QuickHull', 'One line description of project.', 'Miscellaneous'),
]

autodoc_member_order = 'bysource'
# autodoc_member_order = 'groupwise'
add_module_names = False

def setup(app):
    app.add_stylesheet('css/custom.css')
