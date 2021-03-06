#! python3
# -*-coding: utf-8 -*-

"""
@file InputFilesTab.py
The Input files Tab of the GUI
"""

# Import PyQt modules
from PyQt5 import QtWidgets

# Import custom modules
from NzPyQtToolBox.NzQAutoGridWidgets import NzQAutoGridCheckboxes
from DirMgr.Widget import TranscoderDirMgrWidget

# Import standard modules


class InputFilesTab(QtWidgets.QWidget):
    """
    This tab contains a file browser to select files to transcode
    """
    def __init__(self, parent):
        """
        The constructor for the Configuration tab of the GUI

        @param parent The parent widget
        """
        super().__init__(parent)
        self._parent = parent

        # Create the directory manager widget
        self.dirmgr = TranscoderDirMgrWidget(self)

        # Create the extensions manager widget
        self.extmgr = NzQAutoGridCheckboxes(self)

        # Create the grid
        grid = QtWidgets.QGridLayout()

        # Add the video file extensions for the search
        # Add widgets to the grid
        grid.addWidget(self.extmgr, 0, 0)
        grid.addWidget(self.dirmgr, 1, 0)

        self.setLayout(grid)

    def getSelectedExtensions(self):
        """
        Get the list of extensions selected by the user

        @return the unprocessed list of extensions
        """
        return self.extmgr.choices

    def getFilesFromInputTab(self):
        """
        Get the list of files

        @return the list of files
        """
        return self.dirmgr.getFiles()

    def processDirectory(self, dirpath):
        """
        Define the processing of each new directory added

        @param[in] dirpath The directory just added by the user

        @todo Improve this ugly inteface...
        """
        self._parent.controller.processDirectory(dirpath)
