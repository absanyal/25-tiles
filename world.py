# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 04:07:41 2017

@author: AB Sanyal
"""

#imports
from tiles import tile

#World constants
width = 5
height = 5

#Create the world
world = []

for y in range( height ):
    world.append( [] )
for row in world:
    for x in range( width ):
        row.append( tile( x, y ) )