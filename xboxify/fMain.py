#Boa:Frame:fMain

import string
import re
import os
import DirectoryWalkerThread
import time

from wxPython.wx import *
from wxPython.html import *
from wxPython.lib.buttons import *
from wxPython.grid import *

def create(parent):
    return fMain(parent)

[wxID_FMAIN, wxID_FMAINBTNADDROW, wxID_FMAINBTNDEFAULTCFG, 
 wxID_FMAINBTNDELETEROW, wxID_FMAINBTNFOLDERBROWSE, wxID_FMAINBTNSAVECFG, 
 wxID_FMAINBTNSTART, wxID_FMAINCBREMOVE2SPACES, wxID_FMAINCBREMOVESPACESFIRST, 
 wxID_FMAINCBREMOVESTRINPARA, wxID_FMAINCHCHANGECASE, wxID_FMAINGRFUNNYCHARS, 
 wxID_FMAINHTMLDOCUMENTATION, wxID_FMAINNBMAIN, wxID_FMAINPNBFUNNY, 
 wxID_FMAINPNBMAIN, wxID_FMAINSBMAIN, wxID_FMAINSL1, wxID_FMAINSTATICLINE1, 
 wxID_FMAINSTCHANGECASE, wxID_FMAINSTFOLDER, wxID_FMAINSTIFNAMETOOLONG, 
 wxID_FMAINSTMAXLENNAMES, wxID_FMAINSTRULES, wxID_FMAINTCFOLDER, 
 wxID_FMAINTCMAXLENNAMES, wxID_FMAINWINRULES, 
] = map(lambda _init_ctrls: wxNewId(), range(27))

