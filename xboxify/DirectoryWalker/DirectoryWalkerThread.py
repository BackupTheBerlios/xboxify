#-----------------------------------------------------------------------------
# Name:        DirectoryWalkerThread.py                                       
# Purpose:     Wrapper class for Directory Walker to run it in a thread       
#                                                                             
# Author:      Alexander Skwar <XboxIfy@message-center.info>                  
#                                                                             
# Created:     2003/17/03                                                     
# RCS-ID:      $Id: DirectoryWalkerThread.py,v 1.1 2003/03/17 15:18:03 askwar Exp $
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

import DirectoryWalker
import threading

class DirectoryWalkerThread(threading.Thread):
    """Calls the DirectoryWalker in a thread.  The DirectoryWalker can be accessed
    through the getDirWalker method."""
    
    def __init__(self, folder):
        """Constructor.  Expects one parameter "folder" which is the name of
        the directory to be walked along."""
        
        # Create the thread
        threading.Thread.__init__(self, target = self.Execute, kwargs = {'folder': folder})
        
        # Initialize the DirectoryWalker property
        self.__dirWalker = DirectoryWalker.DirectoryWalker()
        
    def getDirWalker(self):
        return self.__dirWalker
    
    def Execute(self, folder):
        self.__dirWalker.walkTree(folder)
