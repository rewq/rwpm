#!/usr/bin/env python3

from distutils.core import setup, Extension

setup(
	name = "rwpm",
	version = "1.0",
	ext_modules = [Extension("rwpm", ["bind.c", "libmypy.c"])]
	);
