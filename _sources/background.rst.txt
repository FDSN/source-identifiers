.. vim: syntax=rst

===============
Background
===============


The `Standard for the Exchange of Earthquake Data
<http://www.fdsn.org/publications/>`_ (SEED) was adopted by the FDSN
in the 1987 and has served as the dominant standard for seismological
research data archiving and exchange.

This specification of identifier is an expansion and enhancement of
the identifiers defined in SEED version 2.4.

Changes from SEED 2.4
---------------------

In SEED, a unique data source is identified in using *network*,
*station*, *location* and *channel* codes, each of which is
incorporated into the source identifer scheme described in this
specification.  Below is an overview of significant changes from the
codes as used in SEED 2.4.

-  Expand maximum length of each code as follows:

   -  *network* code: 2 => 8 characters
   -  *station* code: 5 => 8 characters
   -  *location* code: 2 => 8 characters

-  Subdivide the channel code into individually delimited codes, allowing expansion
   of each:

   -  channel => “band_source_position”, where:

      -  **Band** indicates the general sampling rate and response band of the data source,
         same meaning as SEED.
      -  **Source** is a code identifying an instrument or other data producer,
         called the "instrument" code in SEED.
      -  **Position** is a code identifying orientation or otherwise relative position,
         called the "orientation" code in SEED.

   -  Single character versions of these individual codes are the same as SEED 2.4

      -  Example: SEED 2.4 channel **BHZ** becomes **B_H_Z** in a source identifier.

   -  Use of FDSN-defined codes is required (except for **A** and **O** band codes)

-  Allow dash “-” character (ASCII 45) in station and location codes.

-  Document a convention for temporary network codes: include 4 digit
   year identifying the start year of a deployment or experiment.  As
   network codes are much larger than in SEED, they can be globally unique
   and would not need to be re-used.

-  Specify a Uniform Resource Name (URN) known as a “source identifier”
   (SID) constructed from a combination of the network, station,
   location and channel codes. This URN provides a convenient, flexible,
   single identifier for use in data formats, request mechanisms, etc.
   while allowing mapping back-and-forth between the URN and the
   separate codes as needed.
