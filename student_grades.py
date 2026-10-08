"""Student Grade Management System."""


class Student:
    """A student with an ID, a name and a list of grades."""

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """Add a grade to the student."""
        self.grades.append(grade)

    def calculate_average(self):
        """Return the average of the grades."""
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

    def check_honor(self):
        """Mark the student for honor roll if the average is above 90."""
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Delete the grade at the given index."""
        del self.grades[index]

    def report(self):
        """Print the student report."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def main():
    """Run the program."""
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)
    student.report()


if __name__ == "__main__":
    main()
