'''
Created on 2014 3 3

@author: Student
'''
import unittest
from random import randint

class PieceError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Piece():
    def __init__(self, row=None,col=None):
        '''
        Raises PieceError
            if row != col
        '''
        self.row = 0
        self.column = 0
        if row is not None and col is not None:
            if row == col:
                self.length = row
                self.initialize(row, col)
            else:
                raise Exception("Piece must be a square Matrix")
    
    def __len__(self):
        return len(self._matrix)

    def initialize(self, row, column):
        '''
        a function that can will initialize the
        piece to be row*column of zeros
        Parameters:
            row: the row dimension
            column: the column dimension
        Return
            None
        Raises PieceError
            if row != col
        '''
        if row > 0 and column > 0 and row == column:
            self._matrix = []
            r = 0
            self.length = row
            self.column = 0
            self.row = 0
            while r < row:
                c = 0
                rw = []
                while c < column:
                    rw.append(0)
                    c += 1
                self._matrix.append(rw)
                r+=1
        else:
            raise PieceError("Piece must be a square Matrix")

    def get_start(self):
        '''
        a function that gets the pieces starting positions
        Parameters:
            None
        Returns:
            x: the starting x position
            y: the starting y position
        '''
        return self.row, self.column

    def get_length(self):
        '''
        a function that returns the length of one dimension of the piece
        Parameters:
            None
        Returns:
            n: the length of one dimension of the piece
        '''
        return self.length

    def move_right(self):
        '''
        a function that moves the piece right if possible
        Parameters:
            None
        Returns:
            True if moved
            False otherwise
        '''
        if self.check_column_empty(self.length-1):
            r = 0
            while r < self.length:
                row = self._matrix[r]
                del row[self.length-1]
                row.insert(0, 0)
                self._matrix[r] = row
                r += 1
            return True
        else:
            return False

    def move_left(self):
        '''
        a function the moves the piece left if possible
        Parameters:
            None
        Returns:
            True if moved
            False otherwise
        '''
        if self.check_column_empty(0):
            r = self.length - 1
            while r >= 0:
                row = self._matrix[r]
                del row[0]
                row.insert(self.length-1, 0)
                r -= 1
            return True
        else:
            return False

    def move_up(self):
        empty = []
        for c in self._matrix[self.length-1]:
            empty.append(0)
        del self._matrix[0]
        self._matrix.insert(self.length,empty)
        
    def move_down(self):
        moved = True
        if self.check_row_empty(self.length-1):
            copy = []
            for c in self._matrix[self.length-1]:
                copy.append(c)
            del self._matrix[self.length-1]
            self._matrix.insert(0,copy)
        else:
            moved = False
        return moved
            
    def set_cell(self,row,column,value):
        if(row >= len(self._matrix)):
            raise PieceError("Piece: row outside of range")
        if(column >=  len(self._matrix[0])):
            raise PieceError("Piece: column outside of range")
        self._matrix[row][column] = value

    def check_column_empty(self,column):
        '''
            a function that checks if the column is empty
            Parameters:
               column: the column to check
            Returns 
                True if empty
                False otherwise
        '''
        r = 0
        empty = True
        while empty and r < self.length:
            if self._matrix[r][column] != 0:
                empty = False
            r += 1 
        return empty

    def check_row_empty(self,row):
        '''
            a function that checks if the row is empty
            Parameters:
               row: the row to check
            Returns 
                True if empty
                False otherwise
        '''
        c = 0
        empty = True
        while empty  and c < self.length:
            if self._matrix[row][c] != 0:
                empty = False
            c += 1
        return empty

    def rotate(self):
        '''
        a function that rotates the piece
        Parameters:
            None
        Returns:
            The piece before rotation
        '''
        matrix = []
        for col in range(self.length-1,-1,-1):
            m = []
            for row in range(self.length-1,-1,-1):
                m.append(self._matrix[row][col])
            matrix.insert(0,m)
        temp = self._matrix
        self._matrix = matrix
        return temp

    def print_m(self):
        '''
        a function to print the piece
        Parameters:
            None
        Returns:
            None
        '''
        print("----")
        for r in self._matrix:
            output = ""
            for cell in r:
                output +=  str(cell) + " "
            print(output)
        print("----")

    def negative_piece(self):
        '''
        a function that creates the negative of itself
        Parameters:
            None
        Returns:
            p: of class piece
        '''
        p = Piece()
        p.length = self.length
        p.row = self.row
        p.column = self.column
        matrix = []
        for r in self._matrix:
            m = [] 
            for c in r :
                if c != 0:
                    m.append(-1 * c)
                else:
                    m.append(c)
            matrix.append(m)
        p._matrix = matrix
        return p

    def create_piece(self):
        '''
        a function that creates a random piece
        Pieces are:
            1.i
            2.j
            3.l
            4.O
            5.s
            6.t
            7.z
        Parameters:
            None
        Returns
            None
        '''
        piece = randint(1,7)
        self.initialize(3, 3)
        if piece == 1:
            self.initialize(4, 4)
            self._straight_piece()
        elif piece == 2:
            self._L_left_piece()
        elif piece == 3:
            self._L_right_piece()
        elif piece == 4:
            self._e_piece()
        elif piece == 5:
            self._z_left_piece()
        elif piece == 6:
            self._z_right_piece()
        elif piece == 7:
            self.initialize(2, 2)
            self._square_piece()
            
    def _straight_piece(self):
        '''
        a function to create the i piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(1,0,1)
        self.set_cell(2,0,1)
        self.set_cell(3,0,1)
    
    def _L_left_piece(self):
        '''
        a function to create the j piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(1,0,1)
        self.set_cell(0,1,1)
        self.set_cell(0,2,1)
    
    def _L_right_piece(self):
        '''
        a function to create the l piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(1,2,1)
        self.set_cell(0,1,1)
        self.set_cell(0,2,1)
    
    def _e_piece(self):
        '''
        a function to create the t piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(1,1,1)
        self.set_cell(0,1,1)
        self.set_cell(0,2,1)
    
    def _z_right_piece(self):
        '''
        a function to create the z piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(1,1,1)
        self.set_cell(0,1,1)
        self.set_cell(1,2,1)   
    
    def _z_left_piece(self):
        '''
        a function to create the s piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,2,1)
        self.set_cell(1,1,1)
        self.set_cell(0,1,1)
        self.set_cell(1,0,1)        
    
    def _square_piece(self):
        '''
        a function to create the o piece
        Parameters:
            None
        Returns None
        '''
        self.set_cell(0,0,1)
        self.set_cell(0,1,1)
        self.set_cell(1,0,1)
        self.set_cell(1,1,1) 
    
    def get_position(self,row,column):
        '''
        getter function that gets the value at position (row,column) of the piece
        Parameters:
            row: the row index of the piece
            column: the column index of the piece
        Returns
             the value at index (row,column)
        '''
        if(row >= len(self._matrix)):
            raise PieceError("Piece: row outside of range")
        if(column >=  len(self._matrix[0])):
            raise PieceError("Piece: column outside of range")
        return self._matrix[row][column]
      
