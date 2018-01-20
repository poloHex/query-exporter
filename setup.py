from setuptools import setup, find_packages

from query_exporter import __version__, __doc__ as description

tests_require = ['asynctest']

config = {
    'name': 'query-exporter',
    'version': __version__,
    'license': 'GPLv3+',
    'description': description,
    'long_description': open('README.rst').read(),
    'author': 'Alberto Donato',
    'author_email': 'alberto.donato@gmail.com',
    'maintainer': 'Alberto Donato',
    'maintainer_email': 'alberto.donato@gmail.com',
    'url': 'https://github.com/albertodonato/query-exporter',
    'packages': find_packages(),
    'include_package_data': True,
    'entry_points': {'console_scripts': [
        'query-exporter = query_exporter.main:script']},
    'test_suite': 'query_exporter',
    'install_requires': [
        'aiohttp',
        'prometheus-client',
        'prometheus-aioexporter >= 1.3.0',
        'PyYaml',
        'SQLAlchemy',
        'sqlalchemy_aio',
        'toolrack'],
    'tests_require': tests_require,
    'extras_require': {'testing': tests_require},
    'keywords': 'sql metric prometheus exporter',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities']}

setup(**config)