class fMain(wxFrame):
    def _init_coll_sbMain_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(i=0, text='XboxIfy')

        parent.SetStatusWidths([-1])

    def _init_coll_nbMain_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(bSelect=true, imageId=-1, pPage=self.pnbMain,
              strText='Main')
        parent.AddPage(bSelect=false, imageId=-1, pPage=self.pnbFunny,
              strText='Funny Characters')
        parent.AddPage(bSelect=false, imageId=-1, pPage=self.htmlDocumentation,
              strText='Documentation')

    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_FMAIN, name='fMain', parent=prnt,
              pos=wxPoint(847, 431), size=wxSize(340, 391),
              style=wxCAPTION | wxSYSTEM_MENU | wxMINIMIZE_BOX | wxTAB_TRAVERSAL,
              title='XboxIfy')
        self._init_utils()
        self.SetClientSize(wxSize(332, 357))
        self.Center(wxBOTH)

        self.sbMain = wxStatusBar(id=wxID_FMAINSBMAIN, name='sbMain',
              parent=self, style=0)
        self.sbMain.SetPosition(wxPoint(0, 357))
        self.sbMain.SetSize(wxSize(332, 20))
        self._init_coll_sbMain_Fields(self.sbMain)
        self.SetStatusBar(self.sbMain)

        self.nbMain = wxNotebook(id=wxID_FMAINNBMAIN, name='nbMain',
              parent=self, pos=wxPoint(0, 0), size=wxSize(332, 337), style=0)

        self.pnbMain = wxPanel(id=wxID_FMAINPNBMAIN, name='pnbMain',
              parent=self.nbMain, pos=wxPoint(0, 0), size=wxSize(324, 311),
              style=wxTAB_TRAVERSAL)

        self.pnbFunny = wxPanel(id=wxID_FMAINPNBFUNNY, name='pnbFunny',
              parent=self.nbMain, pos=wxPoint(0, 0), size=wxSize(324, 311),
              style=wxTAB_TRAVERSAL)

        self.stFolder = wxStaticText(id=wxID_FMAINSTFOLDER, label='Folder:',
              name='stFolder', parent=self.pnbMain, pos=wxPoint(8, 16),
              size=wxSize(120, 13), style=0)

        self.tcFolder = wxTextCtrl(id=wxID_FMAINTCFOLDER, name='tcFolder',
              parent=self.pnbMain, pos=wxPoint(8, 32), size=wxSize(208, 21),
              style=0, value='C:\\')

        self.btnFolderBrowse = wxButton(id=wxID_FMAINBTNFOLDERBROWSE,
              label='Browse', name='btnFolderBrowse', parent=self.pnbMain,
              pos=wxPoint(232, 32), size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.btnFolderBrowse, wxID_FMAINBTNFOLDERBROWSE,
              self.OnBtnfolderbrowseButton)

        self.winRules = wxWindow(id=wxID_FMAINWINRULES, name='winRules',
              parent=self.pnbMain, pos=wxPoint(8, 64), size=wxSize(296, 184),
              style=wxSUNKEN_BORDER)

        self.stRules = wxStaticText(id=wxID_FMAINSTRULES, label='Rules:',
              name='stRules', parent=self.winRules, pos=wxPoint(8, 8),
              size=wxSize(36, 13), style=0)
        self.stRules.SetFont(wxFont(8, wxSWISS, wxNORMAL, wxBOLD, false,
              'MS Shell Dlg'))

        self.stMaxLenNames = wxStaticText(id=wxID_FMAINSTMAXLENNAMES,
              label='Maximum Length of Filenames:', name='stMaxLenNames',
              parent=self.winRules, pos=wxPoint(16, 24), size=wxSize(176, 15),
              style=0)

        self.tcMaxLenNames = wxTextCtrl(id=wxID_FMAINTCMAXLENNAMES,
              name='tcMaxLenNames', parent=self.winRules, pos=wxPoint(224, 20),
              size=wxSize(40, 21), style=0, value='42')

        self.sl1 = wxStaticLine(id=wxID_FMAINSL1, name='sl1',
              parent=self.winRules, pos=wxPoint(24, 48), size=wxSize(232, 2),
              style=0)

        self.stIfNameTooLong = wxStaticText(id=wxID_FMAINSTIFNAMETOOLONG,
              label='If name of file is too long, then:',
              name='stIfNameTooLong', parent=self.winRules, pos=wxPoint(16, 56),
              size=wxSize(216, 15), style=0)

        self.cbRemove2Spaces = wxCheckBox(id=wxID_FMAINCBREMOVE2SPACES,
              label='Remove double spaces', name='cbRemove2Spaces',
              parent=self.winRules, pos=wxPoint(16, 72), size=wxSize(240, 13),
              style=0)
        self.cbRemove2Spaces.SetValue(true)

        self.cbRemoveStrInPara = wxCheckBox(id=wxID_FMAINCBREMOVESTRINPARA,
              label='Remove items in () at end of name',
              name='cbRemoveStrInPara', parent=self.winRules, pos=wxPoint(16,
              88), size=wxSize(240, 13), style=0)
        self.cbRemoveStrInPara.SetValue(false)

        self.cbRemoveSpacesFirst = wxCheckBox(id=wxID_FMAINCBREMOVESPACESFIRST,
              label='Remove spaces, before losing characters',
              name='cbRemoveSpacesFirst', parent=self.winRules, pos=wxPoint(16,
              104), size=wxSize(240, 15), style=0)
        self.cbRemoveSpacesFirst.SetValue(false)

        self.staticLine1 = wxStaticLine(id=wxID_FMAINSTATICLINE1,
              name='staticLine1', parent=self.winRules, pos=wxPoint(24, 128),
              size=wxSize(232, 2), style=0)

        self.stChangeCase = wxStaticText(id=wxID_FMAINSTCHANGECASE,
              label='Change Case:', name='stChangeCase', parent=self.winRules,
              pos=wxPoint(16, 148), size=wxSize(80, 13), style=0)

        self.chChangeCase = wxChoice(choices=['No Change', 'Init Caps',
              'Init Caps; Lowercase Items in ()',
              'Init Caps; Uppercase Items in ()', 'All Uppercase',
              'All Lowercase'], id=wxID_FMAINCHCHANGECASE, name='chChangeCase',
              parent=self.winRules, pos=wxPoint(144, 144), size=wxSize(125, 21),
              style=0, validator=wxDefaultValidator)
        self.chChangeCase.SetSelection(0)

        self.btnStart = wxButton(id=wxID_FMAINBTNSTART, label='Start',
              name='btnStart', parent=self.pnbMain, pos=wxPoint(16, 264),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.btnStart, wxID_FMAINBTNSTART, self.OnBtnstartButton)

        self.btnDefaultCfg = wxButton(id=wxID_FMAINBTNDEFAULTCFG,
              label='Default Config', name='btnDefaultCfg', parent=self.pnbMain,
              pos=wxPoint(112, 264), size=wxSize(88, 23), style=0)
        EVT_BUTTON(self.btnDefaultCfg, wxID_FMAINBTNDEFAULTCFG,
              self.OnBtndefaultcfgButton)

        self.btnSaveCfg = wxButton(id=wxID_FMAINBTNSAVECFG, label='Save Config',
              name='btnSaveCfg', parent=self.pnbMain, pos=wxPoint(224, 264),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.btnSaveCfg, wxID_FMAINBTNSAVECFG,
              self.OnBtnsavecfgButton)

        self.grFunnyChars = wxGrid(id=wxID_FMAINGRFUNNYCHARS,
              name='grFunnyChars', parent=self.pnbFunny, pos=wxPoint(24, 56),
              size=wxSize(272, 232), style=0)
        self.grFunnyChars.SetDefaultColSize(63)
        self.grFunnyChars.SetLabel('')
        self.grFunnyChars.SetAutoLayout(false)
        EVT_GRID_CELL_CHANGE(self.grFunnyChars,
              self.OnGrfunnycharsGridCellChange)

        self.btnAddRow = wxGenBitmapTextButton(ID=wxID_FMAINBTNADDROW,
              bitmap=wxBitmap('Add.gif', wxBITMAP_TYPE_GIF), label='Add',
              name='btnAddRow', parent=self.pnbFunny, pos=wxPoint(40, 16),
              size=wxSize(76, 30), style=0)
        EVT_BUTTON(self.btnAddRow, wxID_FMAINBTNADDROW, self.OnBtnaddrowButton)

        self.btnDeleteRow = wxGenBitmapTextButton(ID=wxID_FMAINBTNDELETEROW,
              bitmap=wxBitmap('Delete.gif', wxBITMAP_TYPE_GIF), label='Delete',
              name='btnDeleteRow', parent=self.pnbFunny, pos=wxPoint(208, 16),
              size=wxSize(76, 30), style=0)
        EVT_BUTTON(self.btnDeleteRow, wxID_FMAINBTNDELETEROW,
              self.OnBtndeleterowButton)

        self.htmlDocumentation = wxHtmlWindow(id=wxID_FMAINHTMLDOCUMENTATION,
              name=u'htmlDocumentation', parent=self.nbMain, pos=wxPoint(0, 0),
              size=wxSize(324, 311))

        self._init_coll_nbMain_Pages(self.nbMain)

    def __init__(self, parent):
        """This method contains "stuff" run, when the application initializes."""
        
        self._init_ctrls(parent)
        
        # Set values used for configuration (wxConfig)
        self.cfg_app_name = 'XboxIfy'
        self.cfg_app_vendor = 'Alexander Skwar'
        self.cfg_local_file_nt = 'XboxIfy'
        self.cfg_local_file_posix = '.xboxify'
        self.cfg_keys = {
            'path': 'Path',
                'maxNameLen': 'Maximum length of filenames',
                'remove2Spaces': 'Remove double spaces',
                'removeParas': 'Remove text in () first',
                'removeSpacesFirst': 'Remove spaces before losing text',
                'changeCase': 'Change Case style'
        }
        self.cfg_paths = {
            'global': 'Global',
                'funnyCharacters': 'Funny Characters'
        }

        # Try to load the stored configuration.  If not present, sets a default config.
        self.LoadConfig()

        # Set an icon for the frame - because it's nicer ;)
        icon_file = 'xbox-icon.ico'
        icon_type = wxBITMAP_TYPE_ICO
        self.icon = wxIcon(icon_file, icon_type)
        self.SetIcon(self.icon)


