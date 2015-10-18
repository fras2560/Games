'''
Created on Oct 18, 2015

@author: Dallas
'''
from minesweeper.square import Square
import networkx as nx
import logging
from minesweeper.settings import SQUARE
import random
class Map():
    def __init__(self, width, height, logger=None, bombs=10):
        if logger is None:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s %(message)s')
            logger = logging.getLogger(__name__)
        self.logger = logging
        self._graph = nx.Graph()
        self.height = height
        self.width = width
        row = 0
        while row < self.height:
            column = 0
            while column < self.width:
                self.add_square(Square(x=column*SQUARE, y=row*SQUARE),row, column)
                column += 1
            row +=1 
        self.set_bombs(bombs)
        self.set_numbers()

    def add_square(self, square, row, column):
        if row > self.height or column > self.width:
            raise Exception("Invalid Square")
        node_id = column + row * self.width
        self._graph.add_node(node_id, node=square)
        if row > 0:
            self._graph.add_edge(node_id, column + (row-1)*self.width)
        if column > 0:
            self._graph.add_edge(node_id, (column - 1) + (row)*self.width)
        if row > 0 and column > 0:
            self._graph.add_edge(node_id, (column - 1) + (row - 1)*self.width)

    def set_bombs(self, bombs):
        set = 0
        upper = self.height* self.width - 1
        nodes = nx.get_node_attributes(self._graph, 'node')
        while set < bombs:
            set += 1
            r = random.randint(0, upper)
            nodes[r].bomb()

    def set_numbers(self):
        nodes = nx.get_node_attributes(self._graph, 'node')
        upper = self.height*self.width - 1
        for x in range(0, upper):
            count = 0
            for neighbor in self._graph.neighbors(x):
                if nodes[neighbor].is_bombed():
                    count += 1
            nodes[x].number(count)

    def output(self):
        nodes = nx.get_node_attributes(self._graph, 'node')
        index = 0
        line_end = self.width
        end = self.width * self.height
        while line_end <= end:
            line = []
            while index < line_end:
                if nodes[index].is_bombed():
                    line.append("X")
                else:
                    line.append(str(nodes[index].get_number()))
                index += 1
            print(", ".join(line))
            #self.logger.info(", ".join(line))
            line_end += self.width

    def left_click(self, x, y):
        fucked_up = False
        nodes = nx.get_node_attributes(self._graph, 'node')
        node_id = (x // SQUARE) + self.width * (y // SQUARE)
        if nodes[node_id].is_covered():
            nodes[node_id].uncover()
        else:
            # uncover all the neighbors
            for neighbor in self._graph.neighbors(node_id):
                if nodes[neighbor].is_bombed() and not nodes[neighbor].is_flagged:
                    fucked_up = True
                elif not nodes[neighbor].is_bombed():
                    nodes[neighbor].uncover()
        return fucked_up

    def right_click(self, x, y):
        nodes = nx.get_node_attributes(self._graph, 'node')
        node_id = (x // SQUARE) + self.width * (y // SQUARE)
        if nodes[node_id].is_flagged():
            nodes[node_id].flag()
            nodes[node_id].question()
        elif nodes[node_id].is_questioned():
            nodes[node_id].question()
        else:
            nodes[node_id].flag()
        return nodes[node_id].is_bombed()

    def draw(self, surface):
        nodes = nx.get_node_attributes(self._graph, 'node')
        for i in range(0, len(nodes)):
            nodes[i].draw(surface)

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.map = Map(10, 10)

    def testOutput(self):
        self.map.output()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()