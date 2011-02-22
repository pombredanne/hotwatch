========
HotWatch
========
:Info: HotWatch is a command line utility for monitoring the status of `HotQueue <http://github.com/richardhenry/hotqueue>`_ queue instances.
:Author: Richard Henry (http://github.com/richardhenry)

About HotWatch
==============

HotWatch is a command line utility for monitoring the status of `HotQueue <http://github.com/richardhenry/hotqueue>`_ queue instances.

Use it like this::

    $ hotwatch otherqueue myqueue thisqueue
    otherqueue: 1182 items
    myqueue: 0 items
    thisqueue: 33181 items

For help, use ``hotwatch --help``.

HTTP interface and other output formats are coming soon.

To install it, run::

    pip install -U hotwatch

The source code is available on `GitHub <http://github.com/richardhenry/hotwatch>`_.

To get help with HotQueue or HotWatch, use the `HotQueue Users mailing list <http://groups.google.com/group/hotqueue-users>`_.

Contributing
============
The source is available on `GitHub <http://github.com/richardhenry/hotwatch>`_. To contribute to the project, fork it on GitHub and send a pull request, all contributions and suggestions are welcome.