#------------------------------------------------------------------------------#
#                     Buttons                                                  #
#------------------------------------------------------------------------------#

    def OnBtnfolderbrowseButton(self, event):
        """Present a dialog for browsing the filesystem, so that the user can
        select a directory which XboxIfy is to operate on."""
        
        dlg = wxDirDialog(self)
        try:
            if dlg.ShowModal() == wxID_OK:
                dir = dlg.GetPath()
                self.tcFolder.SetValue(dir)
        finally:
            dlg.Destroy()

        event.Skip()

    def OnBtnstartButton(self, event):
        """Start the show! ;)"""

        busy = wxBusyInfo('Renaming files.  Please wait...')
        busyCursor = wxBusyCursor()
        timer_start = time.time()
        clock_start = time.clock()

        # Read "simple" values from the frame
        path                = self.tcFolder.GetValue()
        maxNameLen          = self.tcMaxLenNames.GetValue()
        remove2Spaces       = self.cbRemove2Spaces.GetValue()
        removeParas         = self.cbRemoveStrInPara.GetValue()
        removeSpacesFirst   = self.cbRemoveSpacesFirst.GetValue()
        changeCase          = self.chChangeCase.GetSelection()
        changeCaseStr       = self.chChangeCase.GetString(self.chChangeCase.GetSelection())

        # Get the funny characters translation
        regex, translate, trans_table, delete_chars = self.ReadFunnyCharsGrid()

        # Walk the Directory Tree
        self.SetStatusText('Getting list of files and directories...')
        
        # Create the directory walker thread
        dwThread = DirectoryWalkerThread.DirectoryWalkerThread(folder = path)
        
        # Start the thread
        dwThread.start()
        
        # As long as the thread is running, print the current position
        i = j = 0
        while dwThread.isAlive():
            if j > 4:
                self.SetStatusText(dwThread.getDirWalker().getCurrent())
                j = 0
            else:
                j += 1
            if i > 11:
                wx.wxYield()
                i = 0
            else:
                i += 1
        
        # Get a list of all the directories
        dirs = dwThread.getDirWalker().getDirs()
        # Reverse it, so that we're renaming subdirectories before their parents.
        dirs.reverse()
        # Get a list of all the filenames
        files = dwThread.getDirWalker().getFiles()
        
