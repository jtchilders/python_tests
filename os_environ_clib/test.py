#!/usr/bin/env python
import os
import ctypes

os.environ['TEST'] = 'Hello'

cfunc = ctypes.CDLL('/projects/datascience/parton/deephyper/python_tests/os_environ_clib/libtest.so')

cfunc.print_TEST()

