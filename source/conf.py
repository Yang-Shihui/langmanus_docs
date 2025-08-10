# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LangManus'
copyright = '2025, yang shihui'
author = 'yang shihui'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# 'myst_parser',          # 支持 Markdown
#     'sphinx.ext.autodoc',   # 自动生成 API 文档
#     'sphinx.ext.viewcode',  # 显示源码链接
extensions = [
    'myst_parser',          # 支持 Markdown
    'sphinx.ext.autodoc',   # 自动生成 API 文档
    'sphinx.ext.viewcode',  # 显示源码链接
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
