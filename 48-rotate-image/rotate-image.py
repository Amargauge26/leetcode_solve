class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ilen= len(matrix)
        jlen=len(matrix[0])
        mm =[[0 for i in range(jlen)] for _ in range(ilen) ]
        arr=[]
        for j in range(jlen):
            temp=[]
            for i in range(ilen-1,-1,-1):
                temp.append(matrix[i][j])
            
            arr.append(temp)
        
        for i  in range(ilen):
            matrix[i]=arr[i]
        
        return matrix
