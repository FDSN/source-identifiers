.. vim: syntax=rst

.. _channel-codes:

=============
Channel codes
=============

Band, source and position codes
-------------------------------

A *channel* is composed of a sequence of three codes that each
describe an aspect of the instrumentation and its digitization as
follows:

   **Band**: Indicates the general sampling rate and response band of the
   data source. May be empty for non-time series data.

   **Source**: Identifies an instrument or other general data source. Cannot
   be empty.

   **Position**: Identifies the orientation or otherwise relative position.
   The position codes are specific to sources. May be empty.

A *channel* is the combination of these three codes separated by "_"
(ASCII 95) in the following pattern: ``band_source_position``, which
forms the end of a source identifier.

For usage of Band codes **A** and **O**, the source and position codes may
be defined by the generator. In these cases, the source and position
codes should not exceed three characters each in length. In all other
cases, source and position codes defined in this specification must be
used.

Two sequences are reserved for special channels: **L_O_G** for the console
log and the (deprecated) **S_O_H** for general state of health.

.. note::
   All *channels* with single-character *band*, *source*, and
   *position* codes are equivalent to SEED 2.4 channel designations
   and vice versa.


Band Code
---------

The band code specifies the general sampling rate and the approximate
response band of the instrument (when applicable to the data source).

+----------+----------------------------------+-------------------------+------------------+
|Band code |Band type                         |Sample rate (Hz)         |Lower bound (sec) |
+==========+==================================+=========================+==================+
|**F**     |...                               |>= 1000 to < 5000        |>= 10 sec         |
+----------+----------------------------------+-------------------------+------------------+
|**G**     |...                               |>= 1000 to < 5000        |< 10 sec          |
+----------+----------------------------------+-------------------------+------------------+
|**D**     |...                               |>= 250 to < 1000         |< 10 sec          |
+----------+----------------------------------+-------------------------+------------------+
|**C**     |...                               |>= 250 to < 1000         |>= 10 sec         |
+----------+----------------------------------+-------------------------+------------------+
|**E**     |Extremely Short Period            |>= 80 to < 250           |< 10 sec          |
+----------+----------------------------------+-------------------------+------------------+
|**S**     |Short Period                      |>= 10 to < 80            |< 10 sec          |
+----------+----------------------------------+-------------------------+------------------+
|**H**     |High Broadband                    |>= 80 to < 250           |>= 10 sec         |
+----------+----------------------------------+-------------------------+------------------+
|**B**     |Broadband                         |>= 10 to < 80            |>= 10 sec         |
+----------+----------------------------------+-------------------------+------------------+
|**M**     |Mid Period                        |> 1 to < 10              |                  |
+----------+----------------------------------+-------------------------+------------------+
|**L**     |Long Period                       |~ 1                      |                  |
+----------+----------------------------------+-------------------------+------------------+
|**V**     |Very Long Period                  |~ 0.1                    |                  |
+----------+----------------------------------+-------------------------+------------------+
|**U**     |Ultra Long Period                 |~ 0.01                   |                  |
+----------+----------------------------------+-------------------------+------------------+
|**R**     |Extremely Long Period             |>= 0.0001 to < 0.001     |                  |
+----------+----------------------------------+-------------------------+------------------+
|**P**     |On the order of 0.1 to 1 day [1]  |>= 0.00001 to < 0.0001   |                  |
+----------+----------------------------------+-------------------------+------------------+
|**T**     |On the order of 1 to 10 days [1]  |>= 0.000001 to < 0.00001 |                  |
+----------+----------------------------------+-------------------------+------------------+
|**Q**     |Greater than 10 days [1]          |< 0.000001               |                  |
+----------+----------------------------------+-------------------------+------------------+
|**A**     |Administrative Instrument Channel |variable                 |                  |
+----------+----------------------------------+-------------------------+------------------+
|**O**     |Opaque Instrument Channel         |variable                 |                  |
+----------+----------------------------------+-------------------------+------------------+



Source and Position Codes
-------------------------

The source code specifies the family to which the sensor belongs or
otherwise a general data source. In essence, this identifies what is
being measured or simulated. Each of these source types are detailed in
this section.

