# FDSN Source Identifier specification

This specification defines the construction of unique identifiers for data sources exchanged and archived in formats and services defined by the [International Federation of Digital Seismograph Networks](https://www.fdsn.org/) (FDSN) and related services and formats.

This repository contains the source of the documentation and serves as a coordination point for additions and changes to the specification.

Documentation rendered for the `master` branch can be found at: https://github.com/FDSN/source-identifiers/

Specification releases are at: https://docs.fdsn.org/projects/source-identifiers

## Documentation source organization

* The `draft` branch contains the latest draft documentation. All changes are first applied to
  this branch for review and merged with main for releases
* Specification releases are tags in the form `v.#.#-d#`.

## Versioning

The versioning scheme used in tags uses the following form: `vMAJOR.MINOR-dDOC` where:
* `MAJOR.MINOR` are the version of the specification, and
* `DOC` is the version of the documentation.

The `DOC` version changes when the documentation has been updated with clarifications, typos,
etc. and does not imply any functional change to the specification.

## Change procedure

To propose changes to the specification a submitter must provide two things:

* A written description of the change (motivations, potential impact, etc.).
* A fork of the most recent `draft` branch of the repository submitted as a pull request (PR) on GitHub.  The PR should include the changes being proposed.

The procedure is as follows:

1. Submitter sends written proposal to the WG-II mailing list, with or without a link to a GitHub pull request or issue.
2. If written proposal is approved by WG-II but no pull request was submitted, the proposer should submit a pull request to the repository and send a link to the WG-II for technical review.
3. If the written proposal and technical review of the pull request are approved by WG-II, a steward will merge the pull request.

The change will then be included in the next release.

For technical discussion of a potential change without creating pull request,
an issue may be created.  The procedure for Working Group II,
described above, must be followed for any changes.

Changes and issues should only be grouped together when logically
related in order to streamline review and acceptance.

## Documentation build and publishing status:
[![Documentation Status](https://readthedocs.org/projects/source-identifiers/badge/?version=latest)](http://docs.fdsn.org/projects/source-identifiers/en/latest/?badge=latest)
