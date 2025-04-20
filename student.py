# student.py

class Student:
    def __init__(self, roll, name, marks, grade):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.grade = grade

    def to_line(self):
        # Converts student object to string for saving in file
        return f"{self.roll},{self.name},{self.marks},{self.grade}\n"

    @staticmethod
    def from_line(line):
        # Converts line from file into a Student object
        data = line.strip().split(',')
        return Student(data[0], data[1], data[2], data[3])
