from typing import Tuple, List

import dbus


def get_current_song(player: str) -> Tuple[str, str, str]:
    if player == "":
        player = "org.mpris.MediaPlayer2.elisa"
    session_bus = dbus.SessionBus()
    player_bus = session_bus.get_object(
        player, "/org/mpris/MediaPlayer2"
    )
    player_properties = dbus.Interface(player_bus, "org.freedesktop.DBus.Properties")
    metadata = player_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    
    artists = metadata.get("xesam:artist")
    if not artists:
        return "", "", ""
    try:
        if artists.signature == "s":
            artist = str(artists[0])    
        else:
            artist = str(artists)
    except AttributeError:
        artist = str(artists)
        
    artist = str(artist).replace(" - Topic", "")
    if not artist:
        return "", "", ""

    title = str(metadata["xesam:title"])
    album_art = str(metadata.get("mpris:artUrl", ""))
    return title, artist, album_art


def get_players() -> List[str]:
    """
    Get a list of supported music players
    :return:
    :rtype:
    """
    session_bus = dbus.SessionBus()
    valid_players = []
    for i in session_bus.list_names():
        if i.startswith("org.mpris.MediaPlayer2"):
            valid_players.append(i)
    return valid_players
