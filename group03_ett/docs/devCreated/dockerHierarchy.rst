Docker Container Hierarchy
==========================

- httpd [webserver] for hosting the webinterface

    - Mounts volumes to:

        - ``./html`` - webinterface
        - ``./docs/_build/html`` - documentation

        - This is probably a bad idea and maybe the storage should be its own container.

- debian:buster [base] for Python Code Execution

