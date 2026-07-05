class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0]*(cols+1) for _ in range(rows+1)]

        for row in range(rows):
            self.prefix[row][0] = matrix[row][0]
            for col in range(1,cols):
                self.prefix[row][col] = self.prefix[row][col-1] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2+1):
            if col1 > 0:
                total += self.prefix[row][col2] - self.prefix[row][col1-1]
            else:
                total += self.prefix[row][col2]
        return total


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)