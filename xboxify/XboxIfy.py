#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *

import fMain

modules ={'DirectoryWalker': [0, 'Directory Walker class', 'DirectoryWalker.py'],
 'DirectoryWalkerThread': [0,
                           'Threaded Directory Walker',
                           'DirectoryWalkerThread.py'],
 'MakeDist': [0,
              'Create Windows executable and SFX for distribution',
              'MakeDist.py'],
 'Readme': [0, 'Description of application', 'Readme.txt'],
 'fMain': [1, 'Main frame of Application', 'fMain.py'],
 'setup': [0, 'Setup', 'setup.py']}

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
