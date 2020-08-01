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

teacher_practice = Blueprint('teacher_practice', __name__,
                                static_url_path='/experiments/teacher_practice',
                                static_folder='/scif/apps/teacher_practice',
                                template_folder='/scif/apps')

@teacher_practice.route('/experiments/teacher_practice/')
def teacher_practice_base():
    context = {'experiment': 'teacher_practice/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="teacher_practice")

teacher_practice.before_request(csrf.protect)
app.register_blueprint(teacher_practice)

