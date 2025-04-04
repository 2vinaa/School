# Implements the LifeGrid ADT for use with the game of Life.
from adt_array import Array2D


class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1  # Creates the game grid and initializes the cells to dead.

    def __init__(self, numRows, numCols):
        # Allocate the 2-D array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cells to dead.
        self.configure(list())

    # Returns the number of rows in the grid.
    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure(self, coordList):

        # Clear the game grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Returns the number of live neighbors for the given cell.
    def numLiveNeighbors(self, row, col):
        neighbours = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):

                # if outside limits
                if i < 0 or i >= self.numRows() or j < 0 or j >= self.numCols():
                    continue

                # ignore when selecting the target cell
                if i == row and j == col:
                    continue

                if self.isLiveCell(i, j):
                    neighbours += 1
        return neighbours

    # assignment 3
    def draw(self):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print("#\t" if self.isLiveCell(i, j) else ".\t", end="")

            print("")
        print("")

    # assignment 4
    # Generates the next generation of organisms.
    def evolve(self, generations=1):
        # List for storing the live cells of the next generation.
        liveCells = list()

        # Iterate over the elements of the grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                # Determine the number of live neighbors for this cell.
                neighbors = self.numLiveNeighbors(i, j)

                # Add the (i,j) tuple to liveCells if this cell contains
                # a live organism in the next generation.

                if (neighbors == 2 and self.isLiveCell(i, j)) or (neighbors == 3):
                    liveCells.append((i, j))

        # Reconfigure the grid using the liveCells coord list.
        self.configure(liveCells)
