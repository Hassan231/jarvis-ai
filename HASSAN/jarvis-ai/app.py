from tools.system_tool import get_system_status

while True:
    command = input("Jarvis > ").lower()

    if command == "exit":
        break

    elif command == "status":
        status = get_system_status()

        print(f"CPU : {status['cpu']}%")
        print(f"RAM : {status['ram']}%")
        print(f"DISK: {status['disk']}%")

    else:
        print("Unknown command.")