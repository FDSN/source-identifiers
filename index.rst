.. FDSN Source Identifiers documentation master file

========================
Overview
========================

This specification defines the construction of unique identifiers for
data sources exchanged and archived in formats and services defined by
the `International Federation of Digital Seismograph Networks
<http://www.fdsn.org/>`_ (FDSN) and related services and formats.

The FDSN defines, allocates and adopts a number of codes that, when
combined in a hierarchy, uniquely identify a data source at a given
time.  The identifer is constructed by combining `network`, `station`,
`location` and `channel` codes, where the channel code is further
subdivided into `band`, `source` and `subsource` codes.

This specification defines the meaning and rules for these codes in
addition to how they are to be combined into a URI-like pattern as
follows:

::

   FDSN:<network>_<station>_<location>_<band>_<source>_<subsource>

This single-string identifier uniquely identifies a source in FDSN
formats and services.

.. toctree::
   :maxdepth: 2

   self
   definition
   network-codes
   location-codes
   channel-codes
   background
   FDSN home <https://www.fdsn.org/>

* :ref:`search`

