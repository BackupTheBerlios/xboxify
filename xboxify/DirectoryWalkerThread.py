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
