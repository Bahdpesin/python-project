# Assigment on Creating a Python Directory
students = {
    "student1": {"name": "John Doe", "age": 16, "grade": "A"},
    "student2": {"name": "Mary James", "age": 17, "grade": "B"},
    "student3": {"name": "Alex Brown", "age":15, "grade": "C"}
}
# print all student records
for key, record in students.items():
    print(f"{key}: {record}")
