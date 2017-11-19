from setuptools import setup, find_packages
setup(
    name='QuantV',
    version='0.0.1',
    description='Functions for calculating GRE level math',
    long_description='Displayed on GitHub',
    url='https://github.com/hamakobe/GRE-Math',
    author='Harmon Amakobe',
    author_email='hamakobe@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
        ],
    keywords='GRE math functions',
    packages=find_packages(exclude = ['docs', 'tests*']),
    install_requires=[],
    package_data={
        'Q' : ['random_data.dat']
        },
    data_files=None,
    entry_points={
        'console_scripts': [
            'hello=quantv:say_hello',
            ],
        }
    )