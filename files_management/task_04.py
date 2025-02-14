import csv

filename = "students.csv"

students_data = [
    ["Name", "Age", "Grade"],
    ["Alice", 25, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 24, "A"]
]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print(f"File '{filename}' created.")

ages = []
print("\nFile content:")
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader[1:]:
        name, age, grade = row
        age = int(age)
        ages.append(age)
        print(f"Name: {name}, Age: {age}, Grade: {grade}")

average_age = sum(ages) / len(ages)
print(f"\nAverage Age: {average_age:.2f}")
