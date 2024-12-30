import os.path

from repositories.student_preferences_repo import StudentPreferencesRepository


class Instrument:
    def __init__(self, name):
        self.name = name
        self.available = True


class InstrumentsRepository:
    students_file = '../s3_bucket_data/students_2024_2025.csv'

    def __init__(self):
        pass

    def get(self, curso=None):
        main_path = os.path.dirname(__file__)
        file_path = os.path.join(main_path, self.students_file)

        with open(file_path) as f:
            student_lines = f.readlines()
            student_lines.pop(0)

        students = list()

        student_preferences_repo = StudentPreferencesRepository()
        student_preferences = student_preferences_repo.get(curso)

        for student_line in student_lines:
            student = student_line.split(',')
            student_email = student[0].strip()
            student_group = student[1].strip()

            student_preferences

        return students

