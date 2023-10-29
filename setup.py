from setuptools import find_packages, setup

setup(
    name="Idempotent-Requests",
    version="0.0.1",
    description="Flask app for idempotent requests",
    packages = find_packages(exclude=["*.tests"]),
     include_packages_data = True,
    install_requires = [
        "Flask==3.0.0",
        "pydantic==2.4.2"
    ]
)