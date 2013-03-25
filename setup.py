from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc ="protect a site with a disclaimer."
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='bda.disclaimer',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: developement',
            'Environment :: Web Environment',
            'Framework :: Zope3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',           
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Robert Niederreiter',
      author_email='rnix@squarewave.at',
      url='',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools', 
          'cornerstone.browser',
          # -*- Extra requirements: -*
      ],
      extras_require={
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
