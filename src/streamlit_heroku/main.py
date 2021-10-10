import os


def make_app_folder(app_name: str) -> None:
    """
    creates project folder system

    :param app_name: str name of heroku application
    :return: None
    """
    os.mkdir(app_name)


def make_procfile(app_name: str) -> None:
    """
    creates Procfile to tell Heroku what files to run

    :param app_name: str name of heroku application
    :return: None
    """
    txt = f"web: sh setup.sh && streamlit run ./{app_name}/app.py"
    with open(f"Procfile", "w") as procfile:
        procfile.writelines(txt)


def make_runtime() -> None:
    """
    Creates a runtime.txt to tell Heroku which Python version to use.
    Assumes Heroku default version 3.9.7.

    Heroku Supported runtimes:
    python-3.10.1
    python-3.9.7
    python-3.8.12
    python-3.7.12
    python-3.6.15
    """
    version_text = "python-3.9.7"
    with open("runtime.txt", "w") as runtime:
        runtime.writelines(version_text)


def make_requirements() -> None:
    """
    Creates an empty requirements.txt.
    """
    with open("requirements.txt", "w") as requirements:
        requirements.writelines("")


def make_setup_sh() -> None:
    """
    Creates setup.sh
    """
    txt = f"""mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless=true\n\
enableCORS=false\n\
port=$PORT\n\
" > ~/.streamlit/config.toml"""
    with open("setup.sh", "w") as setup:
        setup.writelines(txt)


def make_app_py(app_name: str) -> None:
    """
    creates app.py file

    this is where the main streamlit app goes

    :param app_name: str name of heroku application
    :return: None
    """
    txt = "#Your app goes here"
    with open(f"{app_name}/app.py", "w") as app:
        app.writelines(txt)


def main():
    app_name = os.getcwd().split("/")[-1]
    make_app_folder(app_name)
    make_procfile(app_name)
    make_runtime()
    make_requirements()
    make_setup_sh()
    make_app_py(app_name)
