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

bdi = Blueprint('bdi', __name__,
                                static_url_path='/experiments/bdi',
                                static_folder='/scif/apps/bdi',
                                template_folder='/scif/apps')

@bdi.route('/experiments/bdi/')
def bdi_base():
    context = {'experiment': 'bdi/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="bdi")

bdi.before_request(csrf.protect)
app.register_blueprint(bdi)

