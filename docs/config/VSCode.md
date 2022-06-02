# Setting up Django in PyCharm Community
- [Installing extensions](#installing-extensions)
- [Linking your virtual environment](#linking-your-virtual-environment)
- [Configure run settings](#set-up-a-run-configuration-file)
- [Debugging](#debugging)

## Installing extensions

Make sure you have the Python extension by Microsoft.

   <img width="60%" src="../img/vscode_extension.png">

## Linking your virtual environment

### 1. Select the Python interpreter from the bottom toolbar

   <img width="60%" src="../img/vscode_venv_1.png">

### 2. Enter the location of your Python interpreter in your virtual environment

   <img width="60%" src="../img/vscode_venv_2.png">

On Windows, this will be `.\venv\Scripts\python.exe`

## Set up a run configuration file

### 1. Go to the **Run and Debug** view

   <img width="60%" src="../img/vscode_django_1.png">

### 2. Create a `launch.json` file

   <img width="60%" src="../img/vscode_django_2.png">

### 3. Select Django

   <img width="60%" src="../img/vscode_django_3.png">

### 4. Enter the path to `manage.py`

   <img width="60%" src="../img/vscode_django_4.png">

For our sample project, it will be `${workspaceFolder}/trivia_site/manage.py`

   <img width="60%" src="../img/vscode_django_5.png">

Hit Enter

### 5. Review `launch.json` settings

   <img width="60%" src="../img/vscode_django_6.png">

You can always go back here to edit your run configuration settings.

Notice that `"args"` contains `"runserver"`, since you normally run the command `python manage.py runserver`.

### 6. Run the development server

   <img width="60%" src="../img/vscode_django_7.png">

Now you can click on the run button to use the Django settings you've just configured.

### 7. Switch between consoles in the right sidebar

   <img width="60%" src="../img/vscode_django_8.png">

This will run the development server in the terminal in a tab called Python Debug Console.

Navigate to the **bash** tab to get back to your Terminal console.

## Debugging

### 1. Run the development server using the Django configuration

Follow the steps above to run Django in debug mode

   <img width="60%" src="../img/vscode_django_7.png">

### 2. Set breakpoints in your code

   <img width="60%" src="../img/vscode_debug_1.png">


### 3. Debug using the debugger

   <img width="60%" src="../img/vscode_debug_2.png">

Use the buttons at the top to debug your code from the current breakpoint.

Navigate to the **Debug Console** tab at the bottom to get to evaluate expressions in your current debugger context.

