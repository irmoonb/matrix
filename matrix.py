import random
import time
from bisect import bisect_left

class Matrix:
    """
    Class to represent a 2D matrix with:
    - print, row/col display, row sum/avg
    - sort (row-wise), min/max, find value
    - set element, set all, randomize
    - rotation (transpose)
    """

    def __init__(self, rows, cols, init_val=0):
        if rows < 2 or cols < 2:
            raise ValueError("Rows and/or columns must be at least 2.")
        self.rows = rows
        self.cols = cols
        self.is_sorted = False
        self.matrix = [[init_val for _ in range(cols)] for _ in range(rows)]

    def print_matrix(self):
        for row in self.matrix:
            print("[ " + " ".join(str(x) for x in row) + " ]")

    def print_row(self, row):
        if 0 <= row < self.rows:
            print(" ".join(str(x) for x in self.matrix[row]))

    def print_column(self, col):
        if 0 <= col < self.cols:
            for i in range(self.rows):
                print(self.matrix[i][col], end=" ")
            print()

    def row_sum(self, row):
        if 0 <= row < self.rows:
            return sum(self.matrix[row])
        return 0

    def row_average(self, row):
        if 0 <= row < self.rows:
            return float(self.row_sum(row)) / self.cols
        return 0.0

    def min(self):
        return min(min(row) for row in self.matrix)

    def max(self):
        return max(max(row) for row in self.matrix)

    def sort_matrix(self):
        for row in self.matrix:
            row.sort()
        self.is_sorted = True

    def set_element(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
            self.is_sorted = False

    def set_matrix(self, value):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = value
        self.is_sorted = False

    def randomize_matrix(self, lower, upper):
        random.seed(time.time())
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.randint(lower, upper)
        self.is_sorted = False

    def find_value(self, value):
        for row in self.matrix:
            if self.is_sorted:
                # Binary search (requires sorted rows)
                idx = bisect_left(row, value)
                if idx < self.cols and row[idx] == value:
                    return True
            else:
                if value in row:
                    return True
        return False

    def rotate_matrix(self):
        # Transpose the matrix (swap rows/columns)
        self.matrix = [list(row) for row in zip(*self.matrix)]
        self.rows, self.cols = self.cols, self.rows
        self.is_sorted = False


if __name__ == "__main__":
    try:
        mat = Matrix(7, 3, 1)  # 7 rows, 3 columns, elements = 1
        print("\nSetting matrix to have 7 rows, and 3 columns of 1.")
        mat.print_matrix()
        print()

        mat.set_element(1, 2, 5)
        print("Testing set_element")
        print("Matrix after setting element (1, 2) to 5")
        mat.print_matrix()
        print()

        mat.set_matrix(10)
        print("Testing set_matrix")
        print("Matrix after setting all elements to 10:")
        mat.print_matrix()
        print()

        mat.randomize_matrix(0, 100)
        print("Testing randomize_matrix")
        print("Matrix after randomizing elements between 0 and 100:")
        mat.print_matrix()
        print()

        value_to_find = 5
        is_found = mat.find_value(value_to_find)
        print("Testing find_value: 5 (Linear Search because it has not been sorted yet)")
        print(f"Value {value_to_find} {'found' if is_found else 'not found'} in the matrix.")
        print()

        mat.sort_matrix()
        print("Testing sort_matrix")
        print("Matrix after sorting:")
        mat.print_matrix()
        print()

        print("Testing print_row")
        print("Printing row 1:")
        mat.print_row(0)  # 0 = row 1
        print()

        row_sum = mat.row_sum(0)
        print("Testing row_sum")
        print(f"Sum of elements in row 1: {row_sum}")
        print()

        print("Testing print_column")
        print("Printing column 2:")
        mat.print_column(1)  # 0 = column 1, 1 = column 2
        print()

        row_average = mat.row_average(0)
        print("Testing row_average")
        print(f"Average of elements in row 1: {row_average}")
        print()

        min_value = mat.min()
        print("Testing min_value")
        print(f"Minimum value in the matrix: {min_value}")
        print()

        max_value = mat.max()
        print("Testing max_value")
        print(f"Maximum value in the matrix: {max_value}")
        print()

        # Test binary search after sort
        is_found = mat.find_value(value_to_find)
        print("Testing find_value: 5 (Binary Search after sort)")
        print(f"Value {value_to_find} {'found' if is_found else 'not found'} in the matrix.")
        print()

        print("Testing rotate_matrix")
        print("Matrix before rotating:")
        mat.print_matrix()
        print()
        mat.rotate_matrix()
        print("Matrix after rotating:")
        mat.print_matrix()
        print()

    except Exception as e:
        print(str(e))