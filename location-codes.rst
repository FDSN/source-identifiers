.. vim: syntax=rst

.. _location-codes:

=========================
Location codes
=========================

Location codes are used to logically group channels within a single
station deployment. This can be for channels produced by the same
sensor, channels produced in a sub-processor, many sensors deployed in a
grid or an array, etc.

When used to designate sensors deployed in an array, operators may
choose to identify a series of sensors using ordered or otherwise
meaningful location code values.

The use and meaning of the location code is generally up to the
defining network. However the following guidelines are recommended for
consistency across networks:

1. Channels that are closely related should have the same location
   code, e.g. channels from the same instrument that differ only in
   orientation or sampling rate, like ``B_H_Z`` and ``B_H_E`` or
   ``B_H_Z`` and ``S_H_Z``, should have the same location code.

2. Sharing a single location code does not necessarily imply the
   channels come from the same instrument, e.g. the primary
   seismometer and primary accelerometer might both have location code
   ``00`` even if they are physically separate instruments.

3. The primary seismic channels at traditional seismic stations should
   have location code of ``00`` or be empty.

4. Use of an empty location code is recommended only for stations that
   do not have multiple instruments of the same type and have
   traditionally not used location codes.

5. Sensors in an array within a station may be logically grouped in a
   regular, systematic scheme, e.g. incrementing numbers for a linear
   array, or using two identifiers separated by a dash for a 2D grid.

6. Alpha-numeric ordering should be considered desirable, e.g. using
   ``01`` to ``10`` instead of ``1`` to ``10`` for a linear array.

7. Otherwise the network may use the location code for any meaningful
   system of organizing and namespacing channels at a station.
