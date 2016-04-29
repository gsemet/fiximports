******************
Python Fix Imports
******************

|travis-badge|_ |codecov-badge|_ |readthedocs-badge|_ |pypi-badge|_ |download-badge|_

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
                           c

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


.. |travis-badge| image:: https://travis-ci.org/Stibbons/fiximports.svg?branch=master
.. _travis-badge: https://travis-ci.org/Stibbons/fiximports
.. |codecov-badge| image:: http://codecov.io/github/Stibbons/fiximports/coverage.svg?branch=master
.. _codecov-badge: http://codecov.io/github/Stibbons/fiximports?branch=master
.. |readthedocs-badge| image:: https://readthedocs.org/projects/fiximports/badge/?version=latest
.. _readthedocs-badge: https://readthedocs.org/projects/fiximports/builds/
.. |pypi-badge| image:: https://badge.fury.io/py/fiximports.svg
.. _pypi-badge: https://pypi.python.org/pypi/fiximports/
.. |download-badge| image:: https://img.shields.io/pypi/dm/fiximports.svg
.. _download-badge: https://pypi.python.org/pypi/fiximports
