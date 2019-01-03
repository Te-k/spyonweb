from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='spyonweb',
    version='0.1',
    description='SpyOnWeb python wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Te-k/spyonweb',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='osint',
    install_requires=['requests', 'configparser'],
    license='MIT',
    packages=['spyonweb'],
    entry_points= {
        'console_scripts': [ 'spyonweb=spyonweb.cli:main' ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
