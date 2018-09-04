from setuptools import setup

setup(
    name='snapshotalyzer3300',
    version='0.1',
    author="Curt Mailandt",
    author_email="cmailand@amfam.com",
    description="Snapshotalyzer3300 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/curtm33/snapshotalyzer-33000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)