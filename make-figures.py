#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob

gallery = open("README.txt").read()
gallery += "\n----\n\n"

figure_rst = """
.. figure:: %s/%s.png
   :target: %s/%s-large.png

   Source `%s.py <%s/%s.py>`_

"""

directories = ['simple', 'spine', 'style', 'image',
               'one-line', 'grid', 'voronoi', 'showcase']
for d in directories:
    print "Making all in", d
    for f in glob.glob(d+"/*.py"):
        name = os.path.basename(f)
        name = name.split('.')[0]
        gallery +=  figure_rst % (d,name,d,name,name,d,name)
    print
f = open('index.rst','w')
f.write(gallery)
f.close()

