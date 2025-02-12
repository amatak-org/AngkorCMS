# About
AngkorCMS is written in Python by RONY.



## Struture


angkor-cms/\
│
├── app.py\
├── angkor\
│   └── __init__.py\
└── requirements.txt


## Install

`git clone https://github.com/amatak-org/AngkorCMS.git`

cd AngkorCMS

pip install -r requirements.txt


## Install in Development Mode
`pip install -e .`

## On Windows:
`python -m pip install -U pip setuptools`

## Terminal
`angkor run`

This will start the Angkor server on port 7000,\
and you can access it by navigating to\ 
http://localhost:7000 in your browser.


## Tipes:
# To check all package is installed
`pip list`

angkor       0.1\
blinker      1.9.0\
click        8.1.8\
colorama     0.4.6\
Flask        2.3.2\
itsdangerous 2.2.0\
Jinja2       3.1.5\
MarkupSafe   3.0.2\
pip          25.0.1\
setuptools   75.8.0\
Werkzeug     3.1.3

=======================
#Check the Entry Point:
Run which angkor (on macOS/Linux) or where angkor (on Windows) to verify that the angkor command is correctly installed.

#Check the PYTHONPATH:
Ensure that the cli.py file is in the root directory and that Python can find it. If necessary, add the project root directory to the PYTHONPATH environment variable.

#Reinstall the Package:
Uninstall and reinstall the package in development mode:

bash\
pip uninstall angkor\
`pip install -e .`
