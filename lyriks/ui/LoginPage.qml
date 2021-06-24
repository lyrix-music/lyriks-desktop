import QtQuick 2.6
import QtQuick.Layouts 1.2
import QtQuick.Controls 2.0
import org.kde.kirigami 2.13 as Kirigami

Kirigami.Page
{
    title: "Login"

    ColumnLayout {
        width: parent.width

        Label {
            text: "User Id:"
        }
        TextField {
            Layout.fillWidth: true
            placeholderText: "@beethoven@greatmusicians.xyz"
        }
        Label {
            text: "Password"
        }
        TextField {
            Layout.fillWidth: true
            placeholderText: "my super strong password"
            echoMode: TextInput.Password
        }

        RowLayout {
            width: parent.width
            Button {
                text: "Login"
                Layout.fillWidth: true
            }
            Button {
                text: "Register"
                Layout.fillWidth: true
                
            }
        }
        Button {
            text: "Continue without logging in"
            Layout.fillWidth: true
        }

    }

}