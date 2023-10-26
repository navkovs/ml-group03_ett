How to - Add Python Requirements to the project
===============================================

To keep the project dependencies to itself, they will be installed into a docker container. The container then should work platform independent.

In Order to manage dependencies, the project will make use of `Poetry`_, a Python dependency management system.

To add additional dependencies into the project, one must add the intended requirement to the ``pyproject.toml`` file  in the ``[tool.poetry.dependencies]`` Category and once again use ``make build``. This will then include the requirements.

Alternatively, one can also use ``poetry add PACKAGE_NAME`` to add a package.

To remove a package again, use ``poetry remove PACKAGE_NAME``.

.. _Poetry: https://python-poetry.org/