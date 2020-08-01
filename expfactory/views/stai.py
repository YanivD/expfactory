from expfactory.logger import bot

from flask import (
    Blueprint,
    render_template,
)
from expfactory.views.utils import (
    perform_checks,
    clear_session
)
from expfactory.server import app, csrf
import os

stai = Blueprint('stai', __name__,
                                static_url_path='/experiments/stai',
                                static_folder='/scif/apps/stai',
                                template_folder='/scif/apps')

@stai.route('/experiments/stai/')
def stai_base():
    context = {'experiment': 'stai/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="stai")

stai.before_request(csrf.protect)
app.register_blueprint(stai)

