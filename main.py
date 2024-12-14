# This is a sample Python script.
from raffle_handler import RaffleHandler


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
        year_month = '2025_01'# input(f'Enter year and month: ')
        handler = RaffleHandler(year_month)
        handler.raffle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
