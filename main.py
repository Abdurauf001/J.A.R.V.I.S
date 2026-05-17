import json


def app(environ, start_response):
    """Small WSGI entrypoint for Vercel deployments."""
    payload = {
        "name": "J.A.R.V.I.S",
        "status": "online",
        "message": "JARVIS desktop assistant code is in desktop_main.py.",
    }
    body = json.dumps(payload).encode("utf-8")

    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]


application = app


if __name__ == "__main__":
    from desktop_main import main as run_desktop

    run_desktop()
