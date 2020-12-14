# encoding: utf-8

import gvsig
from gvsig.libs import gvpy

def main(*args):
    layer = gvsig.currentLayer()
    y=gvpy.runalg("EstraDH", layer, "4", "TABLE", "VARIABLE",ADDLAYER=True,NAME="Capa")
