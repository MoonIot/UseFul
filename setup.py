import os
from platform import python_revision

from setuptools import setup


def read_requirements() -> list:
    with open("requirements.txt", "r") as req_file:
        return list(map(lambda x: x.strip(), req_file.readlines()))


def read_package(package_name: str) -> list:
    packages = [package_name, ]
    ignore_file = '__pycache__'

    base_dir = os.path.abspath(os.path.dirname(__file__))
    package_dir = os.path.join(base_dir, package_name)

    def validate_package(pkg: str) -> bool:
        try:
            roots = tuple(os.walk(os.path.join(package_dir, pkg)))
            return '__init__.py' in roots[0][2]
        except IndexError:
            return False

    def read_sub_package(source_pkg: str, pkg: str) -> None:
        try:
            if len(source_pkg.split('.')) > 2:
                pkg_dir = source_pkg.split('.')[1:]
                pkg_dir = '/'.join(pkg_dir)
            else:
                pkg_dir = pkg
            roots = tuple(os.walk(os.path.join(package_dir, pkg_dir)))[0]
        except IndexError:
            return

        for sub_pkg in filter(lambda x: x != ignore_file, roots[1]):
            pkg_dir = source_pkg.split('.')[1:]
            pkg_dir.append(sub_pkg)
            pkg_dir = '/'.join(pkg_dir)

            if validate_package(pkg_dir):
                packages.append(f"{source_pkg}.{sub_pkg}")
                read_sub_package(f"{source_pkg}.{sub_pkg}", sub_pkg)

    roots = tuple(os.walk(package_name))[0]

    for pkg in filter(lambda x: x != ignore_file, roots[1]):
        if validate_package(pkg):
            packages.append(f"{package_name}.{pkg}")
            read_sub_package(f"{package_name}.{pkg}", pkg)

    return packages


setup(
    name="useful",
    version="0.2.0",
    author="dot1mav",
    author_email="dot1mav@gmail.com",
    url="https://github.com/dot1mav/UseFul",
    packages=read_package("UseFul"),
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires='>=3.8',
)
