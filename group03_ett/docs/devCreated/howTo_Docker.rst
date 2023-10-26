How to - Docker
===============

Basics
------

Docker uses Containers based on Images to compartmentalize the executable Code. This makes sure, that every Operating System that executes the same Code will get the same result.

We will use Docker in Order to make sure that our Application always has the right dependencies loaded and will work independently from possible other installations of e. g. Python (like Python2) or libaries like Numpy.

Structure
---------

In Order for our Project to work, we want to seperate the different services we need into multiple containers that all only satisfy a specific purpose.

For this we use the same base image to reduce the things one needs to download.::

    Webserver                                        Number Crunching

    debian:buster-slim --------------------------------------
            |                                               |
            v                                               |
    httpd (docker community image)                          |
            |                                               |
            v                                               v
    Display Website (Interface & Documentation)      Run Python/Flask
    localhost:8080                                   localhost:8081

As one can see, both services require ``debain:buster-slim`` but the webserver additionally loads the ``httpd`` Image from the offical Docker Community Repository which saves us the time to set up a complete webserver and instead we can simply use this one.

Building
--------

From the base images, this project builds its own images that then can be used in the containers needed in the end. To build the necessary images, the project makes use of the docker compose tool which can be invoked by  using ``docker-compose build``.


Installation
------------

As Docker is cross-platform compatible, one simply has to install the docker platfrom in Order to run this Project. Then, once downloaded, the project makes use of ``docker-compose up`` in order to start and stop the different container.

It is important to remember, that once the container is started, one has to shut it down again by first exiting out of the Command Prompt with ``Ctrl + C`` and then by typing ``docker-compose down``. This will make sure to free system resources.