from setuptools import setup

setup(
    name='streamlit_heroku',
    version='0.0.1',
    packages=['src/streamlit_heroku'],
    url='',
    license='MIT',
    author='Daniel Schutz',
    author_email='danieljschutz@gmail.com',
    description='Tool to help create files needed to deploy Streamlit App on Heroku',
    scripts=['src/bin/streamlit_heroku']
)
