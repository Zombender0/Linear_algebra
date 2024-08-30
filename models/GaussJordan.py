from models.Matrix import Matrix

class GaussJordan(Matrix):
    def __init__(self, matrix: list[list]) -> None:
        super().__init__(matrix)
    
    def gauss_jordan(self) ->None:
        for col in range(self.length):
            for row in range(col+1,self.width):
                if self.matrix[col][col] != 1: pass #continue here

    def diagonal_number_to_1(self,col,row):
        for i in range(col+1, self.length):
            if self.matrix[i][row] == 1:
                self.swap(col,row)

    def swap_rows(self):
        for col in range(0,self.length-1):
            for row in range(self.width):
                if self.matrix[col][col] == 1: break
                if self.matrix[row][col] ==1 and self.matrix[col][col] !=1:
                    print(self.matrix[row][col])
                    self.swap(col,row)

    def is_inconsistent(self,col):
        for row in range(self.width):
            if self.matrix[col][row] !=0:
                return False
        return True
        
    def eliminate_gauss_jordan(self,row,col):
        for col in range(self.length):
            pass

    def __str__(self) -> str:
        return super().__str__()