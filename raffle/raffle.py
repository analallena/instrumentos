import random
import logging


class Raffle:
    def __init__(self, students, year_month, student_preferences):
        self.students = list(students)
        self.year_month = year_month
        self.students = student_preferences
        self.logger = logging.getLogger('tipper')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

    def raffle(self):
        available = self.students.copy()
        for student in self.students:
            index = self.get_index(student, available)

            if index >= 0:
                # self.logger.debug("{} gifts to {}".format(person.name, available[index].name))
                student.assi = available[index].name
                available.pop(index)

                if len(available) == 1 and \
                        (available[0].name == self.people[-1].name
                         or available[0].name in self.people[-1].excluded):
                    # self.logger.debug("--------------------------------------------------------------\n\nRUNNING AGAIN")
                    return self.raffle()
            else:
                return self.raffle()

        with open('./data/RAFFLE {0}.csv'.format(self.year), 'a') as f:
            f.write('Giver, Receiver\n')
            for person in self.people:
                f.write('{}, {}\n'.format(person.name, person.giftsTo))
        return self.people

    def get_index(self, person, available):
        trying = 0
        index = random.randint(0, len(available) - 1)
        # self.logger.debug("index: {} available: {}".format(index, available))

        while trying < 3 and (available[index].name == person.name\
                or available[index].name in person.excluded):
            trying += 1
            index = random.randint(0, len(available) - 1)
            # self.logger.debug("calculated new index: {}".format(index))

        if trying >= 3:
            return -1

        return index


