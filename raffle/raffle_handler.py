from repositories.cursos_repo import ClassGroupsRepository
from repositories.instruments_repo import InstrumentsRepository
from raffle import Raffle
from repositories.student_preferences_repo import StudentPreferencesRepository


class RaffleHandler:

    def __init__(self, year):
        self.year = year

    def raffle(self):
        repo = InstrumentsRepository()
        instruments = repo.get()

        repo = ClassGroupsRepository()
        class_groups = repo.get()

        repo = StudentPreferencesRepository()
        student_preferences = repo.get()

        raffle = Raffle(instruments, class_groups, student_preferences)
        raffle.raffle()


