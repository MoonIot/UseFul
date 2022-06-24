from abc import ABC, abstractmethod
from flask import Flask, Blueprint, Response
from flask_restful import Api, Resource
from typing import Optional, Type


class BaseApi(ABC):
    _app: Flask
    _bp: Blueprint
    _api: Api
    _version: str
    _secret: str

    def __init__(self, app: Optional[Flask] = None, version: str = '0'):
        if not isinstance(version, str):
            raise TypeError('version type should be string like \'0.1.0\' or \'0.1.0~beta\'')

        if len(version.split('.')) != 3:
            raise ValueError('version string should like \'0.1.0\' or \'0.1.0~beta\'')

        for x in version.split('.'):
            if '~' in x:
                x = x.split('~')[0]
            if not x.isdigit():
                raise ValueError('version string should like \'0.1.0\' or \'0.1.0~beta\'')

        self._version = version

        self._make_api()

        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        if "secret_key" not in app.config:
            raise ValueError("you're app doesn't have secret_key")

        self._app = app

        self._app.register_blueprint(self._bp)

        self._secret = self._app.config["secret_key"]

    def add_api(self, cls, *url, **kwargs) -> None:
        def set_api(cls_=None):
            if not url and not cls.__url__:
                raise ValueError(f"url not defined for {cls_}")
            self._api.add_resource(cls_, url if url else cls_.__url__, **kwargs)

        if cls is None:
            return set_api
        return set_api(cls)

    def _make_api(self):
        self._bp = Blueprint('api', __name__, url_prefix=f'/api')

        self._bp.before_request(self.before_request)
        self._bp.after_request(self.after_request)

        self._api = Api(self._bp)

        self.ApiResource: Type[Resource] = Resource

    @abstractmethod
    def before_request(self) -> None:
        ...

    @abstractmethod
    def after_request(self, response: Response) -> Response:

        return response
