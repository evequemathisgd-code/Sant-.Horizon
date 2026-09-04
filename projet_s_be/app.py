from flask import Flask, render_template
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "clé-temporaire-locale"
)

@app.after_request
def add_security_headers(response):
    headers = {
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    }

    for key, value in headers.items():
        response.headers[key] = value

    response.headers["Content-Security-Policy"] = (
        "default-src 'self';"
        "script-src 'self';"
        "style-src 'self';"
        "img-src 'self' data:;"
        "font-src 'self';"
        "connect-src 'self';"
        "object-src 'none';"
        "base-uri 'self';"
        "frame-ancestors 'none';"
        "form-action 'self';"
        "upgrade-insecure-requests;"
    )

    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/philosophie")
def philosophie():
    return render_template("philosophie.html")

@app.route("/massage-californien")
def massage_californien():
    return render_template("massage_californien.html")

@app.route("/massage-ayurvedique")
def massage_ayurvedique():
    return render_template("massage_ayurvedique.html")

@app.route("/mentions-legales")
def mentions_legales():
    return render_template("mentions_legales.html")

@app.route("/confidentialite")
def confidentialite():
    return render_template("confidentialite.html")

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning(f"404 : {error}")
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=False)
