from flask import Blueprint, render_template, request, flash, url_for, redirect

app_bp = Blueprint("application", __name__)


@app_bp.route("/application", methods=["GET", "POST"])
def generate_link():
    if request.method == "POST":
        link = request.form["original_url"]
        # generate_shorter_link...
