import os.path


class ClassGroupsRepository:
    cursos_file = '../data/cursos.csv'

    def __init__(self):
        pass

    def get(self):

        main_path = os.path.dirname(__file__)
        file_path = os.path.join(main_path, self.cursos_file)

        cursos = list()
        with open(file_path) as f:
            cursos_lines = f.readlines()

        for curso in cursos_lines:
            cursos.append(curso.strip())

        return cursos