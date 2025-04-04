from random import randint

from adt_matrix import Matrix
from lifegrid import LifeGrid


def initialize_matrix(m: Matrix, min_val=0, max_val=10):
    for i in range(m.numRows()):
        for j in range(m.numCols()):
            m[i, j] = randint(min_val, max_val)


def print_matrix(m: Matrix):
    for i in range(m.numRows()):
        for j in range(m.numCols()):
            print(f"{m[i, j]}\t", end="")
        print()
    print()


def assignment_1_1():
    # ASSIGNMENT 1.1
    m1 = Matrix(2, 2)
    m2 = Matrix(2, 2)

    initialize_matrix(m1)
    initialize_matrix(m2)

    print_matrix(m1)
    print_matrix(m2)

    print("result of subtraction")
    m_sub = m1 - m2
    print_matrix(m_sub)


def assignment_1_2():
    # ASSIGNMENT 1.2
    m1 = Matrix(3, 2)
    m2 = Matrix(2, 2)

    initialize_matrix(m1)
    initialize_matrix(m2)

    print_matrix(m1)
    print_matrix(m2)

    print("result of multiplication")
    m_sub = m1 * m2
    print_matrix(m_sub)


def assignment_1_3():
    # ASSIGNMENT 1.2
    m1 = Matrix(3, 2)

    initialize_matrix(m1)

    print_matrix(m1)

    print("result of transpose")
    m_res = m1.transpose()
    print_matrix(m_res)


def assignment_2():
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(1, 3)
    life_grid.setCell(2, 2)
    life_grid.setCell(3, 1)

    life_grid.draw()
    print(life_grid.numLiveNeighbors(2, 2))


def assignment_4():
    # From left to right, and top to bottom
    # 1: dies out after 2 generations
    # 2: becomes an oscillator after generation 4
    # 3: dies out after generation 3
    # 4: dies out after generation 2
    # 5: dies out ofter generation 1
    # 6: becomes stable after generation 1
    # 7: is stable from the beginning

    # fig 1
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(1, 3)
    life_grid.setCell(2, 2)
    life_grid.setCell(3, 1)

    # fig 2
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(0, 0)
    life_grid.setCell(1, 1)
    life_grid.setCell(2, 2)
    life_grid.setCell(3, 3)
    life_grid.setCell(4, 4)
    life_grid.setCell(4, 0)
    life_grid.setCell(3, 1)
    life_grid.setCell(2, 2)
    life_grid.setCell(1, 3)
    life_grid.setCell(0, 4)

    # fig 3
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(0, 1)
    life_grid.setCell(1, 1)
    life_grid.setCell(2, 1)
    life_grid.setCell(3, 1)
    life_grid.setCell(4, 1)
    life_grid.setCell(4, 0)
    life_grid.setCell(0, 3)
    life_grid.setCell(1, 3)
    life_grid.setCell(2, 3)
    life_grid.setCell(3, 3)
    life_grid.setCell(4, 3)
    life_grid.setCell(4, 4)

    # fig 4
    life_grid = LifeGrid(5, 5)
    for i in range(5):
        for j in range(5):
            life_grid.setCell(i, j)

    # fig 5
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(0, 2)
    life_grid.setCell(1, 2)
    life_grid.setCell(2, 2)
    life_grid.setCell(3, 2)
    life_grid.setCell(4, 2)
    life_grid.setCell(2, 0)
    life_grid.setCell(2, 1)
    life_grid.setCell(2, 2)
    life_grid.setCell(2, 3)
    life_grid.setCell(2, 4)

    # fig 6
    life_grid = LifeGrid(5, 5)
    life_grid.setCell(0, 0)
    life_grid.setCell(0, 1)
    life_grid.setCell(1, 1)
    life_grid.setCell(0, 3)
    life_grid.setCell(0, 4)
    life_grid.setCell(1, 3)
    life_grid.setCell(4, 0)
    life_grid.setCell(4, 1)
    life_grid.setCell(3, 1)
    life_grid.setCell(4, 3)
    life_grid.setCell(4, 4)
    life_grid.setCell(3, 3)

    # fig 7
    life_grid = LifeGrid(13, 13)
    life_grid.setCell(0, 0)
    life_grid.setCell(0, 1)
    life_grid.setCell(1, 0)
    life_grid.setCell(1, 2)
    life_grid.setCell(3, 2)
    life_grid.setCell(3, 4)
    life_grid.setCell(5, 4)
    life_grid.setCell(5, 6)
    life_grid.setCell(7, 6)
    life_grid.setCell(7, 8)
    life_grid.setCell(9, 8)
    life_grid.setCell(9, 10)
    life_grid.setCell(11, 10)
    life_grid.setCell(11, 12)
    life_grid.setCell(12, 11)
    life_grid.setCell(12, 12)

    for i in range(10):
        print(f"Generation {i + 1}")
        life_grid.draw()
        life_grid.evolve()


if __name__ == '__main__':
    assignment_4()
