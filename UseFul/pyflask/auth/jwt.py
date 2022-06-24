from .base import BaseApi
from flask import Response, request


class JwtApi(BaseApi):
    def before_request(self) -> None:
        print(request)

    def after_request(self, response: Response) -> Response:
        print(response)
        return super(JwtApi, self).after_request(response)
