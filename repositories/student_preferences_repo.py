import os.path

from domain.student import Student
from domain.student_preference import StudentPreference


class StudentPreferencesRepository:
    preferences_file = '../data/2025_01.csv'

    def __init__(self):
        pass

    def get(self, curso=None):
        main_path = os.path.dirname(__file__)
        file_path = os.path.join(main_path, self.preferences_file)

        with open(file_path) as f:
            preferences_lines = f.readlines()
            preferences_lines.pop(0)
        students_preferences = list()

        for line in preferences_lines:
            line = line.replace('"', '')
            student_info = line.split(',')

            students_preferences.append(StudentPreference(student_info[1].strip(), student_info[2].strip(),
                                                student_info[3].strip(), student_info[4].strip()))

        return students_preferences

