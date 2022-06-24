class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['🍀' * rows for _ in range(self.nums // rows)]) + '\n' + '🍁' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Summ of cell is:')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subsrtaction of cell is:')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше, чем во второй. Вычитание невозможно!"

    def __mul__(self, other):
        print('Multiply of cell is:')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Truediv of cell is:')
        return Cell(self.nums // other.nums)
