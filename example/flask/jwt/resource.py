from . import api


class User(api.ApiResource):
    __url__ = '/user'

    def get(self):
        return {}


@api.add_api
class Posts(api.ApiResource):
    __url__ = '/post'

    def get(self):
        return {}
