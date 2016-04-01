******************
Python Fix Imports
******************

Python Fix Imports is a Python module that can automatically reorganize the ``import`` statements of
your Python script. Please read the documenation for more information.

Example
=======

Fix imports allows you to automatically turn:

.. code:: python

    from any_module import d, f
    from any_module import (b,
                     e)
    from any_module import a, \
                    c,

into:

.. code:: python

    from any_module import a
    from any_module import b
    from any_module import c
    from any_module import d
    from any_module import e
    from any_module import f


Fiximport installation
======================

.. code-block:: bash

    $ pip install fiximports

Development environment
=======================

.. code-block:: bash

    $ virtualenv env
    $ source env/bin/activate
    $ pip install --upgrade -e .
    $ pip install -r test-requirements.txt
    $ python setup.py --version

Executing tests
===============

.. code-block:: bash

    $ python setup.py test

Updating AUTHORS, ChangeLog
===========================

Source distribution:

.. code-block:: bash

    $ python setup.py sdist

Binary distribution:

.. code-block:: bash

    $ python setup.py bdist

Wheels:

.. code-block:: bash

    $ python setup.py bdist_wheel

Update the dependencies for tests
=================================

.. code-block:: bash

    $ pip-compile test-requirements.in

.. note::

    We do "`pin`_" the dependencies for test environment. We do not "`pin`_ " for development.

    .. _pin: http://nvie.com/posts/better-package-management/

Generating the documentation
============================

.. code-block:: bash

    $ python setup.py docs
