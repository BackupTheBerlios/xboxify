import os.path
opj = os.path.join

# Version of the application
version 	= '1.2'
# Name of the application
name    	= 'XboxIfy'
# Short name of the application
short_name  = 'xboxify'
# Description of the program
description	= 'Rename files in such a way, that they can be transferred to Xbox'
# Additional data files - used by py2exe
data_files  = [('Images', [opj('Images', '*.gif'), opj('Images', '*.ico')]),
                ('.', ['*.txt', '*.lnk'])]

# Author of the program
author		= 'Alexander Skwar'
# Author's email
author_email= 'XboxIfy@message-center.info'

# Scripts of the program - used by py2exe
scripts		= ['XboxIfy.py']

# Files which should be in the source distribution
files = ['*.py', '*.lnk', '*.pyw', '*.txt',
        opj('DirectoryWalker', '*.py'),
        opj('Frames', '*.py'),
        opj('Images', '*.gif'), opj('Images', '*.ico'),
        opj('Utils', '*.cfg'), opj('Utils', '*.py'), opj('Utils', 'Tools-i18n', '*.py')]

# Should the source distribution files be uploaded?
# If this is not None, then they'll be uploaded
# upload = None
upload = {
    'host': 'ftp.berlios.de',
    'user': None,               # ie. anonymous
    'pass': None,               # ie. default password
    'acct': None,               # ie. anonymous
    'dir': '/incoming',
    'pasv': True
}
# Uncomment the following line, to DISABLE FTP upload
# upload = None

