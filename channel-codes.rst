.. vim: syntax=rst

.. _channel-codes:

=============
Channel codes
=============

Band, source and subsource codes
--------------------------------

A *channel* is composed of a sequence of three codes that each
describe an aspect of the instrumentation and its digitization as
follows:

   **Band**: Indicates the general sampling rate and response band of the
   data source. May be empty for non-time series data.

   **Source**: Identifies an instrument or other general data source. Cannot
   be empty.

   **Subsource**: Identifies a sub-category within the source, often
   the orientation, relative positon, or sensor type. The meaning of
   subsource codes are specific to the containing source. May be
   empty.

A *channel* is the combination of these three codes separated by "_"
(ASCII 95) in the following pattern: ``Band_Source_Subsource``, which
forms the end of a source identifier.

For usage of Band codes **A** and **O** (both deprecated), the source
and subsource codes may be defined by the generator. In these cases,
the source and subsource codes should not exceed three characters each
in length. In all other cases, source and subsource codes defined in
this specification must be used.

Two sequences are reserved for special channels, both deprecated:
**L_O_G** for the console log and **S_O_H** for general state of health.

.. note::
   All *channels* with single-character ``Band``, ``Source``, and
   ``Subsource`` codes are equivalent to SEED 2.4 channel designations
   and vice versa.

Band Code
---------

The band code specifies the general sampling rate and the approximate
response band of the instrument (when applicable to the data source).

+----------+-------------------------+-----------------------------+------------------+
|Band code |Band type                |Sample rate (samples per sec)|Lower bound (sec) |
+==========+=========================+=============================+==================+
|**J**     |...                      |> 5000                       |                  |
+----------+-------------------------+-----------------------------+------------------+
|**F**     |...                      |>= 1000 to < 5000            |>= 10 sec         |
+----------+-------------------------+-----------------------------+------------------+
|**G**     |...                      |>= 1000 to < 5000            |< 10 sec          |
+----------+-------------------------+-----------------------------+------------------+
|**D**     |...                      |>= 250 to < 1000             |< 10 sec          |
+----------+-------------------------+-----------------------------+------------------+
|**C**     |...                      |>= 250 to < 1000             |>= 10 sec         |
+----------+-------------------------+-----------------------------+------------------+
|**E**     |Extremely Short Period   |>= 80 to < 250               |< 10 sec          |
+----------+-------------------------+-----------------------------+------------------+
|**S**     |Short Period             |>= 10 to < 80                |< 10 sec          |
+----------+-------------------------+-----------------------------+------------------+
|**H**     |High Broadband           |>= 80 to < 250               |>= 10 sec         |
+----------+-------------------------+-----------------------------+------------------+
|**B**     |Broadband                |>= 10 to < 80                |>= 10 sec         |
+----------+-------------------------+-----------------------------+------------------+
|**M**     |Mid Period               |> 1 to < 10                  |                  |
+----------+-------------------------+-----------------------------+------------------+
|**L**     |Long Period              |~ 1                          |                  |
+----------+-------------------------+-----------------------------+------------------+
|**V**     |Very Long Period         |>= 0.1 to < 1                |                  |
+----------+-------------------------+-----------------------------+------------------+
|**U**     |Ultra Long Period        |>= 0.01 to < 0.1             |                  |
+----------+-------------------------+-----------------------------+------------------+
|**W**     |Ultra-ultra Long Period  |>= 0.001 to < 0.01           |                  |
+----------+-------------------------+-----------------------------+------------------+
|**R**     |Extremely Long Period    |>= 0.0001 to < 0.001         |                  |
+----------+-------------------------+-----------------------------+------------------+
|**P**     |On order of 0.1 to 1 day |>= 0.00001 to < 0.0001       |                  |
+----------+-------------------------+-----------------------------+------------------+
|**T**     |On order of 1 to 10 days |>= 0.000001 to < 0.00001     |                  |
+----------+-------------------------+-----------------------------+------------------+
|**Q**     |Greater than 10 days     |< 0.000001                   |                  |
+----------+-------------------------+-----------------------------+------------------+
|**I**     |Irregularly sampled      |irregular                    |                  |
+----------+-------------------------+-----------------------------+------------------+
|**A**     |:strike:`Administrative` |variable, DEPRECATED         |                  |
+----------+-------------------------+-----------------------------+------------------+
|**O**     |:strike:`Opaque`         |variable, DEPRECATED         |                  |
+----------+-------------------------+-----------------------------+------------------+

