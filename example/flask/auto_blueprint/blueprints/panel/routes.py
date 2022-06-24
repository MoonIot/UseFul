from . import bp


@bp.get('/')
@bp.get('/index')
def index():
    ...
