from dash import Dash, html, dcc
import dash
import dash_labs as dl
from flask import Flask

if __name__ == '__main__':
    requests_pathname_prefix=None
else:
    requests_pathname_prefix='/one/'

server = Flask(__name__)
app = Dash(__name__, server=server, plugins=[dl.plugins.pages], requests_pathname_prefix=requests_pathname_prefix)

dash.register_page("another_home", layout=html.Div("App 1!"), path="/")
dash.register_page(
    "very_important", layout=html.Div("Don't miss it!"), path="/important", order=0
)

app.layout = html.Div(
    [
        html.H1("App Frame"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']} - {page['path']}", href=page["path"])
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
