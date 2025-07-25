from flask import Blueprint, render_template, request, flash, url_for, redirect
from app.database.auth import registration_user, login_username, login_password
from flask_login import login_required, logout_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# registration handler
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        # simple checks
        if not username:
            error = "Username is required"
            flash(error)
            return redirect(url_for("auth.register"))
        elif not password:
            error = "Password is required"
            flash(error)
            return redirect(url_for("auth.register"))

        # registration functions
        error = registration_user(username, password, error)
        if error is None:
            return redirect(url_for("auth.login"))

        flash(error)
        return redirect(url_for("auth.register"))

    return render_template("auth/register.html")


# login handler
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        # simple checks
        if not username:
            error = "Username is required"
        if not password:
            error = "Password is required"

        # login functions
        if not login_username(username):
            error = f"User {username} not found"
            flash(error)
            return redirect(url_for("auth.login"))

        if not login_password(username, password):
            error = "Incorrect password"
            flash(error)
            return redirect(url_for("auth.login"))

        if error is None:
            return redirect("/")

    return render_template("auth/login.html")


# logout handler
@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
