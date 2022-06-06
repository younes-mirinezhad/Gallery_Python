import QtQuick 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "./Qml" as Ctrl

ApplicationWindow {
    id: root
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Red
    width: 1280
    height: 720
    title: qsTr("Gallery")

    Item {
        id: mainItm
        anchors.fill: parent

        Ctrl.Topbar {
            id: topbar
            anchors {
                top: mainItm.top
                left: mainItm.left
                right: mainItm.right
                leftMargin: 5
                rightMargin: 5
            }
            height: 40
        }
        Ctrl.Gallery {
            id: gallery
            anchors {
                top: topbar.bottom
                left: mainItm.left
                right: mainItm.right
                bottom: mainItm.bottom
            }
            imageSize: topbar.imageSize
            folderPath: topbar.selectedFolder
        }
    }
}
