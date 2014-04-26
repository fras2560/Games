'''
@author: Dallas Fraser
@contact: fras2560@mylaurier.ca
@version: 1.0
@date: 03/02/2014
@note: This class is used for tetris game
'''
import unittest
from games.piece import Piece

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

class MatrixError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Matrix():
    def __init__(self, row=None, column=None):
        
        self._matrix = []
        if row is not None and row > 0:
            if column is not None and column > 0:
                self.initialize(row, column)
                self.row = row
                self.column = column

    def initialize(self, row, column):
        '''
        a function that can will initialize the
        matrix to be row*column of zeros
        Parameters:
            row: the row dimension
            column: the column dimension
        Return
            None
        '''
        if row > 0 and column > 0:
            self._matrix = []
            self.column = column
            self.row = row
            r = 0
            while r < row:
                c = 0
                rw = []
                while c < column:
                    rw.append(0)
                    c += 1
                self._matrix.append(rw)
                r+=1
        else:
            raise Exception("Matrix not inialized properly")

    def print_m(self):
        '''
        a function to print the matrix
        Parameters:
            None
        Returns:
            None
        '''
        for r in self._matrix:
            output = ""
            for cell in r:
                output +=  str(cell) + " "
            print(output)
        print("-----------")

    def set_cell(self,row,column,value):
        '''
        a setter function to set an element of the matrix at position (row,column)
        Parameters:
            row: the row index of the matrix
            column: the column index of the matrix
            value: the value of matrix position
        Returns:
            None
        Raises MatrixError
            If access is outside matrix range
        '''
        if(row >= len(self._matrix)):
            raise MatrixError("Matrix row was accessed outside of range")
        if(column >=  len(self._matrix[0])):
            raise MatrixError("Matrix column was accessed outside of range")
        self._matrix[row][column] = value

    def get_cell(self, row, column):
        '''
        a getter function to get an element of the matrix at position (row,column)
        Parameters:
            row: the row index of the matrix
            column: the column index of the matrix
        Returns:
            None
        Raises MatrixError
            If access is outside matrix range
        '''
        if(row >= len(self._matrix)):
            raise MatrixError("Matrix row was accessed outside of range")
        if(column >=  len(self._matrix[0])):
            raise MatrixError("Matrix column was accessed outside of range")
        return self._matrix[row][column]

    def create_empty_row(self):
        '''
        a function that creates an empty row of zeros
        Parameters:
            None
        Returns:
            row: a list of zero (size n)
        '''
        row = []
        r = 0
        while r < self.row:
            row.append(0)
            r+=1
        return row

    def check_lines(self):
        '''
        a function that check and delete any completed rows
        Parameters:
            None
        Returns:
            lines: a list of the rows completed
        '''
        lines = []
        row = 0
        while row < self.row:
            complete = True
            col = 0
            while complete and col < self.column:
                if self._matrix[row][col] == 0:
                    complete = False
                else:
                    col +=1 
            if complete:
                del self._matrix[row]
                self._matrix.insert(0, self.create_empty_row())
                lines.append(row)
            row += 1
        return lines

    def add_piece(self,piece):
        '''
            a function that adds the piece to the matrix
            Parameters:
                piece: a object of class piece
            Returns:
                None
        '''
        r,c = piece.get_start()
        length = piece.get_length()
        pos = r
        while pos < r + length:
            pos2 = c
            while pos2 < c + length:
                self._matrix[pos][pos2] += piece.get_position(pos-r, pos2-c)
                pos2 += 1
            pos += 1

    def delete_piece(self,piece):
        '''
        a function that deletes the piece from the matrix
        Parameters:
            piece: of class piece
        Returns:
            None
        '''
        neg = piece.negative_piece()
        self.add_piece(neg)

    def check_overlap(self):
        '''
            a function that checks if there is overlap in the matrix
            Parameters:
                None
            Returns:
                True if overlap
                False otherwise
        '''
        overlap = False
        r = 0
        while not overlap and r < self.row:
            c = 0
            while c < self.column:
                if self._matrix[r][c] > 1:
                    overlap = True
                    break;
                c += 1
            r += 1
        return overlap

    def move_right(self, piece):
        '''
        a function the moves the piece to the right
        Parameters:
            piece: of class piece
        Returns:
            True of piece was moved
            False otherwise
        '''
        self.add_piece(piece.negative_piece())
        moved = True
        if not piece.move_right():
            if not ((piece.column + piece.length) >= self.column):
                piece.column += 1
            else:                
                moved = False
                self.add_piece(piece)
            if moved:
                self.add_piece(piece)
                if self.check_overlap():
                    self.add_piece(piece.negative_piece())
                    piece.column -= 1
                    self.add_piece(piece)
                    moved = False   
        else:
            self.add_piece(piece)
            if self.check_overlap():
                moved = False
                self.add_piece(piece.negative_piece())
                piece.move_left()
                self.add_piece(piece)
        return moved

    def move_left(self, piece):
        '''
        a function the moves the piece to the left
        Parameters:
            piece: of class piece
        Returns:
            True of piece was moved
            False otherwise
        '''
        self.add_piece(piece.negative_piece())
        moved = True
        if not piece.move_left():
            if piece.column > 0:
                piece.column -= 1
            else:
                moved = False
                self.add_piece(piece)
            if moved:
                self.add_piece(piece)
                if self.check_overlap():
                    self.add_piece(piece.negative_piece())
                    piece.column += 1
                    self.add_piece(piece)
                    moved = False
        else:
            self.add_piece(piece)
            if self.check_overlap():
                moved = False
                self.add_piece(piece.negative_piece())
                piece.move_right()
                self.add_piece(piece)
        return moved

    def move_down(self,piece):
        '''
        a function that moves the piece down
        Parameters:
            piece: the piece to move down
        Returns:
            True if piece was moved
            False otherwise
        '''
        self.add_piece(piece.negative_piece())
        moved = True
        if piece.row+len(piece) >= self.row:
            moved = piece.move_down()
            if moved:
                self.add_piece(piece)
                if self.check_overlap():
                    self.add_piece(piece.negative_piece())
                    piece.move_up()
                    self.add_piece(piece)
                    moved = False
            else:
                self.add_piece(piece)
        else:
            piece.row += 1
            self.add_piece(piece)
            if self.check_overlap():
                self.add_piece(piece.negative_piece())
                piece.row -= 1
                moved = False
                self.add_piece(piece)
        return moved

    def rotate_piece(self,piece):
        '''
        a function that rotates the piece if possible
        Parameters:
            piece: the piece to rotate
        Returns:
            True if piece was rotated
            False otherwise
        '''
        self.add_piece(piece.negative_piece())
        piece.rotate()
        self.add_piece(piece)
        rotated = True
        if self.check_overlap():
            self.add_piece(piece.negative_piece())
            piece.rotate()
            piece.rotate()
            piece.rotate()
            rotated = False
            self.add_piece(piece)
        return rotated

