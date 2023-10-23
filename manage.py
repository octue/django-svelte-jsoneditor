#!/usr/bin/env python
"""Management script for the project."""

from __future__ import absolute_import, unicode_literals

import sys


# INFORMATION
# This script manages the test server, so it can be run and
# interacted with as its own application from the root level

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