##        print "Files:\n%s\n\nDirs:\n%s\n" % (files, dirs)

        # Rename the files
        new_files = self.BeautifyNames(
            names=files,
            maxNameLen=maxNameLen,
            remove2Spaces=remove2Spaces,
            removeParas=removeParas,
            removeSpacesFirst=removeSpacesFirst,
            changeCase=changeCase, regexp=regex,
            translate=translate,
            trans_table=trans_table,
            delete_chars=delete_chars,
            status_text_prefix='Files: '
        )

        # Now rename the directories
        new_dirs = self.BeautifyNames(
            names=dirs,
            maxNameLen=maxNameLen,
            remove2Spaces=remove2Spaces,
            removeParas=removeParas,
            removeSpacesFirst=removeSpacesFirst,
            changeCase=changeCase, regexp=regex,
            translate=translate,
            trans_table=trans_table,
            delete_chars=delete_chars,
            status_text_prefix='Dirs: '
        )
        
        timer_end = time.time()
        clock_end = time.clock()
        
        timer = timer_end - timer_start
        clock = clock_end - clock_start
        
        self.SetStatusText('Done! Elapsed time: %.1f seconds' % timer)

        # We're no longer busy ;)
        del busy
        del busyCursor
        event.Skip()

    def OnBtndefaultcfgButton(self, event):
        """Reset the configuration to default values."""
        
        # Get default configuration
        self.SetDefaultConfig()
        
        # Done
        event.Skip()

    def OnBtnsavecfgButton(self, event):
        """User whishes to store the current configuration."""

        # Store configuration
        self.SaveConfig()

        # Done.
        event.Skip()

    def OnBtnaddrowButton(self, event):
        """Append a blank row to the grid."""

        # Add one row to the end of the grid ...
        self.grFunnyChars.AppendRows(1)
        new_row = (self.grFunnyChars.GetNumberRows() - 1)
        new_col = self.grFunnyChars.GetGridCursorCol()
        # ... move the cursor to it ...
        self.grFunnyChars.SetGridCursor(new_row, new_col)
        # ... and make it visible.
        self.grFunnyChars.MakeCellVisible(new_row, new_col)
        # Done.
        event.Skip()

    def OnBtndeleterowButton(self, event):
        """Delete the row, in which the cursor is in."""
        
        row = self.grFunnyChars.GetGridCursorRow()
        rowCnt = self.grFunnyChars.GetNumberRows()
        if ((rowCnt > 0) and (row >= 0)):
            if (row == (rowCnt - 1)):
                if (rowCnt > 1):
                    self.grFunnyChars.SetGridCursor(row - 1,
                                            self.grFunnyChars.GetGridCursorCol())
            self.grFunnyChars.DeleteRows(row, 1)
            
        event.Skip()

#------------------------------------------------------------------------------#
#                     Grid                                                     #
#------------------------------------------------------------------------------#

    def OnGrfunnycharsGridCellChange(self, event):
        """Update either the corrsponding 'Dec.' column or the ASCII representation."""
        
        selectedValue = self.grFunnyChars.GetCellValue(event.GetRow(), event.GetCol())
        
        if ((event.GetCol() == 1) or (event.GetCol() == 3)):
            targetCol = (event.GetCol() - 1)
            try:
                ascii = string.join(map(lambda i:chr(int(i, 10)),
                                          string.split(selectedValue, ':')), '')
            except:
                ascii = ''
            convertedValue = ascii
        else:
            targetCol = (event.GetCol() + 1)
            try:
                dec = string.join(map(lambda i:`ord(i)` , selectedValue), ':')
            except:
                dec = ''
            convertedValue = dec
            
        self.grFunnyChars.SetCellValue(event.GetRow(), targetCol, convertedValue)
        
        event.Skip()


