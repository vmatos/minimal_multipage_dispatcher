# To reproduce the issue

The two apps run individually.

```
$ python app_one/app.py
```

or

```
$ python app_two/app.py
```


However do not run when imported from a module. Example: when running through `DispatcherMiddleware`.

```
$ python dashboards.py

Traceback (most recent call last):
  File "dashboards.py", line 5, in <module>
    from app_one.app import app as one_app
  File "/home/vmatos/experiments/minimal_multipage_dispatcher/app_one/app.py", line 10, in <module>
    app = Dash(__name__, plugins=[dl.plugins.pages], requests_pathname_prefix=requests_pathname_prefix)
  File "/home/vmatos/experiments/minimal_multipage_dispatcher/venv/lib/python3.8/site-packages/dash/dash.py", line 458, in __init__
    plugin.plug(self)
  File "/home/vmatos/experiments/minimal_multipage_dispatcher/venv/lib/python3.8/site-packages/dash_labs/plugins/pages.py", line 321, in plug
    _import_layouts_from_pages(pages_folder)
  File "/home/vmatos/experiments/minimal_multipage_dispatcher/venv/lib/python3.8/site-packages/dash_labs/plugins/pages.py", line 295, in _import_layouts_from_pages
    page_module = importlib.import_module(f"pages.{page_filename}")
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named 'pages'
```