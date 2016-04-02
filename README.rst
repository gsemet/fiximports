******************
Python Fix Imports
******************

|travis-badge|_ |codecov-badge|_ |readthedocs-badge|_

Python Fix Imports is a Python module that can automatically reorganize the ``import`` statements of
your Python script, sorting them in respect the "one import, one line" principle.

Please read the
`online documenation for more information <http://fiximports.readthedocs.org/en/latest/>`_.

Sublime Text 3 users can use my
`Python Fix Imports<https://packagecontrol.io/packages/Python%20Fix%20Imports>`_ plugin.

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
