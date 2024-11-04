from flask import *
from database import *

user=Blueprint('user',__name__)

@user.route("/usr")
def usr():
     return render_template("user.html")