# Intro to Django Live Training
This is the code for the *O'Reilly Live Training* - **Intro to Django** presented by Arianne Dee

**Note**: If you're looking for the project code for a specific date in the past,
look for the specific class [here](https://github.com/ariannedee/intro-to-django/releases)

Before the class, please follow these instructions:
1. [Install Python](#1-install-python-36-or-higher)
1. [Check that Python was installed properly](#2-make-sure-that-python-is-properly-installed)
1. [Choose an IDE](#3-choose-an-ide)
1. [Download the code](#4-download-the-course-files)
1. [Create a virtual environment](#5-create-a-virtual-environment)
1. [Install Django](#6-install-django)
1. [Download the resources](#7-at-the-beginning-of-class-download-the-resources)

## Set up instructions
Please complete these steps prior to the course.
Email 
[arianne.dee.studios@gmail.com](mailto:arianne.dee.studios@gmail.com)
if you have any questions.
### 1. Install Python 3.6 or higher

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
Follow the instructions here: [Windows Python installer instructions](docs/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 2. Make sure that Python is properly installed
1. Open the *Command Prompt* application in Windows
   or *Terminal* on Mac or Linux

1. Type `python --version` and press enter

1. Type `python3 --version` and press enter

1. One or both of those commands should print
   a Python version of 3.6 or higher
   (whichever version you just downloaded).
   If it doesn't, you have to follow instructions to
   [add Python to your PATH variable](docs/WINSETPATH.md).

**Note:**
You can now type just the `python` or `python3` command
in *Command Prompt* or *Terminal*
to run the Python interpreter.
You can also run a *.py* file by running
`python filename.py`

### 3. Choose an IDE
**PyCharm** or **VS Code** are recommended.

For Django development, I recommend using **PyCharm Professional Edition** (paid).
There is a 30-day free trial if you would like to try it out.

In the course I'll be using the free **PyCharm Community Edition**
but will demo a couple of useful features in the professional edition.


Download here either version here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 4. Download the course files
If you're viewing this on GitHub already, stay on this page.
Otherwise, go to the GitHub repository: https://github.com/ariannedee/intro-to-django

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
   - **PowerShell**: `venv\Scripts\Activate.ps1`
   - **CommandPrompt**: `venv\Scripts\activate.bat`

If you are new to virtual environments, please watch this 
[video lesson](https://learning.oreilly.com/videos/next-level-python/9780136904083/9780136904083-NLP1_01_03_03/)

### 6. Install Django
Once your virtual environment has been activated, install Django 3 using pip:
- `pip install django` to install the latest version of Django
  
**OR**
- `pip install "django>=3.0,<4"` to install the latest Django 3 version (once version 4 is released)

### 7. At the beginning of class, download the resources
When you have signed in to the class,
download the PDF files in the **Resources** widget.

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
    - To find where Python is located, [look in these directories](docs/PATH_LOCATIONS.md)
    - You may have to search the internet for where Python gets installed by default on your operating system

### Do you offer private Python help?
Not at the moment, as I am currently taking care of a new human.

If you might be interested in some private training for the future, email 
[**arianne.dee.studios@gmail.com**](mailto:arianne.dee.studios@gmail.com) 
so that I can inform you when I start taking on new clients.
