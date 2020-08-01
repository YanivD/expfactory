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

teacher_starter = Blueprint('teacher_starter', __name__,
                                static_url_path='/experiments/teacher_starter',
                                static_folder='/scif/apps/teacher_starter',
                                template_folder='/scif/apps')

@teacher_starter.route('/experiments/teacher_starter/')
def teacher_starter_base():
    context = {'experiment': 'teacher_starter/index.html'}
    return perform_checks('experiments/experiment.html', quiet=True,
                                                         context=context,
                                                         next="teacher_starter")

teacher_starter.before_request(csrf.protect)
app.register_blueprint(teacher_starter)

