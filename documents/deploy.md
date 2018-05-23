# System deployment tutorial

> For Gym Management System v1.0.0
> 2018.5.23

## Operating environment

1. Download & install `Python 3.6.5` or `Anaconda 5.1 (Python 3.6 version)`
  Download Links
  - [Python 3.6.5](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe)
  - [Anaconda 5.1](https://repo.anaconda.com/archive/Anaconda3-5.1.0-Windows-x86_64.exe)
2. Install or upgrade `pip` to version `10.0.1`
  - Use `python -m pip install --upgrade pip` command in `cmd`
3. Install software relevant rely
  This software need three python packages to run
  - django 2.0.4
  - pymysql == 0.8.0
  - mysqlclient == 1.3.12
  You can find the `requirements.txt` file then open the `cmd` at current directory and run this command: `pip install -r requirements.txt` (Please ensure that your account has system administrator privileges, Otherwise pip installation operation may fail)

## Run the software

Find the `manage.py` under the `sourcecode` directory, and then run this file with a parameters

command: `python manage.py runserver`
