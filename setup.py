from setuptools import setup

APP = ['voting_countdown.py']
DATA_FILES = ['data']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True
    },
    'packages': ['datetime'],
    'iconfile': 'data/election.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