Source and Subsource Codes
--------------------------

The source code specifies the family to which the sensor belongs or
otherwise a general data source. In essence, this identifies what is
being measured or simulated. Each of these source types are detailed in
this section.

The subsource code provides a way to indicate the directionality of
the sensor measurement (orientation), the relative location of the
sensor or the sensor type.  Subsource codes are source-specific.

.. _geographic-orientation:

   **Geographic orientation subsource codes**

   Traditional orientation values of North-Source (N), East-West (E),
   and Vertical (Z) should `only` be used when within 5 degress of
   true directions.  Do not use **N** or **E** designations if the
   orientation of horizontal components is known to deviate more than
   5 degrees from true North/East.

   For orthogonal components that are in nontraditional orientations,
   if the orientation of the horizontal components is known to
   deviate more than 5 degrees from true North and East, the
   respective channels should be named **1**, **2** instead of N, E
   (N->1, E->2).

   For sources that record data in a direction typically aligned with
   geographical coordinate systems, the subsource identifier should
   follow these conventions (where appropriate):

   +--------------------+------------------------------------------------------------+
   |Subsource codes     | Description                                                |
   +====================+============================================================+
   |**N**, **E**, **Z** | Traditional orientations of North (N), East (E), and Up (Z)|
   |                    |                                                            |
   |                    | *When within 5 degrees of true directions*                 |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **Z** | Orthogonal components, nontraditional horizontals          |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **3** | Orthogonal components, nontraditional orientations         |
   +--------------------+------------------------------------------------------------+
   |**T**, **R**        | For rotated components or beams (Transverse, Radial)       |
   +--------------------+------------------------------------------------------------+
   |**A**, **B**, **C** | Triaxial (Along the edges of a cube turned up on a corner) |
   +--------------------+------------------------------------------------------------+
   |**U**, **V**, **W** | Optional components, also used for raw triaxial output     |
   +--------------------+------------------------------------------------------------+

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
      **M**       Mass Position Seismometer
      **N**       Accelerometer
      **P**       Geophone, very short period seismometer with natural frequency 5 - 10 Hz or higher
      ======      ======

   *Subsource Code* - See :ref:`Geographic orientation codes <geographic-orientation>` for more details.

   +--------------------+------------------------------------------------------------+
   |**N**, **E**, **Z** | Traditional orientations of North (N), East (E), and Up (Z)|
   |                    |                                                            |
   |                    | *When within 5 degrees of true directions*                 |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **Z** | Orthogonal components, nontraditional horizontals          |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **3** | Orthogonal components, nontraditional orientations         |
   +--------------------+------------------------------------------------------------+
   |**T**, **R**        | For rotated components or beams (Transverse, Radial)       |
   +--------------------+------------------------------------------------------------+
   |**A**, **B**, **C** | Triaxial (Along the edges of a cube turned up on a corner) |
   +--------------------+------------------------------------------------------------+
   |**U**, **V**, **W** | Optional components, also used for raw triaxial output     |
   +--------------------+------------------------------------------------------------+

   Dip/Azimuth: Ground motion vector

   Signal Units: ``m``, ``m/s``, ``m/s**2``