The position code provides a way to indicate the directionality of the
sensor measurement (orientation) or the relative location of the sensor.
Position codes are source-specific. When orthogonal directions are used,
there are traditional orientations of North (N), East (E), and Vertical
(Z), as well as other orientations that can be converted to traditional
ones. These options are detailed with each source type. Only use N or E
for the orientation when it is within 5 degrees of north or east. Use 1
or 2 when orientations are more than 5 degrees from north or east or to
avoid any assumptions about the orientation and ensure that the metadata
is consulted.

Seismometer
^^^^^^^^^^^

   Measures displacement/velocity/acceleration along a line defined by
   the the dip and azimuth.

   *Source Code*

   .. table::
      :align: left

      ======      ======
      **H**       High Gain Seismometer
      **L**       Low Gain Seismometer
      **G**       Gravimeter
      **M**       Mass Position Seismometer
      **N**       Accelerometer
      ======      ======

   *Position Code*

   .. table::
      :align: left

      ===================== ======
      **Z**, **N**, **E**   Traditional (Vertical, North-South, East-West), when with 5 degrees of true directions
      **A**, **B**, **C**   Triaxial (Along the edges of a cube turned up on a corner)
      **T**, **R**          For formed beams or rotated components (Transverse, Radial)
      **1**, **2**, **3**   Orthogonal components but non traditional orientations
      **U**, **V**, **W**   Optional components
      ===================== ======

   Dip/Azimuth: Ground motion vector

   Signal Units: ``m``, ``m/s``, ``m/s**2``

Tilt Meter
^^^^^^^^^^

   Measures tilt from the horizontal plane. Azimuth is typically N/S or
   E/W.

   *Source Code*

   **A**

   *Position Code*

   **N**, **E** - Traditional

   Dip/Azimuth: Ground motion vector

   Signal Units: ``rad`` (radian)

Creep Meter
^^^^^^^^^^^

   Measures the absolute movement between two sides of a fault.
   Traditionally this has been done by means of fixing a metal beam on
   one side of the fault and measuring its position on the other side,
   but can also done with light beams, triangulation wires and other
   techniques.

   The orientation and therefore the dip and azimuth would be
   perpendicular to the measuring beam, which would be along the average
   travel vector for the fault. Position/negative travel would be
   arbitrary, but would be noted in the dip/azimuth.

   *Source Code*

   **B**

   *Position Code*

   None defined

   Dip/Azimuth: Along the fault or wire vector

   Signal Units: ``m`` (meter)

Calibration Input
^^^^^^^^^^^^^^^^^

   Usually only used for seismometers or other magnetic coil
   instruments. This signal monitors the input signal to the coil to be
   used in response evaluation. Usually tied to a specific instrument.
   Sometimes all instruments are calibrated together, sometimes
   horizontals are calibrated separately from verticals.

   *Source Code*

   **C**

   *Position Code*

   **A**, **B**, **C**, **D** - For when there are only a few cal sources for many devices.

   Blank if there is only one calibrator at a time or, match calibrated
   channel (i.e. **Z**, **N** or **E**).

Pressure
^^^^^^^^

   A barometer, or microbarometer that measures pressure. Used to
   measure the atmospheric pressure or sometimes for state of health
   monitoring down hole. This includes infrasonic and hydrophone
   measurements.

   *Source Code*

   **D**

   *Position Code*

   .. table::
      :align: left

      ======  ===========
      **O**   Outside
      **I**   Inside
      **D**   Down hole
      **F**   Infrasound
      **H**   Hydrophone
      **U**   Underground
      ======  ===========

   Dip/Azimuth: Not applicable

   Signal Units: ``Pa`` (Pascal)

Electronic Test Point
^^^^^^^^^^^^^^^^^^^^^

   Used to monitor circuitry inside recording system, local power or
   seismometer. Usually for power supply voltages, or line voltages.

   *Source Code*

   **E**

   *Position Code*

   Designate as desired, make mnemonic as possible, use numbers for test
   points, etc.

   Dip/Azimuth: Not applicable

   Signal Units: ``V`` (Volt), ``A`` (Ampere), ``Hz`` (Hertz), etc.

