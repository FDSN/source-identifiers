.. vim: syntax=rst

.. _network-codes:

=========================
Network codes
=========================

`Network codes <http://www.fdsn.org/networks/>`_ are assigned by the
FDSN to uniquely identify the owner and operator responsible for the
data collected by a network.  Network operators `may request a network
code <http://www.fdsn.org/networks/request/>`_ as needed for new
deployments.

Temporary network code convention
---------------------------------

Network codes for deployments that are known to be temporary are
strongly encouraged to include the 4-digit start year of the deployment
at the end of the code with the following pattern:

::

   <1-4 characters><4-digit start year>

For example, ``SEIS2018`` would be a valid network code and imply that the
initial deployment was in the year 2018 and is temporary.

.. _transitional-mapping:

Transitional mapping of previously allocated temporary network codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Historical temporary network codes were allocated as two-character
codes, with the first character being a digit (0-9) or the letters X,
Y or Z.  Many of these codes have been reused for different
deployments in different years and are therefore not globally
unique. A data owner or delegate data center may wish to convert, or
provide an alias, for data using the older, 2-character codes. The
mapping from the 2-character codes is strongly recommended to follow
this pattern:

::

   <2-character code><4-digit start year>

where the initial character is a digit (``0-9``) or the letters ``X``,
``Y`` or ``Z``.

For example, a network deployment allocated a network code of ``XA``
operating in the years 2002 and 2003 could be mapped to ``XA2002``.

A temporary network operator may wish to request a 6 character network
code in the transitional mapping pattern above in order have a
globally unique code that is also usable with miniSEED 2 through the
mapping. Furthermore, the FDSN reserves all 6 character network
codes that match the transitional mapping pattern for all previously
or future allocated 2 character temporary network codes. Thus the code
XA2002 must be assigned solely to the temporary network with code XA
that was operating in 2002.

Special network codes
---------------------

Two network codes are reserved for special cases:

* ``SS`` – This code may be used by any institution running a Single Station,
  the station should be registered with the `International
  Registry of Seismograph Stations <http://www.isc.ac.uk/registries/>`_.
  Care must be taken to ensure that the station code is not the same
  as another station using the SS network code.

* ``XX`` – This code is not real.  It is reserved for test data, examples or
  transient usage when a real code cannot be used.  Data with this network
  code should never be distributed.
