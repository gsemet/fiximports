******************
Python Fix Imports
******************

|travis-badge|_ |codecov-badge|_ |readthedocs-badge|_ |pypi-badge|_

Python Fix Imports is a Python executable that can automatically reorganize the ``import``
statements of your Python script, by splitting single import statement importing several package
into as many import statement as imported module ("one import, one line" principle), and sorting
these import statements respecting position of *group* of them.

The main advantage for this method is to strictly restrict the forms of import statement and
facilitate multiple code branch merges and rebase, while still allowing to specify a given order if
it is the wish of the developer.

Please read the full rational
`online documenation for more information <http://fiximports.readthedocs.org/en/latest/>`_.

Sublime Text 3 users can use my
`Python Fix Imports <https://packagecontrol.io/packages/Python%20Fix%20Imports>`_ plugin.

Example
=======

Fix imports allows you to automatically turn:

.. code:: python

    from any_module import d, f
    from other_module import z, x
    from any_module import (b,
                     e)
    from any_module import a, \
                    c,

    from a_module_that_should_be import at, after, all_others

into:

.. code:: python

    from any_module import a
    from any_module import b
    from any_module import c
    from any_module import d
    from any_module import e
    from any_module import f
    from other_module import x
    from other_module import z

    from a_module_that_should_be import after
    from a_module_that_should_be import all_others
    from a_module_that_should_be import at


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

Universal Wheels:

.. code-block:: bash

    python setup.py bdist_wheel --universal

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

Release and upload to Pypi
==========================

- Commit everything localy

- Create the release tag

  .. code-block:: bash

      git tag 0.?.?

- Create you source distribution to regenerate ChangeLog properly

  .. code-block:: bash

      $ python setup.py sdist

- Overwrite the release tag

  .. code-block:: bash

      git tag --force 0.?.?

- Push to Github, create a release with the same tag

- Build source and distribution:

  .. code-block:: bash

      $ rm -rfv dist/*
      $ python setup.py bdist
      $ python setup.py bdist_wheel
      $ python setup.py bdist_wheel --universal

- Upload distributions:

  .. code-block:: bash

      $ twine upload dist/*


.. |travis-badge| image:: https://travis-ci.org/Stibbons/fiximports.svg?branch=master
.. _travis-badge: https://travis-ci.org/Stibbons/fiximports
.. |codecov-badge| image:: http://codecov.io/github/Stibbons/fiximports/coverage.svg?branch=master
.. _codecov-badge: http://codecov.io/github/Stibbons/fiximports?branch=master
.. |readthedocs-badge| image:: https://readthedocs.org/projects/fiximports/badge/?version=latest
.. _readthedocs-badge: https://readthedocs.org/projects/fiximports/builds/
.. |pypi-badge| image:: https://badge.fury.io/py/fiximports.svg
.. _pypi-badge: https://badge.fury.io/py/fiximports
