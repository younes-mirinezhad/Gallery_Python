import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.15

MouseArea {
    id: control
    width: 75
    height: 30
    property string icon_btn
    property bool icon_visible: false
    property string text_btn
    property bool text_visible: true
    property bool clicked: false
    property int radius: 5
    property int contentLeftMargin: 0
    property string buttonColor: enabled ? "white" : "grey"

    Rectangle {
        radius: control.radius
        anchors.fill: parent
        color: control.buttonColor

        RowLayout{
            anchors.fill: parent

            Item { Layout.fillWidth: !img.visible }
            Image{
                id: img
                visible: control.icon_visible
                source: control.icon_btn
                Layout.preferredWidth: control.height
                Layout.preferredHeight: control.height
                Layout.leftMargin: control.contentLeftMargin
            }
            Text{
                id: txt
                visible: control.text_visible ? x + width + 15 < control.width : 0
                text: control.text_btn
                Layout.leftMargin: control.contentLeftMargin
            }
            Item { Layout.fillWidth: true }
        }
    }
}
