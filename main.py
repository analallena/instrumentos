# This is a sample Python script.
from raffle.raffle_handler import RaffleHandler
from repositories.cursos_repo import ClassGroupsRepository
import os.path


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def generate_fake_students(name):
    # Use a breakpoint in the code line below to debug your script.
    groups_repo = ClassGroupsRepository()
    groups = groups_repo.get()

    main_path = os.path.dirname(__file__)
    file_path = os.path.join(main_path, "s3_bucket_data/students_2024_2025.csv")

    with open(file_path, 'w') as f:
        f.write(f'Email, Curso\n')
        for group in groups:
            for i in range(0, 12):
                f.write("patata_{}_{}@instituto.com, {}\n".format(group.replace(' ', ''), i, group))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(f'Dentro de la funcion lambda')

    # print(f'What do you want to do?')
    # print(f'1 - Print instruments')
    # print(f'2 - Do raffle')
    #
    # resultado = input(f'Choose one: ')
    #
    # if resultado == '1':
    #     raffle = PrintInstruments(000)
    #     raffle.raffle(True)
    # if resultado == '2':

    # year_month = '2025_01'# input(f'Enter year and month: ')
    # handler = RaffleHandler(year_month)
    # handler.raffle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
