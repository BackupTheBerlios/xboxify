RCS-ID:      $Id: Readme.txt,v 1.2 2003/03/30 15:07:36 askwar Exp $

XboxIfy allows to easily change (local) filenames in such a way,
that they can be easily transferred to Xbox.

--------------------------------------------------------------------------------

Installation:

- Windows: 

  If you downloaded the .EXE file, you can start XboxIfy by simply
  doubleclicking on XboxIfy.exe.  No further installation is required.
  The program doesn't copy any .dll-files to the Windows system directory -
  if you want to remove the program, simply delete the directory containing
  the XboxIfy.exe and that's it!  XboxIfy stores the configuration in the
  registry under HKEY_CURRENT_USER\Software\XboxIfy.  If you delete this
  key as well, every traces of the program have been removed.

- All operating systems (source release):

  Obviously, you managed to unpack the source archive (.zip, .tar.gz or
  .tar.bz2) already ;)
  XboxIfy is written in Python with the wxPython GUI toolkit.  If you want
  to run XboxIfy, you'll need to have Python and the GUI toolkit installed.
  You can download it from:

  Python -> http://python.org -> http://python.org/2.2.2/
  wxPython -> http://wxPython.org/ -> 
  http://sf.net/project/showfiles.php?group_id=10718&release_id=129421

  wxPython requires wxWindows to work, which you can get here:
  http://wxWindows.org -> http://wxwindows.org/downld2.htm

  XboxIfy is known to work with Python 2.2.2, wxPython 2.3.4.2 and
  wxWindows 2.4.0 on Windows and Linux.

  For Windows, download stable releaseses from the URLs mentioned above.
  Linux users might be able to find Python et.al. in their distribution.

  Installation instructions for Python and all the other required
  libraries are out of scope of this documentation.  For me, everything
  worked out of the box on Windows XP Pro and Linux with the above mentioned
  files - YMMV.

  Once you've got everything installed, you SHOULD be able to start XboxIfy
  by executing:

  python XboxIfy.py

  This requires, that the system can find the python executable in the PATH.

--------------------------------------------------------------------------------

Usage:

  Start the program as described above under "Installation" and follow
  the GUI ;)

  Notes:
  "Funny Characters" is a translation table for characters which aren't 
  allowed to exist in to-be transferred filenames, because of limitations
  of the Xbox FATX filesystem.  In the default configuration, it's preset
  with values which just allow "plain" (boring *G*) characters like
  a, b, c, ... to survive.  "Special" characters like ä, ö, ü ... are
  removed.
  With the help of the Funny Characters table, you could setup XboxIfy so,
  that it translates from/to many characters.  Ie. it's possible to 
  translate ß -> ss or (c) -> c or _-_ -> - or what not...
  
  The drop down box "Change Case" is only half way implemented right now.
  Only the options "No Change", "Init Caps", "All Lowercase" and 
  "All Uppercase" work.  I didn't yet get around to implement 
  "Init Caps; Lowercase in ()" and "Init Caps; Uppercase in ()" because
  I can't see a reason for these options....
  Everything else should work as advertised.

--------------------------------------------------------------------------------

Updates:

  You can find new versions of this program at:

  	http://xboxify.berlios.de

  If you've got any problems with this program, feel free to send me an email:

  	Alexander Skwar <XboxIfy@message-center.info>

--------------------------------------------------------------------------------

License:

  This program is released under the GNU Public License v2.  Please see the
  file COPYING.txt for the full license information.


  
