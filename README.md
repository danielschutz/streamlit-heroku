#streamlit-heroku
####This is a command line tool to help create necessary files to deploy a Streamlit app on Heroku

##Installation
```
pip install streamlit-heroku
```

##Instructions
####From the top directory of a git repo, run the following command:
```python
streamlit_heroku
```
If you run the command in an empty repo named ```new-app```, the repo will no contain the following tree:

```
.
├── new-app
│   └── app.py
├── Procfile
├── requirements.txt
├── runtime.txt
└── setup.sh
```

The main Streamlit app should go in new-app/app.py.

After installing dependencies, you will need to update the requirements.txt. Here is an example of one method:
```bash
pip freeze > requirements.txt
```

###Note: This template assumes Python version 3.9.7, which is the default version for Heroku. If you want to use a different version, you can update runtime.txt. The following runtimes are supported on all supported stacks:
    python-3.10.0
    python-3.9.7
    python-3.8.12
    python-3.7.12
    python-3.6.15

##Deploy
####Your project should ready to deploy using the Heroku CLI.

###Create Heroku App
```bash
heroku create
```

###Push to Heroku
```bash
git push heroku main
```

###Open your app
```bash
heroku open
```