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

two_of_four_ocd = Blueprint('spq', __name__,
                                static_url_path='/experiments/spq',
                                static_folder='/scif/apps/spq',
                                template_folder='/scif/apps')

@two_of_four_ocd.route('/experiments/spq/')
def two_of_four_ocd_base():
    context = {'experiment': 'spq/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="spq")

two_of_four_ocd.before_request(csrf.protect)
app.register_blueprint(two_of_four_ocd)

