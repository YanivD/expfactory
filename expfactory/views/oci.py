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

oci = Blueprint('oci', __name__,
                                static_url_path='/experiments/oci',
                                static_folder='/scif/apps/oci',
                                template_folder='/scif/apps')

@oci.route('/experiments/oci/')
def oci_base():
    context = {'experiment': 'oci/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="oci")

oci.before_request(csrf.protect)
app.register_blueprint(oci)