Magnetometer
^^^^^^^^^^^^

   Measures the magnetic field at the sensor location. They measure the
   part of the field

   vector that is aligned with the measurement coil. Many magnetometers
   are three axis. The instrument will typically be oriented to local
   magnetic north. The dip and azimuth should describe this in terms of
   the geographic north.

   Example: Local magnetic north is 13 degrees east of north in
   Albuquerque. So if the magnetometer is pointed to magnetic north, the
   azimuth would be + 103 for the E channel. Some magnetometers do not
   record any vector quantity associated with the signal, but record the
   total intensity. So, these would not have any dip/ azimuth.

   *Source Code*

   **F**

   *Position Code*

   **Z**, **N**, **E** - Magnetic

   Dip/Azimuth: Not applicable

   Signal Units: ``T`` (Tesla)

Humidity
^^^^^^^^

   Absolute/relative measurements of humidity. Temperature recordings
   may also be needed for meaningful results.

   *Source Code*

   **I**

   *Position Code*

   .. table::
      :align: left

      ==========================   ===========
      **O**                        Outside environment
      **I**                        Inside building
      **D**                        Down hole
      **1**, **2**, **3**, **4**   Cabinet sources
      --                           All other letters for mnemonic source types.
      ==========================   ===========

   Dip/Azimuth: Not applicable

   Signal Units: ``%`` (Percent)

Rotational Sensor
^^^^^^^^^^^^^^^^^

   Measures solid-body rotations about an axis, commonly given in
   “displacement” (radians), velocity (radians/second) or acceleration
   (radians/second**2).

   *Source Code*

   **J** - High Gain Seismometer

   *Position Code*

   .. table::
      :align: left

      ==========================   ===========
      **Z**, **N**, **E**          Traditional (Vertical, North-South, East-West)
      **A**, **B**, **C**          Triaxial (Along the edges of a cube turned up on a corner)
      **T**, **R**                 For formed beams (Transverse, Radial)
      **Z**, **1**, **2**          Orthogonal components, but non traditional horizontal orientations
      **1**, **2**, **3**          Orthogonal components, but non traditional orientations
      **U**, **V**, **W**          Optional components
      ==========================   ===========

   Dip/Azimuth: Axis about which rotation is measured following
   right-handed rule.

   Signal Units: ``rad``, ``rad/s``, ``rad/s**2`` – following right-handed rule

Temperature
^^^^^^^^^^^

   Measurement of the temperature at some location. Typically used for
   measuring:

   1. Weather

     - Outside temperature

   2. State of Health

     - Inside recording building
     - Down hole
     - Inside electronics

   *Source Code*

   **K**

   *Position Code*

   .. table::
      :align: left

      ==========================   ===========
      **O**                        Outside environment
      **I**                        Inside building
      **D**                        Down hole
      **1**, **2**, **3**, **4**   Cabinet sources
      --                           All other letters for mnemonic source types.
      ==========================   ===========

   Signal Units: ``degC``, ``°C``, ``K``

Water Current
^^^^^^^^^^^^^

   Measurement of the velocity of water in a given direction. The
   measurement may be at depth, within a borehole or a variety of other
   locations.

   *Source Code*

   **O**

   *Position Code*

   None defined

   Dip/Azimuth: Along current direction

   Signal Units: ``m/s`` (meter/second)

   .. note::
      The special, administrative channel codes of **L_O_G** and
      **S_O_H** (deprecated) do not denote water current and should be
      avoided when using the “O” Source Code.

Geophone
^^^^^^^^

   Very short period seismometer, with natural frequency 5 - 10 Hz or
   higher.

   *Source Code*

   **P**

   *Position Code*

   **Z**, **N**, **E** - Traditional

   Dip/Azimuth: Ground Motion Vector

   Signal Units: ``m``, ``m/s``, ``m/s**2``

Electric Potential
^^^^^^^^^^^^^^^^^^

   Measures the Electric Potential between two points. This is normally
   done using a high impedance voltmeter connected to two electrodes
   driven into the ground. In the case of magnetotelleuric work, this is
   one parameter that must be measured.

   *Source Code*

   **Q**

   *Position Code*

   None defined

   Dip/Azimuth: Not applicable

   Signal Units: ``V`` (Volt)

