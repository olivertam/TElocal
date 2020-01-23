from setuptools import setup

def readme():
      with open('README.rst') as f:
               return f.read()

setup(name='TElocal',
      version='0.1.0',
      description='Tool for estimating differential enrichment of Transposable Elements and other highly repetitive regions in a locus-specific approach',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Environment :: Console',
          'Natural Language :: English',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Programming Language :: Python :: 2.7',
          'Operating System :: MacOS',
          'Operating System :: Unix'
      ],
      keywords='TE transposable element differential enrichment',
      url='http://hammelllab.labsites.cshl.edu/software#TElocal',
      author='Talitha Forcier, Ying Jin, Eric Paniagua, Oliver Tam, Molly Hammell',
      author_email='talitha@cshl.edu',
      license='GPLv3',
      packages=[
          'TEToolkit',
          'TEToolkit.IO',
          'TEToolkit.ShortRead'
      ],
      platforms=[
          'Linux',
          'MacOS'
      ],
      install_requires=[
          'argparse',
          'pysam>=0.9'
      ],
      include_package_data=True,
      zip_safe=False,
      scripts=[
          'TElocal'
      ]
)
