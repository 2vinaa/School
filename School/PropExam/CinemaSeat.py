from multarr import Array2D
import random

class Seat:
    def __init__(self, val:bool):
        self.is_occupied = val

    def __str__(self):
        if self.is_occupied is True:
            return "Occupied"
        else:
            return "Available"

class CinemaGrid:

    def __init__(self, row, cols):
        self.grid = Array2D(numRows=row, numCols= cols)

    def fill_cinema(self):
        for i in range(self.grid.numRows()):
            for j in range(self.grid.numCols()):
                x = bool(random.randint(0,1))
                self.grid[i,j] = Seat(x)


    def check_occupancy(self, row, col):
        if not self.grid[row, col]:
            return f"The seat in position {row},{col} is available"
        elif self.grid[row, col]:
            return f"The seat in position {row},{col} is not available"


    def mark_occupancy(self, row, col):
        if self.grid.__getitem__([row, col]):
            self.grid.__setitem__([row,col], Seat(True))
            return f"The occupancy has been set in {row},{col}"
        else:
            return f"The occupancy has not been set in {row},{col} as it was already occupied"


    def available_seat_counter(self):
        counter = 0
        for i in range(self.grid.numRows()):
            for j in range(self.grid.numCols()):
                if self.grid.__getitem__([i,j]):
                    counter += 1
        return f"The available seats are : {counter}"

    def __str__(self):
        result = ''
        for i in range(self.grid.numRows()):
            row = []
            for j in range(self.grid.numCols()):
                seat = self.grid.__getitem__([i, j])
                row.append(str(seat))  # Use the string representation of the Seat object
            result += ' '.join(row) + '\n'
        return result






if __name__ == "__main__":

    odi = CinemaGrid(10, 15)



    odi.fill_cinema()

    # Example of checking occupancy of a specific seat
    print(odi.check_occupancy(3, 5))  # Check the seat at position (3, 5)

    # Example of marking occupancy
    print(odi.mark_occupancy(3, 5))  # Mark the seat at position (3, 5)


    # Example of available seats count
    print(odi.available_seat_counter())  # Count the available seats

    print(odi)

