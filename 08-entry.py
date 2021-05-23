import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Entry Demo')
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text('Hello, World!')
        vbox.pack_start(self.entry, True, True, 0)
        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.check_editable = Gtk.CheckButton(label='Editable')
        hbox.pack_start(self.check_editable, True, True, 0)
        self.check_editable.connect('toggled', self.on_editable_toggled)
        self.check_editable.set_active(True)


    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)


win = EntryWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()