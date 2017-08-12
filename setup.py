from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jiradoc',
    version='0.1',
    description='A JIRAdoc parser',
    long_description=long_description,
    url='https://github.com/lucianovdveekens/jiradoc',
    author='Luciano van der Veekens',
    author_email='lucianovdveekens@gmail.com',
    packages=find_packages(),
    install_requires=['argparse', 'ply'],
    package_data={
        'jiradoc': ['data/test.jiradoc']
    },
    entry_points={
        'console_scripts': [
            'jiradoc=jiradoc.__main__:main',
        ],
    },
)
