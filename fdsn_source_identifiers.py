#!/usr/bin/env python3

"""This module contains a SourceID class for FDSN Source Identifiers

http://docs.fdsn.org/projects/source-identifiers
"""

import sys
import re
from enum import Enum

# A regex to validate Source Identifiers
sourceid_re = re.compile('^FDSN:'              # Required prefix
                         '([A-Z0-9]{1,8})'     # Required network: upper-alphanumeric
                         '(_([-A-Z0-9]{1,8})'  # Optional non-empty station: upper-alphanumeric and dash
                         '(_([-A-Z0-9]{0,8})'  # Optional possibly-empty location: upper-alphanumeric and dash
                         '(_([A-Z0-9]*_[A-Z0-9]+_[A-Z0-9]*)' # Optional channel with non-empty source: upper-alphanumeric
                         ')?)?)?$')            # Nested hierarchy of optional codes

# Regex patterns to validate SEED-compatible codes
network_seed_re = re.compile('^[A-Z0-9]{1,2}$')
station_seed_re = re.compile('^[A-Z0-9]{1,5}$')
location_seed_re = re.compile('^[A-Z0-9]{0,2}$')
channel_seed_re = re.compile('^[A-Z0-9]{3,3}$')
channel_seed_compat_re = re.compile('^[A-Z0-9]_[A-Z0-9]_[A-Z0-9]$')

class SourceID(object):
    """Class for FDSN Source Identifiers: http://docs.fdsn.org/projects/source-identifiers

    Methods support conversion to and from SEED and extended network, station, location, and channel codes.

    Validation of source identifiers and individual codes is included.
    """

    def __init__(self, sourceid=None):
        self.sourceid = None

        if sourceid is not None:
            if self.is_valid(sourceid):
                self.sourceid = sourceid
            else:
                raise Exception(f'Invalid Source Identifier: {sourceid}')

    def __str__(self):
        return f'{self.sourceid}'

    def __repr__(self):
        return f'{self.sourceid}'

    def is_valid(self, sourceid=None):
        """Verify Source Identifier is a valid form"""

        return True if sourceid_re.match(sourceid or self.sourceid) else False

    @classmethod
    def from_seed(cls, network=None, station=None, location=None, channel=None, validate=True):
        """Generate a new SourceID constructed from individual SEED codes

        Convert SEED network, station, location, channel fields to a Source Identifier
        of the form: FDSN:NET_STA_LOC_CHAN, where CHAN="BAND_SOURCE_SUBSOURCE"

        The SEED channel is converted to the extended form of "BAND_SOURCE_SUBSOURCE".
        """
        if network is None:
            raise Exception(f'Network code is a minimum requirement')

        # Check for valid SEED and extended code contents
        if validate:
            errs = []

            if not network_seed_re.match(network):
                errs.append(f"Invalid SEED network code:'{network}'")

            if station and not station_seed_re.match(station):
                errs.append(f"Invalid SEED station code:'{station}'")

            if location and not location_seed_re.match(location):
                errs.append(f"Invalid SEED location code:'{location}'")

            if channel and not channel_seed_re.match(channel):
                errs.append(f"Invalid SEED channel code:'{channel}'")

            if errs:
                raise ValueError('\n'.join(errs))

        # Create an extended channel (band_source_subsource) from SEED channel
        if channel:
            channel = f'{channel[0]}_{channel[1]}_{channel[2]}'

        # Generate Source Identifier at appropriate level
        if station is None and location is None and channel is None:
            return cls(f'FDSN:{network}')
        elif location is None and channel is None:
            return cls(f'FDSN:{network}_{station}')
        elif channel is None:
            return cls(f'FDSN:{network}_{station}_{location}')
        else:
            return cls(f'FDSN:{network}_{station}_{location}_{channel}')

    def to_seed(self, validate=True):
        """Split a Source Identifier into SEED network, station, location, channel codes

        An extended channel the form "BAND_SOURCE_SUBSOURCE" is collapsed to SEED channel codes.
        """

        if self.sourceid is None:
            raise Exception(f'Source Identifier is not available')

        if not self.is_valid():
            raise Exception(f'Invalid Source Identifier: {sourceid}')

        # Split into 4 codes and skip "FDSN:" prefix
        network, station, location, channel, *_ = self.sourceid[5:].split('_', maxsplit=3) + [None] * 4

        # Collapse extended channel (band_source_subsource) to a SEED channel
        if channel and channel_seed_compat_re.match(channel):
            channel = f'{channel[0]}{channel[2]}{channel[4]}'

        # Enforce SEED code length limits
        if validate:
            errs = []

            if not network_seed_re.match(network):
                errs.append(f"Invalid SEED network code:'{network}'")

            if station and not station_seed_re.match(station):
                errs.append(f"Invalid SEED station code:'{station}'")

            if location and not location_seed_re.match(location):
                errs.append(f"Invalid SEED location code:'{location}'")

            if channel and not channel_seed_re.match(channel):
                errs.append(f"Invalid SEED channel code:'{channel}'")

            if errs:
                raise ValueError('\n'.join(errs))

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
            network, station, location, channel, *_ = SourceID(sid).to_seed() + [None] * 4
        except Exception as e:
            print(e)
            sys.exit(1)

        print (f"Input SourceID: '{sid}'")
        print ("=> {}{}{}{}".
               format(
                   f"Network: '{network}'",
                   f" Station: '{station}'" if station else '',
                   f" Location: '{location}'" if location else '',
                   f" Channel: '{channel}'" if channel else ''))

    # Otherwise individual SEED codes are provided, convert to SourceID
    elif len(args.inputcodes) > 0:
        network, station, location, channel, *_ = args.inputcodes + [None] * 4

        if args.verbose:
            print (f'Generating SourceID from {network}, {station}, {location}, {channel}')

        try:
            sid = SourceID.from_seed(network, station, location, channel)
        except Exception as e:
            print(e)
            sys.exit(1)

        print ("Input {}{}{}{}".
               format(
                   f"Network: '{network}'",
                   f" Station: '{station}'" if station else '',
                   f" Location: '{location}'" if location else '',
                   f" Channel: '{channel}'" if channel else ''))
        print (f"=> SourceID: '{sid}'")

    else:
        parser.print_help(sys.stderr)
