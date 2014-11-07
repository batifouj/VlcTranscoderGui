#! python3
#-*-coding: utf-8 -*-

"""
@file TranscoderController.py
The Controller for the transcoder
"""

from PyQt5 import QtCore
import Model.TranscoderModel as TranscoderModel

class Controller():
    """
    This is a the 'Controller' part of the MVC implementation. It deals with
    the communication between the View and the Model
    """
    def __init__(self, model, view):
        """
        The class constructor

        @param model: the model of the MVC GUI
        @param view: the view of the MVC GUI
        """
        # Save pointers to model and view
        self.model = model
        self.view = view

        # Register the controller in the model and the view
        self.model.controller = self
        self.view.controller = self

        self.ConnectModelAndView()


    def addRootDirectory(self, rootDir):
        """
        Append a root directory to the list of root directories in the Model
        """
        self.model.addRootDirectory(rootDir)


    def ConnectModelAndView(self):
        # Encapsulator
        self.encapsulatorModel = TranscoderModel.TooltipedDataListModel(
            self.model.encapsulatorsODic)
        self.view.encapsCombo.setModel(self.encapsulatorModel)

        # Video codec
        self.vCodecModel = TranscoderModel.TooltipedDataListModel(
            self.model.vCodecODic)
        self.view.vCodecCombo.setModel(self.vCodecModel)

        # Audio codec
        self.aCodecModel = TranscoderModel.TooltipedDataListModel(
            self.model.aCodecODic)
        self.view.aCodecCombo.setModel(self.aCodecModel)

        # Audio bitrate
        self.aBitRateModel = QtCore.QStringListModel(self.model.aBitRateList)
        self.view.aBitRateCombo.setModel(self.aBitRateModel)

        # Sample rate
        self.aSampleRateModel = QtCore.QStringListModel(self.model.aSampleRateList)
        self.view.aSampleRateCombo.setModel(self.aSampleRateModel)
