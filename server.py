from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path

app = Flask(__name__)

STATIC_DIR = Path(app.root_path) / "static"
TEMPLATES_DIR = Path(app.root_path) / "templates"


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(STATIC_DIR, "favicon.ico", mimetype="image/x-icon")


@app.route("/submit_contact_form", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def submit_form_gone():
    """Contact form UI is hidden; endpoint retired (no CSV / SMTP)."""
    abort(410)


@app.route("/<string:page_name>")
def html_page(page_name):
    # Only serve real HTML templates; avoid 500s for missing assets like favicon.
    if not page_name.endswith(".html"):
        abort(404)
    template_path = TEMPLATES_DIR / page_name
    if not template_path.is_file():
        abort(404)
    return render_template(page_name)
