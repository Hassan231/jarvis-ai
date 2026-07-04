import os

def open_app(app_name):
    apps = {
        "notepad": "notepad",
        "calculator": "calc",
        "chrome": "start chrome",
        "vscode": "code"
    }

    if app_name in apps:
        os.system(apps[app_name])   
        return f"Opening {app_name}..."
    else:
        return f"I don't know how to open {app_name}."