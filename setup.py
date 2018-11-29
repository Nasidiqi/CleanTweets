from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name = 'CleanTweets',
      author = 'Krystin Sinclair, Jessica Fogerty, Henry Tappa',
      description = '...',
      license = 'MIT',
      packages = find_packages(),
      install_requires = required,
      version = '0.0'
      url = 'git@github.com:jfogerty18/CleanTweets.git')
