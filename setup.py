from setuptools import setup

setup(
    name='spyonweb',
    version='0.1',
    description='SpyOnWeb python wrapper',
    url='https://github.com/Te-k/spyonweb',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='osint',
    install_requires=['requests', 'configparser'],
    license='MIT',
    packages=['spyonweb'],
    entry_points= {
        'console_scripts': [ 'spyonweb=spyonweb.cli:main' ]
    }
)
