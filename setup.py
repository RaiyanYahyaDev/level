from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup
from level.__init__ import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
	long_description = file.read()


class RunTests(Command):
	description = 'run tests'
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		print(__version__)
		errno = call(['pytest', '--cov=sew', '--cov-report=term-missing'])
		raise SystemExit(errno)


setup(
	name='level',
	version=__version__,
	description='A new take on code management.',
	long_description=long_description,
	url='https://gitlab.com/raiyanyahya/level',
	author='Raiyan Yahya',
	author_email='raiyanyahyadeveloper@gmail.com',
	classifiers=[
		'Intended Audience :: Developers',
		'Topic :: Utilities',
	],
	keywords='cli',
	packages=find_packages(),
	install_requires=['click', 'pytest'],
	extras_require={'test': ['coverage', 'pytest', 'pytest-cov']},
	entry_points={'console_scripts': ['level=level.cli:cli']},
	cmdclass={'test': RunTests},
)
