*************
Start Hacking
*************

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

.. note::

    In the normal case, package is automatically published to Pypi after successful Travis build.

    To release using this automatic procedure, simply create a new tag, push it (do not forget to do
    ``git push --tags``). When successful, Travis will automatically publish a new version on Pypi.

    Promote the tag to a proper Release in Github to align everything.

    PS: ChangeLog will be properly updated on Pypi, not on Github (you need to align it manually).

Here is the manual release procedure.

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

- Push to Github with:

  .. code-block:: bash

      git push --tags

- create a release with the same tag

- Build source and distribution:

  .. code-block:: bash

      $ rm -rfv dist/*
      $ python setup.py bdist
      $ python setup.py bdist_wheel
      $ python setup.py bdist_wheel --universal

- Upload distributions:

  .. code-block:: bash

      $ twine upload dist/*
