from os import path, listdir
from flask import Flask
from importlib import import_module
from typing import Optional


class AutoBlueprint:
    _app: Flask
    _package_name: str
    _file_path: str
    _blueprint_path: str

    def __init__(self, package_name: str, file_path: str, app: Optional[Flask] = None,
                 blueprint_path: str = 'blueprints') -> None:
        self._package_name = package_name
        self._file_path = path.abspath(path.dirname(file_path))
        self._blueprint_path = blueprint_path

        if app:
            self.init_app(app)

    def init_app(self, app: Flask, *, load_blueprints: bool = False) -> None:
        self._app = app
        
        if load_blueprints:
            self._read_from_blueprint()

    def load_blueprints(self) -> None:
        self._read_from_blueprint()

    def _read_from_blueprint(self) -> None:
        ignore = ['__pycache__']

        for bp_module in listdir(path.join(self._file_path, self._blueprint_path)):
            bp_dir = path.join(self._file_path, self._blueprint_path, bp_module)
            if bp_module not in ignore and path.isdir(bp_dir):
                module = import_module(f'.{bp_module}', f'{self._package_name}.{self._blueprint_path}')
                if "bp" in dir(module):
                    self._app.register_blueprint(module.bp)
