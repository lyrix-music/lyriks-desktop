import QtQuick 2.6
import QtQuick.Layouts 1.2
import QtQuick.Controls 2.0
import org.kde.kirigami 2.13 as Kirigami



Kirigami.Page
{
    id: root
    title: "Lyriks"
    
    signal playerChanged(string playerName)
    
    
    ColumnLayout {
        width: parent.width
        height: parent.height

        RowLayout {
            width: parent.width
            visible: true

            Image {
                Layout.preferredHeight: trackInformationColumn.implicitHeight
                Layout.preferredWidth: trackInformationColumn.implicitHeight
                id: albumArt
                
                source: lyrixAlbumArt
            }
            ColumnLayout {
                id: trackInformationColumn
                Kirigami.Heading {
                    level: 1
                    id: trackNameLabel
                    text: lyrixTrack === "" ? "🎵" : lyrixTrack

                }
                Label {
                    id: artistNameLabel
                    text: lyrixArtist === "" ? "You are currently not listening to any song" : lyrixArtist
                }
            }
        
        }

        ComboBox {
            visible: true
            width: parent.width
            model: availablePlayers
            onCurrentIndexChanged: {
                console.warn(availablePlayers[currentIndex])
                lx.playerChanged(availablePlayers[currentIndex])
            }
        }
    
        RowLayout {
        
            visible: false
            width: parent.width
            CheckBox {
                id: scrobbleCheckBox
                text: "Scrobble"
                onCheckedChanged: {
                    
                    lx.outputStr("Hello")
                }
            }
            CheckBox {
                id: broadcastCheckBox
                text: "Broadcast"
            }
            
        }

        Flickable {
            id: flickable
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.bottomMargin: Kirigami.Units.largeSpacing

            TextArea.flickable: TextArea {
                text: lyrixLyrics
                readOnly: true
                wrapMode: TextArea.Wrap
            }

            ScrollBar.vertical: ScrollBar { }
        }
        /*TextArea {
            readOnly: true
            
            text: lyrixLyrics
            
            
        }*/
       

    }

}