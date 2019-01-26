from setuptools import setup

def readme(): #automatically includes the readme as the homepage on github
    with open('README.rst') as f:
        return f.read()
    
setup(name='mymodule',
      version='0.1',
      description='Scrape NFL data',
      long_description='Pull data from TeamRankings Website.',
      classifiers=[
        'Development Status :: 1',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Web Scrapping',
      ],
      url='http://github.com/tymiguel/TeamRankingsWebScraper',
      author='Tyler Miguel',
      author_email='miguel_tyler@yahoo.com',
      license='MIT',
      packages=['package'],
      install_requires=['contextlib', 'requests', 'bs4', 'pandas', 'collections', 'os', 'sys'],
      include_package_data=True,
      zip_safe=False)