Rainfall
^^^^^^^^

   Measures total rainfall, or an amount per sampling interval

   *Source Code*

   **R**

   *Position Code*

   **Z**, **N**, **E** - Traditional

   Dip/Azimuth: Not applicable

Linear Strain
^^^^^^^^^^^^^

   Dip/Azimuth are the line of the movement being measured. Positive
   values are obtained when stress/distance increases and negative when
   they decrease.

   *Source Code*

   **S**

   *Position Code*

   **Z**, **N**, **E** - Vertical, North-South, East-West

   Dip/Azimuth: Along axis of measurement

   Signal Units: ``m/m`` (meter per meter)

Tide
^^^^

   Measurement of depth of water at monitoring site. Not to be confused
   with lunar tidal filters or gravimeter output.

   *Source Code*

   **T**

   *Position Code*

   **Z** - Always vertical

   Dip/Azimuth: Always vertical

   Signal Units: ``m`` (meter) - Relative to sea level or local ocean depth

Bolometer
^^^^^^^^^

   Infrared instrument used to evaluate average cloud cover. Used in
   astronomy to determine observability of the sky.

   *Source Code*

   **U**

   *Position Code*

   None defined

   Dip/Azimuth: Not applicable

Volumetric Strain
^^^^^^^^^^^^^^^^^

   *Source Code*

   **V**

   *Position Code*

   None defined

   Dip/Azimuth: Not applicable

   Signal Units: ``m**3/m**3``

Wind
^^^^

   Measures the wind vector or velocity. Normal notion of dip and
   azimuth does not apply.

   *Source Code*

   **W**

   *Position Code*

   .. table::
      :align: left

      =====  ===========
      **S**  Windspeed
      **D**  Wind direction vector, relative to geographic north
      =====  ===========

   Dip/Azimuth: Not applicable

   Signal Units: ``m/s``

Derived or generated channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Time series derived from observational data or entirely generated by
   a computer.

   .. warning::
      This code is deprecated.  If no other *Source code* is
      applicable, a new code should be requested and allocated by the
      FDSN.

   *Source Code*

   **X**

   *Position Code*

   Similar to the observable data that was modified or the observable
   equivalent for generated time series (synthetics). See Position Codes
   for the corresponding observed channel.

   **Further Usage (DEPRECATED)**

   In order to document the provenance of the data, information must be
   available in the metadata for this channel that documents the
   algorithms, processes, or systems that modified or generated the time
   series. A channel comment, providing a Uniform Resource Locator
   (URL), must be included in the metadata. The information available at
   the URL must identify the processes that were applied to modify or
   generate the time series. This information must reference the FDSN
   web site (http://www.fdsn.org/x-instrument/).

Non-specific instruments
^^^^^^^^^^^^^^^^^^^^^^^^

   For instruments not specifically covered by an existing Source Code
   the Y Source Code can be used.

   .. warning::
      This code is deprecated.  If no other *Source code* is
      applicable, a new code should be requested and allocated by the
      FDSN.

   *Source Code*

   **Y**

   *Position Code*

   Instrument specific.

   **Further Usage (DEPRECATED)**

   In order to document the instrument type and provenance of the data,
   information must be available in the metadata for this channel that
   documents the instrument that was used to generate the time series. A
   channel comment, providing a short description of the instrument, the
   type of measurement it makes and a Uniform Resource Locator (URL)
   referencing the FDSN web site (http://www.fdsn.org/y-instrument) that
   fully describes the instrumentation.

Synthesized Beams
^^^^^^^^^^^^^^^^^

   This is used when forming beams from individual elements of an array.

   *Source Code*

   **Z**

   *Position Code*

   .. table::
      :align: left

      =====   ===========
      **I**   Incoherent beam
      **C**   Coherent beam
      **F**   FK beam
      **O**   Origin beam
      **D**   Wind direction vector, relative to geographic north
      =====   ===========

   Dip/Azimuth: Ground motion vector

   Signal Units: ``m``, ``m/s``, ``m/s**2``
