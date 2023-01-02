"""566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of
the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as
they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output
the original matrix.
Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        curr_row = len(mat)
        curr_col = len(mat[0])
        print(curr_row, curr_col)
        if curr_row * curr_col != r * c:
            return mat

        elements = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                elements.append(mat[i][j])
        result = []
        k = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(elements[k])
                k += 1
            result.append(temp)

        return result