# Louis Liao — Portfolio

Simple Flask portfolio site (Colorlib Unfold template).

## Local run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app server run --debug
```

Open http://127.0.0.1:5000/

Production-style locally:

```bash
gunicorn server:app
```

## Deploy (Zeabur)

- App entry: `gunicorn server:app` (see `Procfile`)
- Install deps from `requirements.txt`
- Live: https://louisliao.zeabur.app/

## Notes

- Contact form UI is hidden; `/submit_contact_form` returns 410 and does not store or email submissions.
- Do not commit secrets (`pw/`, `.env`, credentials).

## Template source

- https://themewagon.com/themes/free-bootstrap-4-html5-responsive-portfolio-website-template-unfold/
