from setuptools import setup, find_packages
import os

version = '1.0.0'

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

setup(
    name='dashboard_app',
    version=version,
    description='Dashboard App',
    author='Frappe',
    author_email='baljeet@ameotech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
