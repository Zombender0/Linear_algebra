from models.GaussJordan import GaussJordan 

matrix = [[1,4,-2,8,12],[0,1,-7,2,-4],[0,0,5,-1,7],[0,0,1,3,-5]]
if not GaussJordan._valid_matrix(matrix):
    exit(0)
m = GaussJordan(matrix)
m.gauss_jordan(True)
print(m)