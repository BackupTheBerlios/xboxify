import os, stat

class DirectoryWalker:
    """Class for walking a directory tree."""
    
    def __init__(self, path = None):
        """Constructor of class.  If path parameter is given, it directly
        walks the directory tree."""
        
        # Initialize the lists containing the items
        self.__dirs     = []
        self.__chars    = []
        self.__blocks   = []
        self.__files    = []
        self.__fifos    = []
        self.__links    = []
        self.__socks    = []
        
        # Currently processed "object"
        self.__current = ''
        
        # If the user specified a path, walk the tree
        if not path is None:
            self.walkTree(path)
            
    def clearLists(self):
        """Clear all the "file"lists."""

        self.__dirs     = []
        self.__chars    = []
        self.__blocks   = []
        self.__files    = []
        self.__fifos    = []
        self.__links    = []
        self.__socks    = []
        
    def walkTree(self, path):
        """Walk the directory given in 'path'."""
        
        for f in os.listdir(path):
            pathname = os.path.join(path, f)
            self.__current = pathname
            mode = os.stat(pathname)[stat.ST_MODE]
            if stat.S_ISREG(mode):
                self.__files.append(pathname)
            elif stat.S_ISDIR(mode):
                self.__dirs.append(pathname)
                self.walkTree(pathname)
            elif stat.S_ISCHR(mode):
                self.__chars.append(pathname)
            elif stat.S_ISBLK(mode):
                self.__blocks.append(pathname)
            elif stat.S_ISFIFO(mode):
                self.__fifos.append(pathname)
            elif stat.S_ISLNK(mode):
                self.__links.append(pathname)
            elif stat.S_ISSOCK(mode):
                self.__socks.append(pathname)
                
    def getDirs(self):
        """Get a list of all the directories found."""
        return self.__dirs
    
    def getChars(self):
        """Get a list of all the character special device files found."""
        return self.__chars
    
    def getBlocks(self):
        """Get a list of all the block special device files found."""
        return self.__blocks
    
    def getFiles(self):
        """Get a list of all the regular files found."""
        return self.__files
    
    def getFifos(self):
        """Get a list of all the FIFO (named pipe) files found."""
        return self.__fifos
    
    def getLinks(self):
        """Get a list of all the symbolic links found."""
        return self.__links
    
    def getSocks(self):
        """Get a list of all the sockets found."""
        return self.__socks

    def getCurrent(self):
        """Get the currently processed object."""
        return self.__current
    
