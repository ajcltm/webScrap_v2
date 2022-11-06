from setuptools import setup, find_packages

setup(name='webScrap_v2',
      version='0.1',
      url='https://github.com/ajcltm/webScrap',
      license='MIT',
      author='ajcltm',
      author_email='ajcltm@gmail.com',
      description='',
      packages=find_packages(exclude=['webScrap_v2']),
      zip_safe=False,
      setup_requires=['pydantic>=1.0'],
      test_suite='test.test_fileSaver')