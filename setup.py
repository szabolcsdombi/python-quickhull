from setuptools import setup, Extension

QuickHull = Extension(
	'QuickHull.hull',
	sources = [
		'src/QuickHull.cpp',
		'src/quickhull/QuickHull.cpp',
	]
)

setup(
	name = 'QuickHull',
	version = '0.9.0',
	description = 'QuickHull',
	url = 'https://github.com/cprogrammer1994/QuickHull',
	author = 'Szabolcs Dombi',
	author_email = 'cprogrammer1994@gmail.com',
	license = 'MIT',
	packages = ['QuickHull'],
	ext_modules = [QuickHull],
	platforms = ['win32', 'win64']
)