Tilt Meter
^^^^^^^^^^

   Measures tilt from the horizontal plane. Azimuth is typically N/S or
   E/W.

   *Source Code*

   **A**

   *Subsource Code* - See :ref:`Geographic orientation codes <geographic-orientation>` for more details.

   +--------------------+------------------------------------------------------------+
   |**N**, **E**        | Traditional orientations of North (N), East (E), and Up (Z)|
   |                    |                                                            |
   |                    | *When within 5 degrees of true directions*                 |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**        | Orthogonal components, nontraditional orientations         |
   +--------------------+------------------------------------------------------------+

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

   *Subsource Code*

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

   *Subsource Code*

   **A**, **B**, **C**, **D** - For when there are only a few calibration sources for many devices.

   Blank if there is only one calibrator at a time or, match calibrated
   channel (i.e. **Z**, **N** or **E**).

Pressure
^^^^^^^^

   A barometer, microbarometer, or other gauge that measures pressure.
   Used to measure atmospheric, water, and any other pressure.  This
   includes infrasonic and hydrophone measurements.

   *Source Code*

   **D**

   *Subsource Code*

   .. table::
      :align: left

      ======  ===========
      **O**   Outside
      **I**   Inside
      **D**   Down hole
      **F**   Infrasound
      **G**   Deep sea differential pressure gauge
      **H**   Hydrophone
      **U**   Underground
      ======  ===========

   Dip/Azimuth: For many pressure measurements Dip and Azimuth are not
   applicable.  If the signal will be used for seismological
   applications, set Dip to -90 if a positive pressure change gives a
   positive signal, 90 if a positive pressure change gives a negative
   signal. This will align polarities with the vertical seismometer
   channel for UPGOING waves.

   Signal Units: ``Pa`` (Pascal)

Electronic Test Point
^^^^^^^^^^^^^^^^^^^^^

   Used to monitor circuitry inside recording system, local power or
   seismometer. Usually for power supply voltages, or line voltages.

   *Source Code*

   **E**

   *Subsource Code*

   Designate as desired, make mnemonic as possible, use numbers for test
   points, etc.

   Dip/Azimuth: Not applicable

   Signal Units: ``V`` (Volt), ``A`` (Ampere), ``Hz`` (Hertz), etc.

Magnetometer
^^^^^^^^^^^^

   Measures the magnetic field at the sensor location. They measure
   the part of the field vector that is aligned with the measurement
   coil. Many magnetometers are three axis. The instrument will
   typically be oriented to local magnetic north. The dip and azimuth
   should describe this in terms of the geographic north.

   Example: Assuming magnetic north is 13 degrees east of north at the
   recording site, if the magnetometer is pointed to magnetic north, the
   azimuth would be + 103 for the E channel. Some magnetometers do not
   record any vector quantity associated with the signal, but record the
   total intensity. So, these would not have any dip or azimuth.

   *Source Code*

   **F**

   *Subsource Code*

   **Z**, **N**, **E** - Magnetic

   Dip/Azimuth: Not applicable

   Signal Units: ``T`` (Tesla)

Humidity
^^^^^^^^

   Absolute/relative measurements of humidity. Temperature recordings
   may also be needed for meaningful results.

   *Source Code*

   **I**

   *Subsource Code*

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

   **J** - Rotation rate sensor

   *Subsource Code* - See :ref:`Geographic orientation codes <geographic-orientation>` for more details.

   +--------------------+------------------------------------------------------------+
   |**N**, **E**, **Z** | Traditional orientations of North (N), East (E), and Up (Z)|
   |                    |                                                            |
   |                    | *When within 5 degrees of true directions*                 |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **Z** | Orthogonal components, nontraditional horizontals          |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **3** | Orthogonal components, nontraditional orientations         |
   +--------------------+------------------------------------------------------------+
   |**T**, **R**        | For rotated components or beams (Transverse, Radial)       |
   +--------------------+------------------------------------------------------------+
   |**A**, **B**, **C** | Triaxial (Along the edges of a cube turned up on a corner) |
   +--------------------+------------------------------------------------------------+
   |**U**, **V**, **W** | Optional components, also used for raw triaxial output     |
   +--------------------+------------------------------------------------------------+

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

   *Subsource Code*

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

   *Subsource Code*

   None defined

   Dip/Azimuth: Along current direction

   Signal Units: ``m/s`` (meter/second)

   .. note::
      The special, administrative channel codes of **L_O_G** and
      **S_O_H** (both deprecated) do not denote water current and should be
      avoided when using the “O” Source Code.

