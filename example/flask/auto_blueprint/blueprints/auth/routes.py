from . import bp


@bp.route('/register', methods=['GET', 'POST'])
def register():
    ...


@bp.route('/', methods=['GET', 'POST'])
def login():
    ...


@bp.get('/logout')
def logout():
    ...