class Test(unittest.TestCase):

    def setUp(self):
        self.p = Piece(4,4)

    def tearDown(self):
        pass

    def test_get_start(self):
        r,c = self.p.get_start()
        self.assertEqual(r, 0)
        self.assertEqual(c, 0)

    def test_get_length(self):
        l = self.p.get_length()
        self.assertEqual(l,4)

    def test_move_right(self):
        self.p.set_cell(0, 0, 1)
        moved = self.p.move_right()
        self.assertEqual(moved,True)
        matrix = [[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(matrix, self.p._matrix)
        self.p.initialize(4, 4)
        self.p.set_cell(3, 3, 1)
        moved = self.p.move_right()
        self.assertEqual(moved, False)
    
    def test_move_left(self):
        self.p.set_cell(0, 0, 1)
        moved = self.p.move_left()
        self.assertEqual(moved,False)
        self.p.initialize(4, 4)
        self.p.set_cell(0, 3, 1)
        self.p.set_cell(1, 3, 1)
        self.p.set_cell(1, 2, 1)
        self.p.set_cell(2, 3, 1)
        moved = self.p.move_left()
        self.assertEqual(moved, True)
        matrix = [[0,0,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0]]
        self.assertEqual(matrix, self.p._matrix)

    def test_check_column_empty(self):
        self.p.set_cell(0, 0, 1)
        self.assertEqual(self.p.check_column_empty(0),False)
        self.assertEqual(self.p.check_column_empty(1),True)
            
    def test_rotate(self):
        self.p.initialize(3, 3)
        self.p.set_cell(0, 0, 1)
        self.p.set_cell(0, 1, 2)
        self.p.set_cell(0, 2, 3)
        self.p.set_cell(1, 0, 4)
        self.p.set_cell(1, 1, 5)
        self.p.set_cell(1, 2, 6)
        self.p.set_cell(2, 0, 7)
        self.p.set_cell(2, 1, 8)
        self.p.set_cell(2, 2, 9)
        self.p.rotate()
        matrix = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(matrix, self.p._matrix)
        self.p.rotate()
        self.p.rotate()
        self.p.rotate()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(matrix, self.p._matrix)
    
    def test_rotate_l_piece(self):
        self.p.initialize(3, 3)
        self.p._L_left_piece()
        expected = [[1,1,1],[1,0,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #one rotation
        expected = [[0,1,1],[0,0,1],[0,0,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #two rotations
        expected = [[0,0,0],[0,0,1],[1,1,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        # three rotations
        expected = [[1,0,0],[1,0,0],[1,1,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #back to beginning
        expected = [[1,1,1],[1,0,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        
        self.p.initialize(3, 3)
        self.p._L_right_piece()
        expected = [[1,1,1],[0,0,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #one rotation
        expected = [[0,0,1],[0,0,1],[0,1,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #two rotations
        expected = [[0,0,0],[1,0,0],[1,1,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        # three rotations
        expected = [[1,1,0],[1,0,0],[1,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #back to beginning
        expected = [[1,1,1],[0,0,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)

    def test_rotate_straight_piece(self):
        self.p._straight_piece()
        expected = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        #one rotate
        self.p.rotate()
        expected = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        #two rotates
        self.p.rotate()
        expected = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
        self.assertEqual(self.p._matrix,expected)
        #three rotates
        self.p.rotate()
        expected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
        self.assertEqual(self.p._matrix,expected)
        #back to beginning
        self.p.rotate()
        expected = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
        self.assertEqual(self.p._matrix,expected)

    def test_rotate_e_piece(self):
        self.p.initialize(3, 3)
        self.p._e_piece()
        expected = [[1,1,1],[0,1,0],[0,0,0],]
        self.assertEqual(self.p._matrix,expected)
        #one rotate
        self.p.rotate()
        expected = [[0,0,1],[0,1,1],[0,0,1],]
        self.assertEqual(self.p._matrix,expected)        
        #two rotate
        self.p.rotate()
        expected = [[0,0,0],[0,1,0],[1,1,1],]
        self.assertEqual(self.p._matrix,expected)        
        #three rotate
        self.p.rotate()
        expected = [[1,0,0],[1,1,0],[1,0,0],]
        self.assertEqual(self.p._matrix,expected)       
        #back to beginning
        self.p.rotate()
        expected = [[1,1,1],[0,1,0],[0,0,0],]
        self.assertEqual(self.p._matrix,expected)

    def test_rotate_z_piece(self):
        self.p.initialize(3, 3)
        self.p._z_left_piece()
        expected = [[0,1,1],[1,1,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #one rotation
        expected = [[0,1,0],[0,1,1],[0,0,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #two rotations
        expected = [[0,0,0],[0,1,1],[1,1,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        
        # three rotations
        expected = [[1,0,0],[1,1,0],[0,1,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #back to beginning
        expected = [[0,1,1],[1,1,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        
        self.p.initialize(3, 3)
        self.p._z_right_piece()
        expected = [[1,1,0],[0,1,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #one rotation
        expected = [[0,0,1],[0,1,1],[0,1,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #two rotations
        expected = [[0,0,0],[1,1,0],[0,1,1]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        # three rotations
        expected = [[0,1,0],[1,1,0],[1,0,0]]
        self.assertEqual(self.p._matrix,expected)
        self.p.rotate()
        #back to beginning
        expected = [[1,1,0],[0,1,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
    
    def test_negative_piece(self):
        self.p.initialize(2, 2)
        self.p.set_cell(1, 1, 4)
        n = self.p.negative_piece()
        self.assertEqual(n._matrix, [[0,0],[0,-4]])
    
    def test_straight_piece(self):
        self.p._straight_piece()
        expected = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
        self.assertEqual(self.p._matrix,expected)

    def test_L_left_piece(self):
        self.p.initialize(3, 3)
        self.p._L_left_piece()
        expected = [[1,1,1],[1,0,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
    
    def test_L_right_piece(self):
        self.p.initialize(3, 3)
        self.p._L_right_piece()
        expected = [[1,1,1],[0,0,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
    
    def test_e_piece(self):
        self.p.initialize(3, 3)
        self.p._e_piece()
        expected = [[1,1,1],[0,1,0],[0,0,0],]
        self.assertEqual(self.p._matrix,expected)
    
    def test_z_right_piece(self):
        self.p.initialize(3, 3)
        self.p._z_right_piece()
        expected = [[1,1,0],[0,1,1],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)
    
    def test_z_left_piece(self):
        self.p.initialize(3, 3)
        self.p._z_left_piece()
        expected = [[0,1,1],[1,1,0],[0,0,0]]
        self.assertEqual(self.p._matrix,expected)

    def test_square_piece(self):
        self.p.initialize(2, 2)
        self.p._square_piece()
        expected = [[1,1],[1,1]]
        self.assertEqual(self.p._matrix,expected)          
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()