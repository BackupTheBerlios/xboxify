#!/usr/bin/python
"""Setup wrapper for creating Windows executable."""

#-----------------------------------------------------------------------------
# Name:        setup.py                                                       
# Purpose:     Setup wrapper for creating Windows executable                  
#                                                                             
# Author:      Alexander Skwar <ASkwar@email-server.info>                     
#                                                                             
# Created:     2003/12/03                                                     
# RCS-ID:      $Id: setup.py,v 1.1 2003/03/12 20:14:12 askwar Exp $                                                
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

# ------------------> Nothing user-configurable below here! <------------------ 
#-------------------------------------------------------------------------------

from distutils.core import setup
import py2exe
import glob
import MakeDist
import os

def main():
    
    # Now let py2exe build the executable
    setup(
    	name='XboxIfy', 
    	version=MakeDist.version, 
    	scripts=['XboxIfy.py'], 
    	description='Rename files in such a way, that they can be transferred to Xbox', 
    	author='Alexander Skwar', 
    	author_email='ASkwar@email-server.info', 
    	data_files=[('.',((glob.glob('*.gif') + glob.glob('*.ico')) + glob.glob('*.txt')))]
    )
    
if __name__ == '__main__':
    if not os.name in ('nt', 'dos'):
        print "Error: setup.py can only be run in Windows or DOS!\n"
        sys.exit(1)

    main()