#------------------------------------------------------------------------------#
#                     Self made methods                                        #
#------------------------------------------------------------------------------#

    def LoadConfig(self):
        """Load the stored configuration (if present).  If no configuration has
        been stored, it will set default values."""

        # First set a default config.  The values will be overwritten by the
        # stored values, if present.
        self.SetDefaultConfig()

        # Posix (Linux) needs to load/store the config differently than Windows (NT)
        if (os.name == 'posix'):
            cfg = wxConfig(self.cfg_app_name, self.cfg_app_vendor, self.cfg_local_file_posix)
        elif (os.name == 'nt'):
            cfg = wxConfig(self.cfg_app_name, self.cfg_app_vendor, self.cfg_local_file_nt)

        # Do we have the "Global" config scope?
        if cfg.Exists(self.cfg_paths['global']):
            # Yes, we do.  Decend into it
            cfg.SetPath(self.cfg_paths['global'])
            # Load all the items we're interested in - if present
            if cfg.HasEntry(self.cfg_keys['path']):
                self.tcFolder.SetValue(cfg.Read(self.cfg_keys['path']))
            if cfg.HasEntry(self.cfg_keys['maxNameLen']):
                self.tcMaxLenNames.SetValue(cfg.Read(self.cfg_keys['maxNameLen']))
            if cfg.HasEntry(self.cfg_keys['remove2Spaces']):
                self.cbRemove2Spaces.SetValue(cfg.ReadInt(self.cfg_keys['remove2Spaces']))
            if cfg.HasEntry(self.cfg_keys['removeParas']):
                self.cbRemoveStrInPara.SetValue(cfg.ReadInt(self.cfg_keys['removeParas']))
            if cfg.HasEntry(self.cfg_keys['removeSpacesFirst']):
                self.cbRemoveSpacesFirst.SetValue(cfg.ReadInt(self.cfg_keys['removeSpacesFirst']))
            if cfg.HasEntry(self.cfg_keys['changeCase']):
                self.chChangeCase.SetSelection(cfg.ReadInt(self.cfg_keys['changeCase']))
            # Move up one level
            cfg.SetPath('..')

        # Do we have the "Funny Characters" config scope?
        if cfg.Exists(self.cfg_paths['funnyCharacters']):
            # Yessir -> Go there.
            cfg.SetPath(self.cfg_paths['funnyCharacters'])
            # Empty the grid with the funny characters
            self.grFunnyChars.ClearGrid()
            self.grFunnyChars.DeleteRows(0, self.grFunnyChars.GetNumberRows())

            # Loop through all the entries of this config scope
            entry = cfg.GetFirstEntry()
            # Add rows to the grid
            self.grFunnyChars.AppendRows(cfg.GetNumberOfEntries())
            curRow = 0
            # As long as there are entries, loop
            while entry[0]:
                # Get the name of the entry.  It's our decimal value
                dec_from = entry[1]
                # Decode the decimal value
                ascii_from = string.join(map(lambda i:chr(int(i, 10)), string.split(dec_from, ':')), '')
                # Get to what this is to be translated.
                dec_to = cfg.Read(dec_from)
                # It might be, that it is to be translated to nothing; ie. delete
                ascii_to = ''
                if (dec_to.strip() != ''):
                    ascii_to = string.join(map(lambda i:chr(int(i, 10)), string.split(dec_to, ':')), '')
                # Add the values to the grid
                self.grFunnyChars.SetCellValue(curRow, 0, ascii_from)
                self.grFunnyChars.SetCellValue(curRow, 1, dec_from)
                self.grFunnyChars.SetCellValue(curRow, 2, ascii_to)
                self.grFunnyChars.SetCellValue(curRow, 3, dec_to)
                curRow += 1
                # Get next entry
                entry = cfg.GetNextEntry(entry[2])

            # Up one level
            cfg.SetPath('..')
        
        del cfg
        
        return None

    def SaveConfig(self):
        """Store the current configuration."""
        
        # Read values from the frame
        path = self.tcFolder.GetValue()
        maxNameLen = self.tcMaxLenNames.GetValue()
        remove2Spaces = self.cbRemove2Spaces.GetValue()
        removeParas = self.cbRemoveStrInPara.GetValue()
        removeSpacesFirst = self.cbRemoveSpacesFirst.GetValue()
        changeCase = self.chChangeCase.GetSelection()

        # Linux (Posix) and Windows (NT) need different calls to create the config
        if (os.name == 'posix'):
            cfg = wxConfig(self.cfg_app_name, self.cfg_app_vendor,
                            self.cfg_local_file_posix)
        elif (os.name == 'nt'):
            cfg = wxConfig(self.cfg_app_name, self.cfg_app_vendor,
                            self.cfg_local_file_nt)

        # Go to the "Global" configuration scope
        cfg.SetPath(self.cfg_paths['global'])
        # And write stuff
        cfg.Write(self.cfg_keys['path'], path)
        cfg.Write(self.cfg_keys['maxNameLen'], maxNameLen)
        cfg.WriteInt(self.cfg_keys['remove2Spaces'], remove2Spaces)
        cfg.WriteInt(self.cfg_keys['removeParas'], removeParas)
        cfg.WriteInt(self.cfg_keys['removeSpacesFirst'], removeSpacesFirst)
        cfg.WriteInt(self.cfg_keys['changeCase'], changeCase)
        # Leave "Global" scope
        cfg.SetPath('..')

        # If there's a "Funny Characters" scope, remove it, so that deleted
        # items from the grid are also deleted from the configuration.
        if cfg.HasGroup(self.cfg_paths['funnyCharacters']):
            cfg.DeleteGroup(self.cfg_paths['funnyCharacters'])

        # Now go to the "Funny Characters" scope
        cfg.SetPath(self.cfg_paths['funnyCharacters'])
        # And store all the "Funny Characters".  Store the decimal values,
        # because these are just ASCII values
        for rowNum in range(self.grFunnyChars.GetNumberRows()):
            cfg.Write(self.grFunnyChars.GetCellValue(rowNum, 1),
                        self.grFunnyChars.GetCellValue(rowNum, 3))

        # Done with "Funny Characters" scope
        cfg.SetPath('..')
        # Make sure configuration gets written
        cfg.Flush()
        # We no longer need the configuration here.
        del cfg

    def SetDefaultConfig(self):
        """Set a default configuration for the application."""

        self.CreateDefaultFunnyCharsGrid()
        self.cbRemove2Spaces.SetValue(1)
        self.cbRemoveStrInPara.SetValue(0)
        self.cbRemoveSpacesFirst.SetValue(0)
        self.chChangeCase.SetSelection(0)
        self.tcMaxLenNames.SetValue('42')
        self.tcFolder.SetValue(os.getcwd())
        
        return None

    def CreateDefaultFunnyCharsGrid(self):
        """Create a grid with default values for the "Funny" characters."""

        # This may take some time - change cursor
        self.SetCursor(wxHOURGLASS_CURSOR)

        # Create a grid, if none present.
        if (self.grFunnyChars.GetTable() is None):
            self.grFunnyChars.CreateGrid(0, 4)
        else:
            # Grid present.  Delete all the rows
            self.grFunnyChars.DeleteRows(0, self.grFunnyChars.GetNumberRows())
            # Clear the grid
            self.grFunnyChars.ClearGrid()

        # Set some attributes
        self.grFunnyChars.SetLabelTextColour(wxColour(111, 191, 0))
        self.grFunnyChars.DisableDragRowSize()
        self.grFunnyChars.DisableDragColSize()