class test_case(unittest.TestCase):

    def setUp(self):
        self.m = Matrix(3,3)
        self.p = Piece(3,3)
        self.p._e_piece()

    def tearDown(self):
        pass

    def test_print_m(self):
        '''
        If it runs then it passes
        '''
        print("Print Test")
        print("----------")
        self.m.print_m()
        print("----------")

    def test_set_cell(self):
        self.m.set_cell(1, 1, 1)
        self.assertEqual(self.m._matrix[1][1],1)

    def test_create_empty_row(self):
        result = self.m.create_empty_row()
        self.assertEqual(result, [0,0,0])

    def test_check_lines(self):
        self.m.set_cell(0, 1, 1)
        self.m.set_cell(1, 0, 1)
        self.m.set_cell(1, 1, 1)
        self.m.set_cell(1, 2, 1)
        self.m.set_cell(2, 2, 1)
        matrix = [[0,0,0],[0,1,0],[0,0,1]]
        result = self.m.check_lines()
        self.assertEqual(result,[1])
        self.assertEqual(self.m._matrix, matrix)

    def test_add_piece(self):
        self.m = Matrix(3,3)
        self.m.add_piece(self.p)
        expected = [[1,1,1],[0,1,0],[0,0,0]]
        self.assertEqual(expected, self.m._matrix)

    def test_delete_piece(self):
        self.m = Matrix(3,3)
        self.m.add_piece(self.p)
        self.m.delete_piece(self.p)
        expected = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(expected, self.m._matrix)
        self.m.set_cell(2, 2, 1)
        self.m.add_piece(self.p)
        self.m.delete_piece(self.p)
        expected = [[0,0,0],[0,0,0],[0,0,1]]
        self.assertEqual(expected, self.m._matrix)
    
    def test_check_overlap(self):
        self.m.set_cell(1, 1, 1)
        overlap = self.m.check_overlap()
        self.assertEqual(overlap, False)
        self.m.set_cell(2, 2, 4)
        overlap = self.m.check_overlap()
        self.assertEqual(overlap, True)
        self.m.initialize(3, 3)
        self.m.set_cell(0, 0, 1)
        self.p._z_right_piece()
        self.m.add_piece(self.p)
        overlap = self.m.check_overlap()
        self.assertEqual(overlap, True)
        self.m.add_piece(self.p.negative_piece())
        overlap = self.m.check_overlap()
        self.assertEqual(overlap, False)

    def test_move_right(self):
        #test round one keep piece in bounds
        self.p.initialize(2, 2)
        self.p._square_piece()
        self.m.set_cell(2, 2, 1)
        self.m.add_piece(self.p)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, True )
        expected = [[0,1,1],[0,1,1],[0,0,1]]
        self.assertEqual(self.m._matrix,expected)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, False )
        expected = [[0,1,1],[0,1,1],[0,0,1]]
        self.assertEqual(self.m._matrix,expected)
        #test round two test piece in bounds by rotating
        self.m.initialize(3, 3)
        self.p.initialize(3, 3)
        self.p._e_piece()
        self.m.add_piece(self.p)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, False)
        expected = [[1,1,1],[0,1,0],[0,0,0]]
        self.assertEqual(self.m._matrix,expected)
        self.m.add_piece(self.p.negative_piece())
        self.p.rotate()
        self.p.rotate()
        self.p.rotate()
        self.m.add_piece(self.p)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, True)
        expected = [[0,1,0],[0,1,1],[0,1,0]]
        self.assertEqual(self.m._matrix,expected)
        #test round three check piece is blocked by a block
        self.m.initialize(4, 4)
        self.p.initialize(3, 3)
        self.p._e_piece()
        self.m.add_piece(self.p)
        self.m.set_cell(0, 3, 1)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, False)
        expected = [[1,1,1,1],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(self.m._matrix,expected)
        self.m.add_piece(self.p.negative_piece())
        self.p.rotate()
        self.p.rotate()
        self.m.add_piece(self.p)
        moved = self.m.move_right(self.p)
        self.assertEqual(moved, True)
        expected = [[0,0,0,1],[0,0,1,0],[0,1,1,1],[0,0,0,0]]
        self.assertEqual(self.m._matrix,expected)

    def test_move_left(self):
        #this test references move_right
        #test round one keep piece in bounds
        self.p.initialize(2, 2)
        self.p._square_piece()
        self.m.set_cell(2, 2, 1)
        self.m.add_piece(self.p)
        self.m.move_right(self.p)
        moved = self.m.move_left(self.p)
        self.assertEqual(moved, True )
        expected = [[1,1,0],[1,1,0],[0,0,1]]
        self.assertEqual(self.m._matrix,expected)
        moved = self.m.move_left(self.p)
        self.assertEqual(moved, False )
        expected = [[1,1,0],[1,1,0],[0,0,1]]
        self.assertEqual(self.m._matrix,expected)
        #test round two test piece in bounds by rotating
        self.m.initialize(3, 3)
        self.p.initialize(3, 3)
        self.p._e_piece()
        
        self.p.rotate()
        self.p.rotate()
        self.p.rotate()
        self.m.add_piece(self.p)
        moved = self.m.move_right(self.p)
        moved = self.m.move_left(self.p)
        self.assertEqual(moved, True)
        expected = [[1,0,0],[1,1,0],[1,0,0]]
        self.assertEqual(expected,self.m._matrix)

    def test_move_down(self):
        self.p.initialize(3, 3)
        self.p._L_right_piece()
        self.m.initialize(4, 4)
        self.m.add_piece(self.p)
        moved = self.m.move_down(self.p)
        self.assertEqual(moved, True)
        expected = [[0,0,0,0],[1,1,1,0],[0,0,1,0],[0,0,0,0]]
        self.assertEqual(expected,self.m._matrix)
        moved = self.m.move_down(self.p)
        self.assertEqual(moved, True)
        expected = [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,0,1,0]]
        self.assertEqual(expected,self.m._matrix)
        moved = self.m.move_down(self.p)
        self.assertEqual(moved, False)
        expected = [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,0,1,0]]

    def test_rotate_piece(self):
        self.p.initialize(3, 3)
        self.p._L_right_piece()
        self.m.initialize(3, 3)
        self.m.add_piece(self.p)
        rotated = self.m.rotate_piece(self.p)
        self.assertEqual(rotated, True)
        expected = [[0,0,1],[0,0,1],[0,1,1]]
        self.assertEqual(expected, self.m._matrix)
        self.m.set_cell(2, 0, 1)
        rotated = self.m.rotate_piece(self.p)
        self.assertEqual(rotated, False)
        expected = [[0,0,1],[0,0,1],[1,1,1]]
        self.assertEqual(expected, self.m._matrix)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()      
