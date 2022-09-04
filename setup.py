from setuptools import setup


setup(
    name='friendly_name_mixin',
    version='1.0.3',
    url='https://github.com/petarmaric/friendly_name_mixin',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description='Mixin class for extracting friendly names from classes',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    platforms='any',
    py_modules=['friendly_name_mixin'],
    tests_require = ['coverage>=3.3', 'nose>=1.0', 'nosexcover>=1.0.7'],
    test_suite = 'nose.collector',
)
