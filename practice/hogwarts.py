"""#Looping thru a list
students = ['Hermione', 'Harry', 'Ron']

for i in range(len(students)):
    print(i + 1, students[i])

# Dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry":" Gryffindor",
    "Ron": "Gryffindor" ,
    "Draco": "Slytherin"
    }

for student in students:
    print(student, students[student])"""

#list of dictionaries, #None
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherine", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")