from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='jiradoc',
    version='0.1',
    description='A small Python module to parse JIRAdoc markup files and insert them into JIRA',
    long_description=long_description,
    url='https://github.com/lucianovdveekens/jiradoc',
    author='Luciano van der Veekens',
    author_email='lucianovdveekens@gmail.com',
    packages=find_packages(),
    install_requires=['ply', 'jira', 'pyyaml', 'appdirs'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    package_data={
        'jiradoc': ['data/sample_config.yml']
    },
    entry_points={
        'console_scripts': [
            'jiradoc=jiradoc.__main__:main',
        ],
    },
)
