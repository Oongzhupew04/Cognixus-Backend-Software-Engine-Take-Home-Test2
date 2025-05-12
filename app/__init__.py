from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.contrib.github import make_github_blueprint
from flask_dance.contrib.facebook import make_facebook_blueprint
import os

file_path = os.path.abspath(os.getcwd())+"/todo.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


google_bp = make_google_blueprint(
    client_id="261395564675-6ljhvh2mk0r0s19lu9fgj0tjs8vvrjc8.apps.googleusercontent.com",
    client_secret="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",
    redirect_to="google_login",
    scope=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]
)
facebook_bp = make_facebook_blueprint(
    client_id="539202525925799",
    client_secret="73b4ea4b753d1f553bc681fc0e058662",
    redirect_to="facebook_login"
)
github_bp = make_github_blueprint(
    client_id="Ov23linshJXIEsSRwcwU",
    client_secret="1fc23f0e1d2a3a7f56494f399dd70dc9ec9904da",
    redirect_to="github_login",
    scope="read:user,user:email"
)

app.register_blueprint(google_bp, url_prefix="/google_login")
app.register_blueprint(facebook_bp, url_prefix="/facebook_login")
app.register_blueprint(github_bp, url_prefix="/github_login")


from app import routes, models
