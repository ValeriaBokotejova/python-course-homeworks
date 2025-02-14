from datetime import datetime

filename = "log.txt"

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(filename, "a+", encoding="utf-8") as file:
    if file.tell() == 0:
        print(f"{filename} created.")
    
    file.write(current_time + "\n")
    print(f"Appended: {current_time}")

with open(filename, "r", encoding="utf-8") as file:
    print("\nFile content:")
    print(file.read())
