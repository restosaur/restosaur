About
=====

What Restosaur is?
^^^^^^^^^^^^^^^^^^

Restosaur is a RESTful foundation library for Python, which aims to be a
transparent layer for building REST-like or RESTful services,
adaptable to any web framework.

The key concepts are:

  * make library layer as transparent as possible,
  * operate on object of any type as a model,
  * focus on resources and their representations,
  * base on content types as a client-server contract machinery,
  * do not force an API developer to use any specific structures,
    patterns, solutions,
  * maximize flexibility of constructing control flow and data
    factories,
  * provide clean interface, sane defaults and handy toolkit,
  * make library independent from any web framework and provide adapters
    to common web frameworks,
  * follow *explicit is better than implicit* rule (see PEP20) -- no
    magic inside.


.. note::

  Up to v0.8 Restosaur is a Django-only project for historical reasons.
  Please follow :doc:`roadmap` for details.


What Restosaur is not?
^^^^^^^^^^^^^^^^^^^^^^

Restosaur is not a framework. There are no batteries included. There are
no paginators, CRUD mappers, authenticators, permission system
nor autogenerated HTML representation (which is a bad concept at all).

Every REST-like or RESTful API may be very specific. As an API author
you shold have possibility to do anything you want and use any tool you
need.

If you're using a web framework, you have decent tools already.
Restosaur just helps you to adapt your data and business logic to
a RESTful service.

