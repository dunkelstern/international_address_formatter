import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='international_address_formatter',
        version='1.0.0',
        description='International address formatter',
        long_description='''
This is a address formatter that can format addresses in multiple formats that are common in different countries.

For formatting the addresses the `worldwide.yml` from [OpenCageData address-formatting repository](https://github.com/OpenCageData/address-formatting) is used to format the address according to customs in the country that is been encoded.

See `README.md` in the [repository](https://github.com/dunkelstern/international_address_formatter) for more information.
        ''',
        long_description_content_type='text/markdown',
        url='https://github.com/dunkelstern/international_address_formatter',
        author='Johannes Schriewer',
        author_email='hallo@dunkelstern.de',
        license='LICENSE.txt',
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Operating System :: OS Independent'
        ],
        keywords='address formatting, international',
        packages=['international_address_formatter'],
        scripts=[
        ],
        install_requires=[
            'PyYAML >= 5.0',
            'pystache >= 0.5',
        ],
        setup_requires=[],
        tests_require=[],
        dependency_links=[
        ]
)
