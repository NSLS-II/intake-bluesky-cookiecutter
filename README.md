# Intake Bluesky Cookiecutter

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating
a suitcase subpackage.

See the [intake-bluesky documentation](https://nsls-ii.github.io/intake-bluesky).


After cookiecutting your intake-bluesky subproject, you should:

* Create a repo and put it there.
* Add the repo to your <a href="https://travis-ci.org/">Travis-CI</a> account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Release your package by pushing a new tag to master.
