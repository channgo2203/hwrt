#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
from nose.plugins.skip import SkipTest
import shutil
import os

# hwrt modules
import hwrt.download as download


# Tests
def execution_test():
    download.get_parser()
    # download.is_file_consistent(31, 'mysql_online')
