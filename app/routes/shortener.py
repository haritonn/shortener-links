from flask import Blueprint, render_template, request, flash, url_for, redirect
from app.database.redirect import generate_and_save_pair
from app.database.db import db, Links

app_bp = Blueprint("application", __name__)


# Generating original_url - short_url pair, returning short_url
@app_bp.route("/", methods=["GET", "POST"])
def generate_link():
    if request.method == "POST":
        original_url = request.form["original_url"]
        short_url, error = generate_and_save_pair(original_url)

        if error is not None:
            flash(error)
            return redirect("/application")

        return render_template(
            "application/index.html", short_url=f"{request.url_root}{short_url}"
        )

    return render_template("application/index.html")


# Redirecting from short_url to original_url
@app_bp.route("/<short_url>", methods=["GET"])
def redirect_to_original(short_url):
    try:
        original_url = (
            db.session.query(Links.original_url)
            .filter_by(shorter_url=short_url)
            .scalar()
        )
        return redirect(original_url)
    except Exception:
        error = "Link not found in database"
        flash(error)
        return redirect("/")
