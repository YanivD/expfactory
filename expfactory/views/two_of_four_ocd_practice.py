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

two_of_four_ocd_practice = Blueprint('two_of_four_ocd_practice', __name__,
                                static_url_path='/experiments/two_of_four_ocd_practice',
                                static_folder='/scif/apps/two_of_four_ocd_practice',
                                template_folder='/scif/apps')

@two_of_four_ocd_practice.route('/experiments/two_of_four_ocd_practice/')
def two_of_four_ocd_practice_base():
    context = {'experiment': 'two_of_four_ocd_practice/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="two_of_four_ocd_practice")

two_of_four_ocd_practice.before_request(csrf.protect)
app.register_blueprint(two_of_four_ocd_practice)

