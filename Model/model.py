from PySide6.QtCore import QAbstractListModel, QModelIndex
from PySide6.QtCore import Qt, Signal, Slot, QUrl
import os, threading

class PictureModel(QAbstractListModel):

    PATH_ROLE = Qt.UserRole + 1

    dataChanged = Signal()

    def __init__(self):
        super(PictureModel, self).__init__()
        print("-- PictureModel")

        self.pictureFolder=""
        self.pictures = []
        self.currentIndex = 0

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == PictureModel.PATH_ROLE:
            return self.pictures[row]["path"]
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.pictures)

    def roleNames(self):
        return {
            PictureModel.PATH_ROLE: b'path',
        }

    @Slot(str, str)
    def addPicture(self, path=""):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.pictures.append({'path': path})
        self.endInsertRows()
    
    # @Slot(int, str, str)
    # def insertPicture(self, row, path):
    #     self.beginInsertRows(QModelIndex(), row, row)
    #     self.pictures.insert(row, {'path': path})
    #     self.endInsertRows()

    # @Slot(int, str, str)
    # def editPicture(self, row, path):
    #     ix = self.index(row, 0)
    #     self.pictures[row] = {'path': path}
    #     self.dataChanged.emit(ix, ix, self.roleNames())

    # @Slot(int)
    # def deletePicture(self, row):
    #     self.beginRemoveColumns(QModelIndex(), row, row)
    #     del self.pictures[row]
    #     self.endRemoveRows()
    
    @Slot(QUrl)
    def setPictureFolder(self, _path):
        print("---- setPictureFolder")
        if(os.path.isdir(_path.toLocalFile())):
            self.pictureFolder = _path.toLocalFile()
            # self.loadPictures()
            threading.Thread(target = self.loadPictures).start()

    def loadPictures(self):
        print("---- loadDataset")
        for entry in os.scandir(self.pictureFolder):
            if entry.is_file(follow_symlinks=False) and entry.path.endswith(".jpg"):
                self.addPicture(path=entry.path)
                
        print("------", len(self.pictures), "Images founded")
