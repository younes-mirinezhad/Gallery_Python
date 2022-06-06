import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15
import Qt.labs.platform 1.1

Pane {
    id: topbar_Itm
    Material.elevation: 10
    padding: 0
    property alias selectedFolder: folder_dlg.folder
    property int imageSize: imageSizeSlider.value

    FolderDialog { id: folder_dlg }

    RowLayout {
        anchors.fill: parent
        Item { Layout.preferredWidth: 20 }
        Label { text: "Images folder:" }
        TextField {
            Layout.fillWidth: true
            Layout.preferredHeight: 40
            readOnly: true
            text: topbar_Itm.selectedFolder
            placeholderText: "Select images folder"
            verticalAlignment: TextField.AlignVCenter
            horizontalAlignment: TextField.AlignHCenter
        }
        IconButton {
            text_visible: false
            icon_visible: true
            icon_btn: "../Icons/folder.png"
            width: 25
            height: 25
            onClicked: folder_dlg.open()
        }
        Item { Layout.preferredWidth: 20 }
        Label { text: "Image Size:" }
        Slider {
            id: imageSizeSlider
            Layout.preferredWidth: 100
            stepSize: 25
            from: 100
            to: 300
            value: 200
            snapMode: Slider.SnapAlways
        }
        Item { Layout.preferredWidth: 20 }
    }
}
