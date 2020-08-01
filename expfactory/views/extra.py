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

extra = Blueprint('extra', __name__,
                                static_url_path='/experiments/extra',
                                static_folder='/scif/apps/extra',
                                template_folder='/scif/apps')

@extra.route('/experiments/extra/')
def extra_base():
    context = {'experiment': 'extra/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="extra")

extra.before_request(csrf.protect)
app.register_blueprint(extra)

