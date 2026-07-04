from tools.system_tool import get_system_status
from tools.app_tool import open_app

while True:
    command = input("Jarvis > ").lower()

    if command == "exit":
        break

    elif command == "status":
        status = get_system_status()
        print(f"CPU : {status['cpu']}%")
        print(f"RAM : {status['ram']}%")
        print(f"DISK: {status['disk']}%")

    elif command.startswith("open "):
        app = command.replace("open ", "")
        print(open_app(app))

    else:
        print("Unknown command.")