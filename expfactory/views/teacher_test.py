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

teacher_test = Blueprint('teacher_test', __name__,
                                static_url_path='/experiments/teacher_test',
                                static_folder='/scif/apps/teacher_test',
                                template_folder='/scif/apps')

@teacher_test.route('/experiments/teacher_test/')
def teacher_test_base():
    context = {'experiment': 'teacher_test/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="teacher_test")

teacher_test.before_request(csrf.protect)
app.register_blueprint(teacher_test)