##        self.grFunnyChars.AutoSizeColumns(true)
        self.grFunnyChars.SetDefaultCellAlignment(wxALIGN_CENTRE, wxALIGN_CENTRE)
        self.grFunnyChars.SetRowLabelSize(0)
        # Add labels for the columns
        self.grFunnyChars.SetColLabelValue(0, 'Replace')
        self.grFunnyChars.SetColLabelValue(1, 'Dec.')
        self.grFunnyChars.SetColLabelValue(2, 'With')
        self.grFunnyChars.SetColLabelValue(3, 'Dec.')

        # Some default translations
        default_translations = {
            ',': '.',
            '<': '(',
            '>': ')',
            '_': ' ',
            '"': "'",
            '/': '-',
            '\\': '-',
            ':': '-',
            ';': '.',
            '=': '-'
        }

        # Tell the grid to not repaint now, because we're adding quite some rows.
        self.grFunnyChars.BeginBatch()
        start_dec = 0
        end_dec = 256
        start_to_end = range(start_dec, end_dec)
        self.grFunnyChars.AppendRows(len(start_to_end))
        curRow = 0
        for x in start_to_end:
            # The first column stores the ASCII from value
            self.grFunnyChars.SetCellValue(curRow, 0, chr(x))
            # Second column holds the decimal value
            self.grFunnyChars.SetCellValue(curRow, 1, ('%03d' % x))
            # "Some" characters are safe
            # Values stolen from PreXbCopyTool
            if ((32 <= x <= 33) or (35 <= x <= 41) or (45 <= x <= 46) or 
               (48 <= x <= 57) or (64 <= x <= 91) or (93 <= x <= 123) or 
               (125 <= x <= 126) or 
               (129 == x) or (148 == x) or (153 <= x <= 154)):
                # Third column stores ASCII to value
                self.grFunnyChars.SetCellValue(curRow, 2, chr(x))
                # Fourth column is for the Decimal to value.
                self.grFunnyChars.SetCellValue(curRow, 3, ('%03d' % x))
            # Add the default translations
            if (chr(x) in default_translations):
                self.grFunnyChars.SetCellValue(curRow, 2, default_translations[chr(x)])
                self.grFunnyChars.SetCellValue(curRow, 3, ('%03d' % ord(default_translations[chr(x)])))
            curRow += 1

        self.grFunnyChars.SetMargins(0, 0)
        # We're done with updating the grid.
        self.grFunnyChars.EndBatch()
        self.SetCursor(wxSTANDARD_CURSOR)
            
        return None

    def BeautifyNames(self, names, maxNameLen, remove2Spaces, removeParas, removeSpacesFirst, changeCase, translate, regexp, trans_table, delete_chars, status_text_prefix = ''):
        """Beautify all the names, so that they can be transferred to Xbox.
        This method RENAMES the file on the HARD DISK!
        Parameters:
            names: List of filenames.  Used as the source when renaming.
            maxNameLen: Maximum number of characters allowed in a filename.
            remove2Spaces: If name is too long, should we remove double spaces?
            removeParas: If name is too long, should stuff in () be dropped first?
            removeSpacesFirst: If name is too long, drop all spaces before losing characters?
            changeCase: The way casing of words should be changed
            translate: Dictionary for translating characters to.  Used together with regexp.
            regexp: Regular expression for translating part(s) of the filename
            trans_table: Translation table for translating single characters.
            delete_chars: List of characters which should be delete from the name.
            status_text_prefix: Prefix for output in status bar
        See also:
            self.multiple_replace
        """

        # TODO: Add fault tolerant integer conversion here!!
        try:
            maxNameLen = int(maxNameLen)
        except:
            maxNameLen = 42

        # Compile some regular expressions, because this speeds up regexps
        if remove2Spaces:
            remove2Spaces_regexp = re.compile('\\s+')
        if removeParas:
            removeParas_regexp = re.compile('[\\[({].*[\\])}]')

        new_files = []
        i = 0
        for num in range(len(names)):
