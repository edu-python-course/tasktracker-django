.. _acen1999: https://www.fakenamegenerator.com/gen-male-hobbit-nz.php?s=06b3fb87-34ca-4d27-80bf-e9f345a27f6e
.. _butime: https://www.fakenamegenerator.com/gen-male-hobbit-nz.php?s=280e40ec-2694-43d6-ad4c-61a2c55da8a3
.. _prombery87: https://www.fakenamegenerator.com/gen-female-hobbit-nz.php?s=acdde07d-08fe-49ad-9e61-484e10e793cd
.. _wheed1997: https://www.fakenamegenerator.com/gen-male-hobbit-nz.php?s=8956c2c9-8d8c-4f9a-b423-fb2a69bd1e16

###############################################################################
                             Task Tracker - Django
###############################################################################

This project implements a simple task tracking system designed to demonstrate
the capabilities of the Django web framework.

Authenticated users have the ability to create new tasks, assigning them either
to themselves or to other users.
Tasks can be updated or modified by their reporters or assignees,
reflecting changes in task status or details.

As a training project, Task Tracker serves as a practical example of a web
application built with Django. It showcases fundamental features such as user
authentication, database schema design, query optimization, and the **MVC**
(Model-View-Controller) software design pattern, which is key to understanding
how Django operates.

And yes, this is another **todo app** on the Internet.

But more than just a checklist, it's a platform for learners to observe
the inner workings of a Django project and to experiment with its extensive
features.

Installing Dependencies
=======================

.. code-block:: shell

    pip install -r requirements.txt

This project comes with a minimal list of dependencies, which can be easily
installed using the command above.
Here is some detailed information on the dependency list:

+---------------------+---------+---------------------------------------+
| Package             | Version | Package homepage                      |
+=====================+=========+=======================================+
| Django              | ^5.0.1  | https://djangoproject.com/            |
+---------------------+---------+---------------------------------------+
| psycopg2-binary     | ^2.9.9  | https://www.psycopg.org/              |
+---------------------+---------+---------------------------------------+
| djangorestframework | ^3.14.0 | https://www.django-rest-framework.org |
+---------------------+---------+---------------------------------------+

.. rubric:: Django

Django is a high-level Python web framework that encourages rapid development
and clean, pragmatic design. Built by experienced developers, it takes care of
much of the hassle of web development, allowing you to focus on writing your
app without needing to reinvent the wheel. It’s free and open source.

.. rubric:: psycopg

Psycopg is the most popular PostgreSQL adapter for the Python programming
language. Its core is a complete implementation of the Python DB API 2.0
specifications. Several extensions allow access to many of the features
offered by PostgreSQL. ``psycopg2-binary`` is intended for beginners to start
playing with Python and PostgreSQL without needing to meet the build
requirements for the ``psycopg2`` package. However, this should not be used
in production. It is suitable, though, for training projects like this one.

Project Configuration
=====================

The Task Tracker project utilizes environment variables for configuration
settings.

+-----------------------+-----------------------------------------------------+
| Variable Name         | Meaning                                             |
+=======================+=====================================================+
| ``DJANGO_SECRET_KEY`` | In Django, the SECRET_KEY is an essential setting   |
|                       | used for cryptographic signing. It should be kept   |
|                       | secret. This key is used by Django to perform       |
|                       | cryptographic operations, such as generating        |
|                       | signatures for CSRF tokens, password reset tokens,  |
|                       | and other secure data. A strong and unique SECRET   |
|                       | KEY is vital for the security of Django             |
|                       | applications.                                       |
|                       |                                                     |
|                       | You can generate a new SECRET_KEY using the         |
|                       | `Djecrety <https://djecrety.ir/>`_ service.         |
+-----------------------+-----------------------------------------------------+
| ``PGHOST``            | PostgreSQL server host, default to "localhost".     |
+-----------------------+-----------------------------------------------------+
| ``PGPORT``            | PostgreSQL server port, default to 5432.            |
+-----------------------+-----------------------------------------------------+
| ``PGUSER``            | PostgreSQL server role name, required.              |
+-----------------------+-----------------------------------------------------+
| ``PGPASSWORD``        | PostgreSQL server role password, required.          |
+-----------------------+-----------------------------------------------------+
| ``PGDATABASE``        | PostgreSQL server database, required.               |
+-----------------------+-----------------------------------------------------+

Setting Up Environment Variables
--------------------------------

Certain settings in the Docker Compose file can be overridden by setting up
environment variables. If you are not familiar with environment variables,
you can read more about them on this
`Wikipedia article <https://en.wikipedia.org/wiki/Environment_variable>`_.

To set an environment variable, type the following into your terminal:

