from flask import Blueprint

hyperlinks = Blueprint('hyperlinks', __name__,
                    template_folder='templates',
                    static_folder='static')


from . import views
