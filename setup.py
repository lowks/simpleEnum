from setuptools import setup

with open('flask/.version', 'rb') as f:
    version = f.read ().decode ("utf-8")
 
setup(
    name = 'simpleEnum',
    packages = ['simpleEnum'],
    version = version
    description = 'A really simple enum implementation',
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
