import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'markdown',
    'passlib',
    'pygments',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms',
    ]

setup(name='learning_journal',
      version='0.0',
      description='learning_journal',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='E.L. Winberry',
      author_email='elaewin@gmail.com',
      url='https://github.com/elaewin/learning-journal/tree/master',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='learning_journal',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = learning_journal:main
      [console_scripts]
      setup_db = learning_journal.scripts.initializedb:main
      """,
      )
