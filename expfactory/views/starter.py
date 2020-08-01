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

starter = Blueprint('starter', __name__,
                                static_url_path='/experiments/starter',
                                static_folder='/scif/apps/starter',
                                template_folder='/scif/apps')

@starter.route('/experiments/starter/')
def starter_base():
    context = {'experiment': 'starter/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="starter")

starter.before_request(csrf.protect)
app.register_blueprint(starter)

