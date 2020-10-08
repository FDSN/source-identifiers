#!/usr/bin/env python3

"""This module contains the SourceID class for supporting FDSN Source Identifiers

http://docs.fdsn.org/projects/source-identifiers
"""

import sys
import re

class SourceID(object):
    """Class for FDSN Source Identifiers: http://docs.fdsn.org/projects/source-identifiers

    Methods support conversion to and from SEED network, station, location, and channel codes.

    Validation of source identifiers and individual codes is included.
    """

    def __init__(self, sourceid=None):
        self.sourceid = None

        if sourceid is not None:
            if self.is_valid(sourceid):
                self.sourceid = sourceid
            else:
                raise Exception(f'Source Identifier is not recognized: {sourceid}')

    def __str__(self):
        return f'{self.sourceid}'

    def __repr__(self):
        return f'{self.sourceid}'

    def is_valid(self, sourceid=None):
        """Verify Source Identifier is a valid form"""

        matchid = sourceid if sourceid is not None else self.sourceid

        # A regex to match Source Identifiers
        sidre = re.compile('^FDSN:'              # Required prefix
                           '([A-Za-z0-9]+)'      # Required network: alphanumeric
                           '(_([-A-Za-z0-9]+)'   # Optional non-empty station: alphanumeric and dash
                           '(_([-A-Za-z0-9]*)'   # Optional possibly empty location: alphanumeric and dash
                           '(_([A-Za-z0-9]*_[A-Za-z0-9]+_[A-Za-z0-9]*)' # Optional channel with non-empty source: alphanumeric
                           ')?)?)?$')            # Nested hierarchy of optional codes

        return True if sidre.match(matchid) else False

    def from_nslc(network=None, station=None, location=None, channel=None, validate=True):
        """Generate a new SourceID constructed from individual codes

        Convert SEED network, station, location, channel fields to a Source Identifier
        of the form: FDSN:NET_STA_LOC_CHAN, where CHAN="BAND_SOURCE_SUBSOURCE"

        If the channel is stricly SEED (3 [A-Za-z0-9] characters) it will be converted to
        the extended form of "BAND_SOURCE_SUBSOURCE".
        """
        if network is None:
            raise Exception(f'Network code is a minimum requirement')

        # Check for valid SEED and extended code contents
        if validate:
            # Alphanumeric characters
            if not re.match('^[A-Za-z0-9]+$', network):
                raise Exception(f"Invalid network code:'{network}'")

            # Alphanumeric and dash
            if station and not re.match('^[-A-Za-z0-9]+$', station):
                raise Exception(f"Invalid station code:'{station}'")

            # Alphanumeric and dash
            if location and not re.match('^[-A-Za-z0-9]+$', location):
                raise Exception(f"Invalid location code:'{location}'")

            # Alphanumeric, either an extended code with underscores or exactly 3-characters
            if channel and (not re.match('^[A-Za-z0-9]*_[A-Za-z0-9]+_[A-Za-z0-9]*$', channel) and
                            not re.match('^[A-Za-z0-9]{3,3}$', channel)):
                raise Exception(f"Invalid channel code:'{channel}'")

        # Create an extended channel (band_source_subsource) from a stricly-SEED channel,
        # identified when exactly 3 of [A-Za-z0-9] characters.
        if channel is not None and re.match('^[A-Za-z0-9]{3,3}$', channel):
            channel = f'{channel[0]}_{channel[1]}_{channel[2]}'

        # Generate Source Identifier at appropriate level
        if station is None and location is None and channel is None:
            return SourceID(f'FDSN:{network}')
        elif location is None and channel is None:
            return SourceID(f'FDSN:{network}_{station}')
        elif channel is None:
            return SourceID(f'FDSN:{network}_{station}_{location}')
        else:
            return SourceID(f'FDSN:{network}_{station}_{location}_{channel}')

    def to_nslc(self, sourceid=None):
        """Split a Source Identifier into network, station, location, channel codes

        An extended channel the form "BAND_SOURCE_SUBSOURCE" is collapsed to SEED channel codes
        when possible, i.e. when exactly 3 of [A-Za-z0-9] characters (with underscore separators).
        """

        splitid = sourceid if sourceid is not None else self.sourceid

        if splitid is None:
            raise Exception(f'Source Identifier is specified')

        if not self.is_valid(splitid):
            raise Exception(f'Source Identifier is not recognized: {splitid}')


        # Split into 4 codes and skip "FDSN:" prefix
        network, station, location, channel, *_ = splitid[5:].split('_', maxsplit=3) + [None] * 4

        # Collapse an extended channel (band_source_subsource) to a stricly-SEED channel
        # when possible, i.e. when exactly 3 of [A-Za-z0-9] characters (with underscore separators).
        if channel is not None and re.match('^[A-Za-z0-9]_[A-Za-z0-9]_[A-Za-z0-9]$', channel):
            channel = f'{channel[0]}{channel[2]}{channel[4]}'

        return [network, station, location, channel]


# Implement a simple converter when called as a command line program
if __name__ == "__main__":

    import argparse
    import textwrap
    import os.path

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert between Source Identifiers and SEED codes',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent(f"""
                                     Examples:\n
                                       {os.path.basename(sys.argv[0])} FDSN:XX_STA_LO_L_H_Z
                                       {os.path.basename(sys.argv[0])} FDSN:XX_STA_LO
                                       {os.path.basename(sys.argv[0])} FDSN:XX_STA
                                       {os.path.basename(sys.argv[0])} FDSN:XX
                                       {os.path.basename(sys.argv[0])} XX STA LO LHZ
                                       {os.path.basename(sys.argv[0])} XX STA LO L_H_Z
                                       {os.path.basename(sys.argv[0])} XX STA LO LL_HH_ZZ
                                       {os.path.basename(sys.argv[0])} XX STA LO
                                       {os.path.basename(sys.argv[0])} XX STA
                                       {os.path.basename(sys.argv[0])} XX
                                     """))
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='increase verbosity')
    parser.add_argument('inputcodes', nargs='*',
                        help='SourceID (FDSN:N_S_L_B_S_s) or individual codes (Net Sta Loc Chan)')
    args = parser.parse_args()

    # A single argument with a "FDSN:" prefix is SourceID, convert to individual codes
    if len(args.inputcodes) == 1 and args.inputcodes[0].startswith('FDSN:'):
        sid = args.inputcodes[0]

        if args.verbose:
            print (f'Generating SEED network, station, location, channel from SourceID {sid}')

        try:
            network, station, location, channel, *_ = SourceID(sid).to_nslc() + [None] * 4
        except Exception as e:
            print(e)
            sys.exit(1)

        print (f"Input SourceID: '{sid}'")
        print ("=> {}{}{}{}".
               format(
                   f"Network: '{network}'",
                   f"Station: '{station}'" if station else '',
                   f"Location: '{location}'" if location else '',
                   f"Channel: '{channel}'" if channel else ''))

    # Otherwise individual codes are provided, convert to SourceID
    elif len(args.inputcodes) > 0:
        network, station, location, channel, *_ = args.inputcodes + [None] * 4

        if args.verbose:
            print (f'Generating SourceID from {network}, {station}, {location}, {channel}')

        try:
            sid = SourceID.from_nslc(network, station, location, channel)
        except Exception as e:
            print(e)
            sys.exit(1)

        print (f"Input Network: '{network}', Station: '{station}', Location: '{location}', Channel: '{channel}'")
        print (f"=> SourceID: '{sid}'")

    else:
        parser.print_help(sys.stderr)
