from setuptools import setup, find_packages

setup(
    name="proyecto_bigdata_ingesta",
    version="1.0.0",
    description="Etapa de ingesta del proyecto integrador de Big Data",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31",
        "pandas>=2.0",
        "openpyxl>=3.1",
    ],
)
