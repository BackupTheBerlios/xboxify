#!/usr/bin/env python
#Boa:App:BoaApp

#-----------------------------------------------------------------------------
# Name:        XboxIfy.py                                                     
# Purpose:     Application script of XboxIfy                                  
#                                                                             
# Author:      Alexander Skwar <XboxIfy@message-center.info>                  
#                                                                             
# Created:     2003/17/03                                                     
# RCS-ID:      $Id: XboxIfy.py,v 1.3 2003/03/17 15:18:03 askwar Exp $
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

from wxPython.wx import *
from Frames import *

modules ={'DirectoryWalker': [0,
                     'Directory Walker class',
                     'DirectoryWalker/DirectoryWalker.py'],
 'DirectoryWalkerThread': [0,
                           'Threaded Directory Walker',
                           'DirectoryWalker/DirectoryWalkerThread.py'],
 'MakeDist': [0,
              'Create Windows executable and SFX for distribution',
              'Utils/MakeDist.py'],
 'Readme': [0, 'Description of application', 'Readme.txt'],
 '__init__': [0,
              'Initialization code for package "Frames"',
              'Frames/__init__.py'],
 '__init__DW': [0,
                'Initialization code for package "DirectoryWalker"',
                'DirectoryWalker/__init__.py'],
 '__version__': [0, 'Version Information', 'Utils/__version__.py'],
 'fMain': [1, 'Main frame of Application', 'Frames/fMain.py'],
 'setup': [0, 'Setup', 'Utils/setup.py']}

class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = fMain.create(None)
        # needed when running from Boa under Windows 9X
        self.main.Show();self.main.Hide();self.main.Show()
        self.SetTopWindow(self.main)
        return true

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
