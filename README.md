# Intro to Django
This is the code for the *O'Reilly Video* - **Intro to Django** presented by Arianne Dee

## Course setup

1. [Install Python 3.11](#1-install-python-311)
1. [Check that Python was installed properly](#2-make-sure-that-python-is-properly-installed)
1. [Choose an IDE](#3-choose-an-ide)
1. [Download the code](#4-download-the-course-files)
1. [Create a virtual environment](#5-create-a-virtual-environment)
1. [Install Django](#6-install-django)

## Set up instructions
Feel free to email me at
[arianne.dee.studios@gmail.com](mailto:arianne.dee.studios@gmail.com)
if you are having any problems getting set up for the course.

### 1. Install Python 3.11

This course uses Python 3.11, but Python 3.8 and higher should work.

The course uses Django 4.2,
so check which Python versions are compatible with 
Django 4.2 [here](https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support).

#### To install the latest version of Python:
1. Go to https://www.python.org/downloads/
1. Click the yellow button at the top to download the latest version of Python.

#### On Mac or Linux
Follow the prompts and install using the default settings.

#### On Windows
The default settings don't add Python to your PATH
so your computer doesn't know where to look for it when Python runs
(for some inexplicable reason).

##### If you're just installing Python now
Follow the instructions here: [Windows Python installer instructions](docs/install/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/install/WINSETPATH.md)

### 2. Make sure that Python is properly installed
1. Open the *PowerShell* application in Windows
   or *Terminal* on Mac or Linux

1. Type `python --version` and press enter
2. Type `python3 --version` and press enter
3. Type `py --version` and press enter

At least one of those commands should print
a Python version of 3.8 or higher
(whichever version you just installed).
If it doesn't, you have to follow instructions to
[add Python to your PATH variable](docs/install/WINSETPATH.md).

### 3. Choose an IDE
**PyCharm** or **VS Code** are recommended.

For Django development, I recommend using **PyCharm Professional Edition** (paid).
There is a 30-day free trial if you would like to try it out.

In the video I use the free **PyCharm Community Edition**, which is sufficient.

Download either version here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 4. Download the course files

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the green "Code" button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **intro-to-django-main** folder to a convenient location

### 5. Create a virtual environment
1. In your console, navigate to the project folder (if you open the project in PyCharm or VSCode, the Terminal pane should already be located there)
2. Using the python command from step 2, create a virtual environment
`python -m venv django_venv` or `python3 -m venv django_venv`
3. Activate your virtual environment
   - **Mac/Linux**: `source django_venv/bin/activate`
   - **PowerShell**: `django_venv\Scripts\Activate.ps1`

If you are new to virtual environments, please watch this 
[video lesson](https://learning.oreilly.com/videos/next-level-python/9780136904083/9780136904083-NLP1_01_03_03/)

### 6. Install Django
Once your virtual environment has been activated, install Django 3 using pip:
- `pip install django` to install the latest version of Django
  
**OR**
- `pip install "django>=4.2,<5"` to install the latest Django 4.2 version (once version 5+ is released)

## FAQs
### Can I use Python 2?

No. Django 3, does not support Python 2 or Python < 3.6.

### PyCharm can't find Python 3

On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
1. Go to **Project: intro-to-django** > **Project Interpreter**
1. Look for your Python version in the Project Interpreter dropdown
1. If it's not there, click **gear icon** > **Add...**
1. In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
1. If it's not there, click the **...** button and navigate to your Python location
    - To find where Python is located, [look in these directories](docs/install/PATH_LOCATIONS.md)
    - You may have to search the internet for where Python gets installed by default on your operating system

### How do I set up my IDE to use Django?
Here are some links to configure your Django project in the following IDEs
- [PyCharm Professional](docs/config/PyCharm_Pro.md)
  - My IDE of choice for working in Django
- [PyCharm Community](docs/config/PyCharm_Com.md)

- [VS Code](docs/config/VSCode.md)

---

## Django Trivia local setup instructions

1. Navigate into the `trivia_site` folder
2. Create a virtual environment with Python 3.8+
3. Activate your virtual environment
4. `$ pip install -r requirements/local.txt` to install local requirements
5. `$ python manage.py migrate` to migrate your database
6. `$ python manage.py createsuperuser` and follow instructions
7. `$ python manage.py loaddata questions` to add seed data
8. `$ python manage.py runserver` to run the development server

---


## Questions or comments?

Email me at  
[**arianne.dee.studios@gmail.com**](mailto:arianne.dee.studios@gmail.com) 
or submit an issue or pull request to this repository.