from setuptools import setup

setup(name='cool_lib',
      version='0.1',
      description='simples example in the python world',
      url='https://github.com/gdamjan/hello-world-python-package',
      author='gdamjan',
      author_email='gdamjan',
      license='MIT',
      packages=['cool_lib'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['cool-cmd=cool_lib.__main__:main'],
      }
)
