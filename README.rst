Vici
====
*This module has been adopted by the strongSwan project. Please direct any pull requests or issues there.*
https://github.com/strongswan/strongswan/tree/master/src/libcharon/plugins/vici/python

A simple python library that allow control of strongSwan over the vici
interface which was introduced in version 5.2.0. It is aimed to be straight
forward and easy to use.


Example usage
-------------

.. code-block:: python

    >>> import vici
    >>> s = vici.Session()
    >>> s.version()
    {'release': '3.18.6-1-ARCH', 'sysname': 'Linux', 'daemon': 'charon',
    'version': '5.2.2', 'machine': 'x86_64'}
    >>> s.load_pool({"p1": {"addrs": "10.0.0.0/24"}})
    CommandResult(success=True, errmsg=None, log=None)
    >>> s.get_pools()
    {'p1': {'offline': '0', 'base': '10.0.0.0', 'online': '0', 'size': '254'}}



Installation
------------

Simply install by using pip;

.. code-block:: bash

    $ pip install vici
