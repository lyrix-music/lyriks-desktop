import sys

from . import rsrc_rc as _  # noqa:

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from .lyrix import LyricsFetcher, LyrixEngine


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/ui/icons/lyrix.png"))

    lyrics_fetcher = LyricsFetcher()
    lx = LyrixEngine()
    lx.songUpdated.connect(lyrics_fetcher.run)

    engine = QQmlApplicationEngine()
    # ctx = engine.rootContext()

    # ctx.setContextProperty("lx", lx)

    engine.load(":/ui/main.qml")
    engine.rootObjects()[0].setProperty("lyricsFetcher", lyrics_fetcher)
    engine.rootObjects()[0].setProperty("lx", lx)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
