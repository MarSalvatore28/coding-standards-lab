"""Student Grade Management System.

Creates student records, stores numeric grades and calculates the
average, letter grade and pass/fail status of each student.
Invalid input never crashes the program; a clear error message is shown.
"""

MIN_GRADE = 0.0
MAX_GRADE = 100.0
PASSING_AVERAGE = 60.0

# (minimum average, letter) ordered from highest to lowest.
LETTER_THRESHOLDS = (
    (90.0, "A"),
    (80.0, "B"),
    (70.0, "C"),
    (60.0, "D"),
)
FAILING_LETTER = "F"


class InvalidInputError(ValueError):
    """Raised when a student field or grade is not valid."""


class Student:
    """A student with an ID, a name and a list of numeric grades."""

    def __init__(self, student_id, name):
        self.student_id = self._validate_text(student_id, "Student ID")
        self.name = self._validate_text(name, "Student name")
        self.grades = []

    @staticmethod
    def _validate_text(value, field_name):
        """Return the stripped value, or raise if it is empty or not text."""
        if not isinstance(value, str) or not value.strip():
            raise InvalidInputError(f"{field_name} must be a non-empty text.")
        return value.strip()

    @staticmethod
    def _validate_grade(grade):
        """Return the grade as float, or raise if it is not valid."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise InvalidInputError(f"Grade '{grade}' is not a number.")
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise InvalidInputError(
                f"Grade {grade} is out of range ({MIN_GRADE:g}-{MAX_GRADE:g})."
            )
        return float(grade)

    def add_grade(self, grade):
        """Add a numeric grade between 0 and 100."""
        self.grades.append(self._validate_grade(grade))

    def calculate_average(self):
        """Return the average of the grades, or 0.0 if there are none."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        """Return the letter grade (A-F) for the current average."""
        average = self.calculate_average()
        for minimum, letter in LETTER_THRESHOLDS:
            if average >= minimum:
                return letter
        return FAILING_LETTER

    def has_passed(self):
        """Return True if the average is 60 or higher."""
        return self.calculate_average() >= PASSING_AVERAGE

    def report(self):
        """Return a formatted report with the student's results."""
        status = "Passed" if self.has_passed() else "Failed"
        lines = (
            f"ID: {self.student_id}",
            f"Name: {self.name}",
            f"Grades Count: {len(self.grades)}",
            f"Average: {self.calculate_average():.2f}",
            f"Final Grade: {self.letter_grade()}",
            f"Status: {status}",
        )
        return "\n".join(lines)


def create_student(student_id, name):
    """Create a student, or show an error and return None if invalid."""
    try:
        return Student(student_id, name)
    except InvalidInputError as error:
        print(f"Error: {error}")
        return None


def safe_call(action, *args):
    """Run a student action and show a clear message if the input is bad."""
    try:
        action(*args)
    except InvalidInputError as error:
        print(f"Error: {error}")


def main():
    """Demonstrate the core requirements."""
    print("--- Invalid students ---")
    create_student("", "Ana")
    create_student("S-002", None)

    student = create_student("S-001", "Ana Torres")
    if student is None:
        return

    print("--- Adding grades ---")
    for grade in (95.0, 88.5, 100, 72.5):
        safe_call(student.add_grade, grade)
    safe_call(student.add_grade, "Fifty")
    safe_call(student.add_grade, 150)

    print(student.report())


if __name__ == "__main__":
    main()
