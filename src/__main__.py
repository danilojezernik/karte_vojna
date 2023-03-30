from src.app.gui import Gui
from src.app.tui import Tui

app = Gui()

while not app.konec():
    app.narisi()
    app.vnos()
    app.naslednja_runda()
