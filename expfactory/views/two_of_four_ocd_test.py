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

two_of_four_ocd_test = Blueprint('two_of_four_ocd_test', __name__,
                                static_url_path='/experiments/two_of_four_ocd_test',
                                static_folder='/scif/apps/two_of_four_ocd_test',
                                template_folder='/scif/apps')

@two_of_four_ocd_test.route('/experiments/two_of_four_ocd_test/')
def two_of_four_ocd_test_base():
    context = {'experiment': 'two_of_four_ocd_test/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="two_of_four_ocd_test")

two_of_four_ocd_test.before_request(csrf.protect)
app.register_blueprint(two_of_four_ocd_test)

