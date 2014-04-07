.. image:: https://travis-ci.org/enthought/distributed-array-protocol.png?branch=master
   :target: https://travis-ci.org/enthought/distributed-array-protocol

Distributed Array Protocol
==========================

Source repository for the Distributed Array Protocol and associated utilities.

A validator for data structures defined in the protocol is included as
``validator.py``.

For a version of the protocol document rendered as HTML, see

http://distributed-array-protocol.readthedocs.org

To build a version of the protocol document yourself, install `Sphinx`_, then
run ``make html`` or ``make singlehtml`` in this directory.  See the output of
``make help`` for more information.

.. _Sphinx: http://sphinx-doc.org/

To run the tests for the validator and the included utilities, run ``python -m
unittest discover`` from this directory.

