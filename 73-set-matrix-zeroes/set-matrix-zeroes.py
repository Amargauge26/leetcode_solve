class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr=[]
        for i in  range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    arr.append((i,j))
        #return matrix

        for i,j in arr:
            for n in range(len(matrix)):
                matrix[n][j]=0
            for n in range(len(matrix[0])):
                matrix[i][n]=0
        

        return matrix
