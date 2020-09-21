.. vim: syntax=rst

=========================
Definition of identifiers
=========================

Data sources are uniquely identified using a sequence of codes named
**network**, **station**, **location** and **channel**, where the
channel is further subdivided into **band**, **source** and
**subsource** codes. Each of these codes must be composed of the
following ASCII character sets:

-  Uppercase [A-Z], ASCII 65 through 90
-  Numeric [0-9], ASCII 48 through 57

The station and location codes may further be composed of the following
ASCII character:

-  Dash “-”, ASCII 45

The codes are further defined as follows:

   **Network code**: Uniquely identifies the owner and network operator
   responsible for the data. `Network codes are assigned by the FDSN <http://www.fdsn.org/networks/>`_.
   Must be between 1 and 8 characters. Further description of :ref:`network-codes`.

   **Station code**: Uniquely identifies a station within a
   network. Station codes may be registered with the `International
   Registry of Seismograph Stations <http://www.isc.ac.uk/registries/>`_.
   Must be between 1 and 8 characters.  Otherwise, these may be whatever
   the operator wishes.

   **Location code**: Uniquely identifies a group of channels within a
   station, for example from a specific sensor or sub-processor. Must
   not exceed 8 characters. The special value of “--” (two dashes) is
   forbidden as it conflicts with previous usage for designating empty locations.
   Further description of :ref:`location-codes`.

*Channel*: A sequence of codes that identify the band, source and
subsource. Definition and values for each of these codes are in
:ref:`channel-codes`.

    **Band**: Indicates the sampling rate range and response band of
    the data source.

    **Source**: Identifies an instrument or other data source.

    **Subsource**: Identifies a sub-category within the source.

Source Identifiers
------------------

The FDSN Source Identifier (SID) is a combination of the network, station,
location, band, source and subsource codes into a Uniform Resource Name
(URN) as defined by `RFC 3986 <https://www.ietf.org/rfc/rfc3986.html>`_.
The pattern of the Source Identifier is as follows:

For identifying a data source, i.e. a specific channel:

::

   FDSN:<network>_<station>_<location>_<band>_<source>_<subsource>

where the `network`, `station` and `source` codes are required to be
non-empty. The underscore (ASCII 95) delimiters must always be present.

Abbreviations of the fully qualified identifer may also be used to
identify higher hierarchical levels such as a `location` (a collection
of specific channels within a station), a `station` within a network,
and a `network` as follows:

::

   FDSN:<network>_<station>_<location>
   FDSN:<network>_<station>
   FDSN:<network>

Example identifiers:

::

   FDSN:IU_COLA_00_B_H_Z

where network=IU, station=COLA, location=00 and channel=B_H_Z

::

   FDSN:NL_HGN__L_H_Z

where network=NL, station=HGN, location is empty and channel=L_H_Z

The ``FDSN:`` portion is a namespace identifier reserved to identify this
specification.

Mapping of SEED 2.4 codes
-------------------------

In the SEED 2.4 standard, data sources are identified by a combination
of network, station, location and channel codes, abbreviated here as a
`NSLC`. A NSLC can always be mapped to a Source
Identifier. Conversely, so long as each code is within the length
restrictions imposed by SEED 2.4, Source Identifiers can be also be
mapped back to SEED 2.4 codes. The mapping is as follows:

From SEED NSLC to Source Identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Network codes**

  The 1 to 2 character network code is mapped without change.

  For temporary networks, starting with X, Y, Z or 0-9, the 2
  character network code may be mapped either unchanged, or may follow
  the :ref:`transitional-mapping` by appending the start year to
  create a 6 character code, when the 6-character code has been
  allocated by the FDSN.

**Station codes**

  The 1 to 5 character station code is mapped without change.

**Location codes**

  The 0 to 2 character location code is mapped without change.

**Channel codes**

  The 3-character channel codes are split into the three single
  character `band`, `instrument` and `orientation` codes, which are
  mapped to the Source Identifier (:ref:`channel-codes`) `band`,
  `source` and `subsource` codes.

Examples
""""""""

Permanent network NSLC: 'IU', 'ANMO', '00', 'BHZ' maps to ``FDSN:IU_ANMO_00_B_H_Z``

Permanent network NSLC: 'IU', 'ANMO', '', 'BHZ' maps to ``FDSN:IU_ANMO__B_H_Z``

Temporary network starting in 2002 NSLC: 'XA', 'ABCD', '00', 'BHZ'
maps to ``FDSN:XA_ABCD_00_B_H_Z`` or to ``FDSN:XA2002_ABCD_00_B_H_Z``

From Source Identifier to SEED NSLC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Network codes**

  Codes from 1 and 2 characters are mapped without change.  Network
  codes following the 6-character :ref:`transitional-mapping`
  are mapped using just the first 2 characters of the code, removing
  the 4 character year.  Otherwise, there is no mapping for network
  codes greater than 2 characters.

**Station codes**

  Codes from 1 to 5 characters are mapped without change.  There is
  no mapping for stations codes greater than 5 characters.

**Locations codes**

  Codes from 0 and 2 characters are mapped without change.  There
  is no mapping for location codes greater than 2 characters.

**Channels codes**

  Code combinations where the Source Identifier (:ref:`channel-codes`)
  `band`, `source` and `subsource` codes are all 1 character each, are
  concatenated in this order and mapped to the 3 character NSLC
  channel codes.  Otherwise, there is no mapping when individual codes
  are greater than 2 characters.

Examples
""""""""

Permanent network ``FDSN:IU_ANMO_00_B_H_Z`` maps to NSLC: 'IU', 'ANMO', '00', 'BHZ'

Permanent network ``FDSN:IU_ANMO__B_H_Z`` maps to NSLC: 'IU', 'ANMO', '', 'BHZ'

Temporary network starting in 2002 ``FDSN:XA_ABCD_00_B_H_Z`` maps to NSLC: 'XA', 'ABCD', '00', 'BHZ'

Temporary network starting in 2002 ``FDSN:XA2002_ABCD_00_B_H_Z`` maps to NSLC: 'XA', 'ABCD', '00', 'BHZ'
