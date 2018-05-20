Python library for cinergia electronic loads control
====================================================

This library enables to monitor and control cinergia electronic loads.

The library has been tested with python 2.7, 3.5 and 3.6.

Requirements
------------

You just need to install pymodbus.

Usage
-----

First import the module and declare a client to connect to the load:

.. code-block:: python

        import cinergia.client
        cinergiaClient = cinergia.client.CinergiaClient('xxx.xxx.xxx.xxx')
        cinergiaClient.connect()

Then you can read some registers (you have to know the registers table):

.. code-block:: python

        print("Errors:", cinergiaClient.read_uint32(168))
        print("Input temperature:",cinergiaClient.read_IQ21(158))

Finally, close the connection:

.. code-block:: python

        cinergiaClient.disconnect()

Install
-------

.. code-block:: bash

   pip install .


Coverage
--------

.. code-block:: bash

   coverage run setup.py
   coverage report -m


Work in progress
----------------

* Implement writing operations
* Include the modbus tables in the module so that to access registers via keywords
