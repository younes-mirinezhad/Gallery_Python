# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from pathlib import Path
from Model.model import PictureModel
from Model.pictureViewPort import ViewPort


if __name__ == "__main__":
    QGuiApplication.setApplicationDisplayName("Gallery")
    QGuiApplication.setOrganizationName("ParsAI")

    qmlRegisterType(PictureModel, "gallery.PictureModel", 1, 0, "PictureModel")
    qmlRegisterType(ViewPort, "gallery.ViewPort", 1, 0, "ViewPort")

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).parent / 'main.qml'
    engine.load(qml_file)
    rootObjects = engine.rootObjects()
    if not rootObjects:
        sys.exit(-1)

    window = rootObjects[0]
    window.setIcon(QIcon('Icons/logo.png'))

    sys.exit(app.exec())
