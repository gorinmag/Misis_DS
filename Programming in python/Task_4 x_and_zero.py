class Cell:
    def __init__(self, number):
        self.number = number  # Номер клетки
        self.occupied = False  # Занята ли клетка
        self.value = None  # Значение клетки ('X' или 'O')

    def occupy(self, player):
        if not self.occupied:
            self.occupied = True
            self.value = player.symbol  # Символ игрока ('X' или 'O')
            return True
        return False

    def __str__(self):
        return self.value if self.value else ' '  # Возвращаем символ или пробел


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]  # Создаем 9 клеток
        #Победные комбинации
        self.winning_combinations = [
            [0, 1, 2],  # горизонтальные
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],  # вертикальные
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],  # диагонали
            [2, 4, 6],
        ]

    def display(self):
        for i in range(0, 9, 3):
            print('|'.join(str(self.cells[j]) for j in range(i, i + 3)))
            if i < 6:
                print('-' * 5)

    def check_winner(self):
        for combo in self.winning_combinations:
            if (self.cells[combo[0]].value and
                    self.cells[combo[0]].value == self.cells[combo[1]].value == self.cells[combo[2]].value):
                return self.cells[combo[0]].value  # Возвращаем символ победителя
        return None  # Если победителя нет

    def is_full(self):
        return all(cell.occupied for cell in self.cells)  # Проверка на заполненность поля


class Player:
    def __init__(self, name, symbol):
        self.name = name  # Имя игрока
        self.symbol = symbol  # Символ игрока ('X' или 'O')


def main():
    print("Добро пожаловать в игру Крестики-нолики!")

    player1 = Player(input("Введите имя первого игрока (X): "), 'X')
    player2 = Player(input("Введите имя второго игрока (O): "), 'O')

    board = Board()
    current_player = player1

    while True:
        board.display()
        move = int(input(f"{current_player.name}, выберите номер клетки (1-9): ")) - 1

        if 0 <= move < 9 and board.cells[move].occupy(current_player):
            winner = board.check_winner()
            if winner:
                board.display()
                print(f"Поздравляем, {current_player.name}! Вы выиграли!")
                break
            if board.is_full():
                board.display()
                print("Игра закончилась вничью!")
                break
            current_player = player2 if current_player == player1 else player1
        else:
            print("Неверный ход, попробуйте снова.")


if __name__ == "__main__":
    main()