##        for file in names:
            file = names.pop(0)
            if (i >= 11):
                # Give control back to the system every so often.  This causes
                # the window to be redrawn.
                wx.wxYield()
                i = 0
            else:
                i = (i + 1)

            # Display information on the status bar
            self.SetStatusText(status_text_prefix + file)

            # Split the filename into directory and filename parts
            splitted    = os.path.split(file)
            dir         = splitted[0]
            base        = splitted[1]

            # Also split the filename into root and extension
            splitted    = os.path.splitext(base)
            root        = splitted[0]
            ext         = splitted[1]

            # Work with the root.  Extension is always preserved!
            # TODO: Add code when extension is > 40 characters!
            new_base = root
            if (not (regexp is None)):
                # Do the multiple character replacements.  Ie. SZ -> 'ss' or such.
                new_base = self.multiple_replace(translate, new_base, regexp)
            if (not (trans_table is None)):
                # Do simple character translation and character deletion.
                # Eg. this will translate '<' -> '(' and delete ':'.
                new_base = new_base.translate(trans_table, delete_chars)

            # The root might have leading and trailing spaces now -> Remove!
            root = new_base.strip()

            # Does the user want to change the case of the words of the filename?
            if changeCase:
                # Yes, he does.
                if (changeCase == 1):
                    # Capitalize words.
                    # TODO: Add nicer capitalization function!
                    root = string.capwords(root)
                    
                elif 2 <= changeCase <= 3:
                    # TODO: Add code for capturing text in () and putting it back at the same place!
                    if (changeCase == 2):
                        print 'Init Caps; Lowercase in ()\n'
                        a = 2
                    else:
                        print 'Init Caps; Uppercase in ()\n'
                        a = 3
                        
                elif (changeCase == 4):
                    # UPPERCASE the whole filename
                    root = root.upper()
                    
                elif (changeCase == 5):
                    # lowercase the whole filename
                    root = root.lower()

            # Remove double spaces?
            if remove2Spaces:
                # Yes, but only if name is too long.
                if (len((root + ext)) > maxNameLen):
                    root = re.sub(remove2Spaces_regexp, ' ', root)
            # Remove things in ()?
            if removeParas:
                # Yes, but only if name is too long.
                if (len((root + ext)) > maxNameLen):
                    root = re.sub(removeParas_regexp, ' ', root)
            # Should we lose spaces before we're losing other characters?
            if removeSpacesFirst:
                # Yes, but only if name is too long.
                if (len((root + ext)) > maxNameLen):
                    root = string.translate(root, string.maketrans('', ''), ' ')
            # Is the name still too long?
            if (len((root + ext)) > maxNameLen):
                # Yes.  We've GOT to lose characters now.
                root = root[:(maxNameLen - len(ext))]
            # Reconstruct the filename.  ext (if != '') starts with a . (dot).
            new_name = os.path.join(dir, (root + ext))
            # Rename the file, if name has changed
            abs_new_name = os.path.abspath(new_name)
            # Only try to rename, if we changed the name
            if os.path.abspath(file) != abs_new_name:
##                print "##################################\n%s\n->\t%s\n" % (file, new_name)
                # For easier comparison, concatenate the lists of the yet-to-be-done
                # files in "names" and the list of renamed files in "new_files"
                # Also uppercase it, because we will not pay attention to
                # casing of filename.
                names_and_new_files = map(string.upper, names + new_files)
                # Get a list of files and subdirectories in the directory of the
                # file.  Uppercase it as well.
                dirlist = map(string.upper, os.listdir(dir))
                
                base = root + ext

                # It might happen, that the name we created already exists
                # If that's the case, try to create a unique name by
                # replacing the last 3 characters of the root with a
                # digit.  Ie. first try to use 001, then 002 etc.pp..
                # It might also happen, that the name already exists and is
                # not (yet) in the list of names AND new_files.  Because of
                # this, get a directory listing and check agains this as well.
