from flask import Blueprint, render_template, request, flash, url_for, redirect
from app.utils import url_utils
from app.database import db

app_bp = Blueprint("application", __name__, url_prefix="application")


# Generating original_url - short_url pair, returning short_url
@app_bp.route("/", methods=["GET", "POST"])
def generate_link():
    if request.method == "POST":
        original_url = request.form["original_url"]


# Redirecting from short_url to original_url
@app_bp.route("/<short_url>", methods="POST")
def redirect_to_original(short_url):
    pass
