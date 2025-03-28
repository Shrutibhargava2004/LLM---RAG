import os
import webbrowser
import psutil

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_file_explorer():
    os.system("explorer")

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_ram_usage():
    memory_info = psutil.virtual_memory()
    return f"RAM Usage: {memory_info.percent}%"

def execute_command(command):
    try:
        result = os.popen(command).read()
        return result if result else "Command executed successfully."
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(open_chrome())
    print(open_calculator())
    print(open_notepad())
    print(open_file_explorer())
    print(get_cpu_usage())
    print(get_ram_usage())
    print(execute_command("echo Hello, World!"))
