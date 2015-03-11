from setuptools import setup
from distutils.core import setup

main_module_name = 'simpleEnum'
main_module      = __import__(main_module_name)
#description      = main_module.__doc__.split('\n\n', 1)

setup(name=main_module_name,
      version = main_module.__version__,
      py_modules=[main_module_name],
      )

'''
setup(
    name = main_module_name,
    version = main_module.__version__,
    description = description,
    author='galtza',
    author_email='galtza@wokki.me',
    url='https://github.com/galtza/simpleEnum',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
'''
