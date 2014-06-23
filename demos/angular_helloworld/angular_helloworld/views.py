from pyramid.view import view_config
from .models import MyModel

@view_config(context=MyModel, renderer="templates/home.jinja2")
def my_view(request):
    return {'project':'angular_helloworld'}