Gravimeter
^^^^^^^^^^

   Measurement of a gravitational field.

   *Source Code*

   **G** - Gravitaional sensor

   *Subsource Code*

   **Z** - Traditionally
   **1** - Unknown, or not vertical**

   *Note*: historically some channels from accelerometers have used a
   instrumentation code of **G**. As of August 2000 the FDSN defined
   the use of this code as limited to gravity.

   Dip/Azimuth: Gravity field Vector

   Signal Units: ``m/s**2``

Electric Potential
^^^^^^^^^^^^^^^^^^

   Measures the Electric Potential between two points. This is normally
   done using a high impedance voltmeter connected to two electrodes
   driven into the ground. In the case of magnetotelleuric work, this is
   one parameter that must be measured.

   *Source Code*

   **Q**

   *Subsource Code*

   None defined

   Dip/Azimuth: Not applicable

   Signal Units: ``V`` (Volt)

Rainfall
^^^^^^^^

   Measures total rainfall, or an amount per sampling interval

   *Source Code*

   **R**

   *Subsource Code*

   None defined

   Dip/Azimuth: Not applicable

Linear Strain
^^^^^^^^^^^^^

   Dip/Azimuth are the line of the movement being measured. Positive
   values are obtained when stress/distance increases and negative when
   they decrease.

   *Source Code*

   **S**

   *Subsource Code* - See :ref:`Geographic orientation codes <geographic-orientation>` for more details.

   +--------------------+------------------------------------------------------------+
   |**N**, **E**, **Z** | Traditional orientations of North (N), East (E), and Up (Z)|
   |                    |                                                            |
   |                    | *When within 5 degrees of true directions*                 |
   +--------------------+------------------------------------------------------------+
   |**1**, **2**, **3** | Nontraditional orientations                                |
   +--------------------+------------------------------------------------------------+

   Dip/Azimuth: Along axis of measurement

   Signal Units: ``m/m`` (meter per meter)

Tide
^^^^

   Measurement of depth of water at monitoring site. Not to be confused
   with lunar tidal filters or gravimeter output.

   *Source Code*

   **T**

   *Subsource Code*

   **Z** - Always vertical

   Dip/Azimuth: Always vertical

   Signal Units: ``m`` (meter) - Relative to sea level or local ocean depth

Bolometer
^^^^^^^^^

   Infrared instrument used to evaluate average cloud cover. Used in
   astronomy to determine observability of the sky.

   *Source Code*

   **U**

   *Subsource Code*

   None defined

   Dip/Azimuth: Not applicable

Volumetric Strain
^^^^^^^^^^^^^^^^^

   *Source Code*

   **V**

   *Subsource Code*

   None defined

   Dip/Azimuth: Not applicable

   Signal Units: ``m**3/m**3``

Wind
^^^^

   Measures the wind vector or velocity. Normal notion of dip and
   azimuth does not apply.

   *Source Code*

   **W**

   *Subsource Code*

   .. table::
      :align: left

      =====  ===========
      **S**  Windspeed
      **D**  Wind direction vector, relative to geographic north
      **H**  Horizontal wind speed
      **Z**  Vertical wind speed
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

   *Subsource Code*

   Similar to the observable data that was modified or the observable
   equivalent for generated time series (synthetics). See subsource codes
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

   *Subsource Code*

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

   *Subsource Code*

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
