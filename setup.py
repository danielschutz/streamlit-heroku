import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit_heroku-danielschutz",
    version="0.0.1",
    author="Daniel Schutz",
    author_email="danieljschutz@gmail.com",
    description='Tool to help create files needed to deploy Streamlit App on Heroku',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    scripts=['bin/streamlit_heroku'],
)