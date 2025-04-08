from adt_array import Array2D

class MagicSquare:
    def __init__(self, n, rotation=0):
        """
        Initialize magic square with given size and orientation.
        n must be odd.
        Orientation can be 0,90,180,270
        """
        self.n = n
        self.rotation = rotation
        self.magic_sq = Array2D(self.n, self.n)


    def fill(self):
        i = 0
        j = self.n // 2
        number = 0

        for element in range(self.n * self.n):
            if self.magic_sq[i,j] is None:
                self.magic_sq.__setitem__([i,j], number+1)
            if self.magic_sq[i,j] is not None:
                if i == self.n-1:
                    i = 0
                    i = i+1
                else:
                    i = i +2
                if j == self.n-1:
                    j = 0
                else:
                    j = j-1
            self.magic_sq.__setitem__([i,j], number+1)

            i -=1
            if i < 0:
                i = self.n-1
            else:
                pass
            j = j+1
            if j > self.n - 1:
                j = 0


    def _apply_rotation(self):
        """Internal method to handle rotation transformations"""
        pass

    def print(self):
        return f"{str({self.magic_sq})}"

    def get_square(self):
        return f"{str({self.magic_sq})}"

    def check(self, matrix):


        pass


if __name__ == "__main__":
    print("Standard 3x3 Magic Square (0° rotation):")
    ms0 = MagicSquare(3)
    ms0.print()
    print("Is a valid magic square?", ms0.check(ms0.get_square()))
    ms0.fill()
    ms0.print()
    print("Is a valid magic square?", ms0.check(ms0.get_square()))

    print("\n90° Rotated 3x3 Magic Square:")
    ms90 = MagicSquare(3, 90)
    ms90.fill()
    ms90.print()
    print("Is a valid magic square?", ms0.check(ms90.get_square()))

    print("\n180° Rotated 5x5 Magic Square:")
    ms180 = MagicSquare(5, 180)
    ms180.fill()
    ms180.print()
    print("Is a valid magic square?", ms0.check(ms180.get_square()))

    print("\n270° Rotated 5x5 Magic Square:")
    ms270 = MagicSquare(5, 270)
    ms270.fill()
    ms270.print()
    print("Is a valid magic square?", ms270.check(ms0.get_square()))

    # Verification test
    print("\nVerification Tests:")
    test_square = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    print("Is valid magic square?", ms0.check(test_square))

    invalid_square = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 1]
    ]
    print("Is invalid square magic?", ms0.check(invalid_square))