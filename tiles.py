# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 02:30:20 2017

@author: AB Sanyal
"""

#imports

class tile():

    def __init__( self, x, y, tileType = "ground", desc = "" ):

        self.tag = "(" + str( x ) + "," + str( y ) + ")" + str( tileType )
        self.tileType = tileType
        self.x = x
        self.y = y
        self.description = desc