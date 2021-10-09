import subprocess
import sys
import os


def make_app_folder(app_name: str) -> None:
    """
    creates project folder system

    :param app_name: str name of heroku application
    :return: None
    """
    os.mkdir(app_name)
    os.mkdir(f"{app_name}/{app_name}")


def make_procfile(app_name: str) -> None:
    """
    creates Procfile to tell Heroku what files to run

    :param app_name: str name of heroku application
    :return: None
    """
    txt = f"web: sh setup.sh && streamlit run ./{app_name}/app.py"
    with open(f"{app_name}/Procfile", "w") as procfile:
        procfile.writelines(txt)


def make_runtime(app_name: str) -> None:
    """
    Creates a runtime.txt to tell Heroku which Python version to use.
    Assumes active Python version.

    :param app_name: str name of heroku application
    :return: None
    """
    version = sys.version_info
    version_text = f"python-{version[0]}.{version[1]}.{version[2]}"
    with open(f"{app_name}/runtime.txt", "w") as runtime:
        runtime.writelines(version_text)


def make_requirements(app_name: str) -> None:
    """
    Creates an empty requirements.txt.

    Use 'streamlit_heroku update-requirements'
    from main project file to update
    requirements.txt after dependencies
    are added.

    :param app_name: str name of heroku application
    :return: None
    """
    with open(f"{app_name}/requirements.txt", "w") as requirements:
        requirements.writelines("")


def make_setup_sh(app_name: str) -> None:
    """
    Creates setup.sh

    :param app_name: str name of heroku application
    :return: None
    """
    txt = f"""mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless=true\n\
enableCORS=false\n\
port=$PORT\n\
" > ~/.streamlit/config.toml"""
    with open(f"{app_name}/setup.sh", "w") as setup:
        setup.writelines(txt)


def make_app_py(app_name: str) -> None:
    """
    creates app.py file

    this is where the main streamlit app goes

    :param app_name: str name of heroku application
    :return: None
    """
    txt = "#Your app goes here"
    with open(f"{app_name}/{app_name}/app.py", "w") as app:
        app.writelines(txt)


def main():
    if len(sys.argv) == 2:
        app_name = sys.argv[1]
        make_app_folder(app_name)
        make_procfile(app_name)
        make_runtime(app_name)
        make_requirements(app_name)
        make_setup_sh(app_name)
        make_app_py(app_name)
    else:
        print("No app name entered")
