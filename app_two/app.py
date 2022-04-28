from dash import Dash, html, dcc
import dash
import dash_labs as dl
from flask import Flask

import os
current_module_path = os.path.dirname(os.path.realpath(__file__))

import sys
if current_module_path not in sys.path:
    sys.path.append(current_module_path)

if __name__ == '__main__':
    requests_pathname_prefix=None
else:
    requests_pathname_prefix='/two/'

print('\nBefore App 2', __name__)
for page in dash.page_registry.values():
    print(page)

server = Flask(__name__)
# When pluging itself, is removing the registered pages?
app = Dash(__name__, server=server, plugins=[dl.plugins.pages], requests_pathname_prefix=requests_pathname_prefix)

print('\nBefore App 2 register page')
for page in dash.page_registry.values():
    print(page)

dash.register_page(__name__+".another_home", layout=html.Div("App 2!"), path='/')
dash.register_page(
    __name__+".very_important", layout=html.Div("Don't miss it! 2"), path="/important", order=0
)

print('\nAfter App 2')
for page in dash.page_registry.values():
    print(page)

app.layout = html.Div(
    [
        html.H1("App 2 Frame"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']} - {page['path']}", href=requests_pathname_prefix[:-1]+page["path"])
                )
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ]
        ),
        dl.plugins.page_container,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

if current_module_path in sys.path:
    sys.path.remove(current_module_path)
