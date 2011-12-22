from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='socialapps.theme.bootstrap',
      version=version,
      description="A theme for socialapps based on Twitter Bootstrap toolkit",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Erik Rivera',
      author_email='erik@rivera.pro',
      url='http://rivera.pro',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['socialapps', 'socialapps.theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
