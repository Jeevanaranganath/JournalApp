from distutils.core import setup

requirements = ['requests==2.22.0',
                'flask==1.1.1',
                'pymysql==0.9.3']


setup(
    name='journalApp',
    version='1.0',
    description='Application to store personal journal log with user management',
    author="Jeevana S Ranganath",
    author_email='jeevanasranganath@gmail.com',
    packages=['journalApp'],
    install_requirements=requirements
)