.. code-block:: shell

    SET VARIABLE=value     # for Windows users
    export VARIABLE=value  # for Unix users (Linux and macOS)

Using an Env File
-----------------

Instead of setting environment variables manually, you can use a ``.env`` file
to centrally manage them. Simply place this file at the root of your project
directory. This file is also used to define environment variables for Docker
containers, ensuring consistent configurations across different environments.

Refer to the provided ``.env.example`` file as a template for setting up your
own ``.env`` file. Be sure to customize the variable values according to your
project's requirements.

Project fixtures
================

There are dummy data included to this repository for testing needs and to use
within a project in a local dev-sandbox. To upload data to the database apply
all available migrations and do:

.. code-block:: shell

    python manage.py loaddata <fixture>

where ``<fixture>`` is the fixture file name.

.. rubric:: Available fixtures

:users:
    Provides users to test project features and play with admin panels while
    development.

    .. csv-table::
        :header: username,password,is_active,is_admin,url

        acen1999,cieted3eiPo,false,false,`acen1999`_
        butime,Zeiriev1oo,true,true,`butime`_
        prombery87,ieZeiSh5k,true,false,`prombery87`_
        wheed1997,enohR4cog,true,false,`wheed1997`_

:tasks:
    Provides dummy tasks. Should be uploaded after the **users** fixtures,
    since it uses reference to the user model.

Using Docker Compose
====================

Prerequisites:

- docker compose installed

This project comes with a Docker Compose file recommended for the Django
training environment. If you are not familiar with Docker Compose, it is
a tool for container management
(`Would you like to know more? <https://docs.docker.com/compose/>`_).

The installation process is described
`here <https://docs.docker.com/compose/install/>`_.

The Compose file defines a minimalistic set of services - a database server
and a GUI client - running in individual containers. You need to map ports
from your machine to docker containers to get things working correctly.

The default mapped ports are:

* 5432 for the ``postgres`` service
* 5050 for the ``pgadmin`` service
* 8080 for the ``static`` service

These values can be changed by modifying the environment variables.

Container management is as simple as:

.. code-block:: shell

    docker compose up -d  # start all containers
    docker compose down   # stop all containers

PostgreSQL
----------

The db service runs the PostgreSQL server container. It exposes port 5432 to
the host machine, allowing you to use it as if you had PostgreSQL running
locally. The default port mapping is "5432:5432". If you already have port 5432
occupied by other software, you may set up any available port by using
the ``POSTGRES_PORT`` environment variable.

The predefined credentials are:

+----------+----------+
| Username | Password |
+==========+==========+
| postgres | postgres |
+----------+----------+

You can run this service separately from other services defined in the Compose
file with:

.. code-block:: shell

    docker compose up -d db

pgAdmin
-------

pgAdmin is one of the most popular PostgreSQL clients. Starting with
version 4.x, it uses a web-based UI running in your web browser. The pgAdmin
container exposes its 80 port to the host machine. By default, this port is
mapped to 5050. If port 5050 is already occupied by other software on your
system, you may set up any available port by using the ``PGADMIN_PORT``
environment variable.

After running pgAdmin, visit http://localhost:5050 in your web browser
(adjust the port number if needed).

The predefined credentials to connect pgAdmin are:

+-------------------------------+----------+
| Email                         | Password |
+===============================+==========+
| pgadmin@edu-python-course.org | pgadmin  |
+-------------------------------+----------+

When connecting to the PostgreSQL server via pgAdmin, use "postgresql-server"
as the alias for the db container. This connection is already defined in the
"servers.json" file under the "docker" directory, so there is no need to
connect manually.

Note that it may take some time for the container to set up and run
the internal server.

Nginx
-----

Nginx (pronounced "engine-x") is a widely-used open-source web server and
reverse proxy server. It is designed for high concurrency, fast delivery of
web content, and offers various features for web application deployment and
performance optimization.

This container has been added to serve any static files via HTTP and simulate
a production environment. The container exposes its 80 port to the host
machine. By default, this port is mapped to 8080. If port 8080 is already
occupied by other software on your system, you may set up any available port by
using the ``STATIC_PORT`` environment variable.

The local storage for static files is the "static" directory.
Place your content into it, and it will be available at
http://localhost:8080/path/to/file.

This directory can be used as the ``STATIC_ROOT`` setting during development:

.. code-block:: python

    # noinspection PyUnresolvedReferences
    STATIC_ROOT = BASE_DIR / "static"

You can run this service separately from other services defined in the Compose
file with:

.. code-block:: shell

    docker compose up -d static

After running the container, visit http://localhost:8080 in your web browser
(adjust the port number if needed).
