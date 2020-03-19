.. xFDSN Source Identifiers documentation master file

xFDSN Source Identifiers
========================

This specification defines the construction of unique identifiers for
data sources exchanged and archived in formats and services defined by
the `International Federation of Digital Seismograph Networks
<http://www.fdsn.org/>`_ (FDSN) and related services and formats.

The FDSN defines, allocates and adopts a number of codes that, when
combined in a hierarchy, uniquely identify a data source.  The
identifer is constructed by combining `network`, `station`, `location`
and `channel` codes, where the channel code is further subdivided into
`band`, `source` and `position` codes.

This specification defines the meaning and rules for these codes in
addition to how they are to be combined into a URI-like pattern as
follows:

::

   XFDSN:<network>_<station>_<location>_<band>_<source>_<position>

This single-string identifier uniquely identifies a source in FDSN
formats and services.

.. toctree::
   :maxdepth: 2

   definition
   channel-codes
   background

* :ref:`search`

