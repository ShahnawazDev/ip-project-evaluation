import sys  # MUST NOT be removed

class Course:
    def __init__(self, courseID, credit):
        self.courseID = courseID
        self.credit = credit

    # Add more functions if necessary


class EnrolledSemester:
    def __init__(self, sem_id):
        self.id = sem_id
        self.courses = []  # list of Course objects

    # Add more functions if necessary


class Grades:
    def __init__(self):
        self.grades = {}  # key: (semester_obj, course_obj) -> grade

    # Add more functions if necessary


class Student:
    def __init__(self, roll, name, dob, branch):
        self.__roll = roll
        self.__name = name
        self.__dob = dob
        self.__branch = branch
        self.__semesters = []   # list of EnrolledSemester objects
        self.__grades = Grades()

    def getResult(self):
        # TODO: Implement this
        pass

    # Add more functions if necessary


def build_students(record):
    """
    Input: takes a dictionary as input
    Process: creates and populates objects
    Output: returns a list of Student objects
    """
    # TODO: Implement this
    pass

#### Main part of the code - DO NOT CHANGE beyond this point ####

def read_input_dictionary():
    raw = ""
    for line in sys.stdin:
        raw += line.strip() + " "
    return eval(raw)


def main():
    record = read_input_dictionary()
    students = build_students(record)

    output = []
    for stu in students:
        output.append(stu.getResult())

    print(output)


if __name__ == "__main__":
    main()