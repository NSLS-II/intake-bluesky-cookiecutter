from setuptools import setup
import versioneer


setup(
    name='suitcase-{{ cookiecutter.subpackage_name }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['suitcase.suitcase_{{ cookiecutter.subpackage_name }}']
)
