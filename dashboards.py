from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from app_default.app import app as default_app

import dash

from app_one.app import app as one_app
from app_two.app import app as two_app

multiple_apps = DispatcherMiddleware(default_app,
    {
        '/one': one_app.server,
        '/two': two_app.server,
    }
)

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=8050,
        application=multiple_apps,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True
    )
