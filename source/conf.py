project = "Stonecharioteer's Writing"
copyright = "2021, Vinay Keerthi"
author = "Vinay Keerthi"
extensions = [
    "sphinx.ext.todo",
    "sphinx_design",
    "sphinx.ext.githubpages",
]
templates_path = ["_templates"]
exclude_patterns = []
html_theme = "furo"
html_title = "Stonecharioteer's Writing"
serif_fonts = "Newsreader, Garamond, Helvetica, Times New Roman, Serif"
html_theme_options = {
    "light_css_variables": {
        "font-stack": serif_fonts,
    },
    "dark_css_variables": {
        "font-stack": serif_fonts,
    },
}
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_last_updated_fmt = ""
todo_include_todos = True
html_show_sphinx = False
