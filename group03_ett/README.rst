Estimated Travel Time - Group 03
================================

.. image:: /devCreated/images/screenshot00.jpg
    :width: 600
    :alt:
    :align: center

This tool can tell you based on the inputs given to it, how long a ship will take to travel from Rotterdam to Hamburg or from Kiel to Gdynia.

It was created for the Course Software Development hosted by the university.

The needed Inputs can be given manually and the following data from the ship is required:

- Latitude
- Longitude
- Length
- Breadth

Sprint Documentation
=====================

The links are broken, as they point towards potentiall personal information.

- `Sprint 02`_
- `Sprint 03`_
- `Sprint 04`_


Presentation
============

The Presentation regarding the Project can be found under the following link.

The links are broken, as they point towards potentiall personal information.

- `PDF Version`_
- `ODP Version`_


Installation for Devs
=====================
- For a quick installation guide for the most tools needed look here: `Starting Guide`_
- After downloading the project, perform the first time setup with ``make dbuild``.
- Now run the project with ``make drun``.
- To get the documentation, run ``make gen-docs`` which will generate a up to date version of the documentation. It can be found in ``docs/_build/html/index.html``.

**Running the Project outside of docker**

It is possible to run the project outside of docker at the moment by using ``make build`` and ``make run``.

Installation for Users
======================
- To simply run the project, one needs ``Docker`` and ``Docker Compose`` which should come with Docker.
- Build the Project by typing into the terminal ``docker-compose build``
- Run the Project by typing into the terminal ``docker-compose run``
- One can now visit `localhost`_ on Port 8080 to get the webinterface.

.. _localhost: http://localhost:8080



