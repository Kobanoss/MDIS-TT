from flask import Blueprint, render_template
from requests import post
from application.routes.__imports__ import *

views = Blueprint('views', __name__)


@views.route("/", methods=['GET', 'POST'])
async def home():
    form = DataForm()
    if form.validate_on_submit():
        await requests.post(API_URL, form.jsonsify())

    return render_template('home.html', form=form)