##                print "names_and_new_files:\n"
##                for FOO in names_and_new_files:
##                    print FOO + "\n"
##                print "\nabs_new_name.upper(): " + abs_new_name.upper() + "\n"
##                if abs_new_name.upper() in names_and_new_files:
##                    print "\t\tabs_new_name.upper() in names_and_new_files:\n"
##                else:
##                    print "\t\tNICHT abs_new_name.upper() in names_and_new_files:\n"
##                    
##                print "dirlist:\n"
##                for FOO in dirlist:
##                    print FOO + "\n"
##                print "\nbase.upper(): " + base.upper() + "\n"
##                if base.upper() in dirlist:
##                    print "\t\tbase.upper() in dirlist:\n"
##                else:
##                    print "\t\tNICHT base.upper() in dirlist:\n"
                    
                if abs_new_name.upper() in names_and_new_files or base.upper() in dirlist:
##                    if abs_new_name.upper() in names_and_new_files:
##                        print "abs_new_name.upper() in names_and_new_files\n"
##                    if base.upper() in dirlist:
##                        print "base.upper() in dirlist\n"

                    # Throw away 3 characters from the end of the filename,
                    # because they'll be replaced by our number used to make
                    # the filename unique.
                    root_base = root[:-3]
                    # Start counting at 0.
                    root_num = 0
                    # Create the first filename with a suffix of '000'
                    base = "%s%03d%s" % (root_base, root_num, ext)
                    new_name = os.path.join(dir, base)
                    abs_new_name = os.path.abspath(new_name)
                    # If the new filename is NOT unique, go on with higher
                    # numbers.
                    while abs_new_name.upper() in names_and_new_files or base.upper() in dirlist:
                        # The name containing the current number is also used
                        # Try next number
                        root_num += 1
                        # Generate the next name
                        base = "%s%03d%s" % (root_base, root_num, ext)
                        new_name = os.path.join(dir, base)
                        abs_new_name = os.path.abspath(new_name)
                        
                    # Eventually, we'll find a free number (or get an overflow).
                
                new_files.append(abs_new_name)
##                print "\n->->\t%s\n" % new_name
                os.rename(file, abs_new_name)

        return new_files
    
    def multiple_replace(self, dict, text, regex):
        """Replace all occurances of the keys of the dict by their values in text.
        It expects to be given a pre-compiled regular expression in the parameter regex."""

        # Python *can* be ugly ;)
        return regex.sub(lambda mo:dict[mo.string[mo.start():mo.end()]], text)
    
    def ReadFunnyCharsGrid(self):
        """Process the grid of the "funny" characters.
        It will return a 4 tuple (regex, translate, trans_table, delete_chars).
        regex: Regular expression usable in multiple_replace containing translation
        of multiple caracters or from 1 character to multiple characters.
        translate: dictionary used to translate multiple characters.
        trans_table: translation table for string.translate() containing translation
        of single characters.
        delete_chars: list of characters which should be deleted from a file name.
        Can be passed as the 3rd parameter to string.translate().
        """

        # translate will be a dict containing muliple character translations
        # e.g. 'SZ' -> 'ss'
        translate = {}
        delete_chars = trans_from = trans_to = ''
        for rowNum in range((self.grFunnyChars.GetNumberRows() - 0)):
            col_1 = self.grFunnyChars.GetCellValue(rowNum, 0)
            col_2 = self.grFunnyChars.GetCellValue(rowNum, 1)
            col_3 = self.grFunnyChars.GetCellValue(rowNum, 2)
            col_4 = self.grFunnyChars.GetCellValue(rowNum, 3)

            # Move on to the next row, if we're either having a blank row
            # or if we're not translating a character (ie. replacing it with
            # itself).
            if ((col_2.strip() == '') or (col_2.strip() == col_4.strip())):
                continue

            # Are we translating from just 1 (one) character; ie. is the value
            # in the decimal column exactly 3 characters long (e.g. 032)?
            if (len(col_2.strip()) == 3):
                # Yes.
                if (col_4.strip() == ''):
                    # The current character is to be deleted
                    delete_chars += col_1
                elif (len(col_4.strip()) == 3):
                    # The current character is to be translated with just one
                    # other character
                    trans_from += col_1
                    trans_to += col_3
                else:
                    # The current character is to be translated with more than
                    # one character
                    translate[col_1] = col_3
            else:
                # We're translating from more than 1 character
                translate[col_1] = col_3

        # Do we have to compile a regular expression for multiple
        # character replacement?
        if (len(translate) > 0):
            # Yes, we do.
            regex_pattern = ('(%s)' % '|'.join(map(re.escape, translate.keys())))
            regex = re.compile(regex_pattern)
        else:
            # No, we don't.
            regex = None

        # Are there any simple character replacements?
        if ((len(trans_from) > 0) and (len(trans_to) > 0)):
            # Yes, there are.
            trans_table = string.maketrans(trans_from, trans_to)
        else:
            # No, there aren't.
            trans_table = None

        # Finish!
        return (regex, translate, trans_table, delete_chars)


