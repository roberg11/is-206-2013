try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Robert',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'r.gjengaar@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['newproject'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
