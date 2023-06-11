from setuptools import setup, find_packages

setup(
    name="notio_-api",
    version="0.0.1",
    author="ik-y",
    packages=find_packages(),
    install_requires=["requests", "datetime"],
    include_package_data=True,
)
