import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import gallery.PictureModel 1.0
import gallery.ViewPort 1.0


Item {
    id: mainItm
    property string folderPath: ""
    onFolderPathChanged: { picModel.setPictureFolder(folderPath) }
    property int imageSize: 200

    Popup {
        id: bigImgPopup
        anchors.centerIn: parent
        width: parent.width*0.85
        height: parent.height*0.85
        padding: 0
        // closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside
        // losePolicy: Popup.NoAutoClose
         closePolicy: Popup.CloseOnEscape

        ColumnLayout {
            anchors.fill: parent

            RowLayout {
                Layout.preferredHeight: 25
                Layout.fillWidth: true
                Item { Layout.fillWidth: true }
                IconButton {
                    id: closeBtn
                    width: 20
                    height: 20
                    Layout.rightMargin: 5
                    Layout.topMargin: 3
                    Layout.bottomMargin: 2
                    text_visible: false
                    icon_visible: true
                    icon_btn: "../Icons/close.png"
                    onClicked: bigImgPopup.close()
                }
            }
            Pane {
                Layout.fillHeight: true
                Layout.fillWidth: true
                padding: 0

                ViewPort {
                    id: imgPopup
                    anchors.fill: parent
                    anchors.margins: 5
                }
            }
        }

    }

    PictureModel { id: picModel}
    GridView {
        id: picGrid
        anchors.fill: parent
        clip: true
        ScrollBar.vertical: ScrollBar { width: 10 }
        cellWidth: mainItm.imageSize
        cellHeight: mainItm.imageSize

        model: picModel
        delegate: Rectangle {
            width: mainItm.imageSize - 2
            height: mainItm.imageSize - 2
            color: "transparent"
            border.width: 1
            border.color: "black"

            MouseArea {
                anchors.fill: parent

                ViewPort {
                    anchors.fill: parent
                    anchors.margins: 2
                    picPath: path
                }
                onClicked: { imgPopup.picPath = path; bigImgPopup.open() }
            }
        }
    }
}
