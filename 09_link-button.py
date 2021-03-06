import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class LinkButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LinkButton Demo")
        self.set_border_width(10)

        button = Gtk.LinkButton.new_with_label(
            uri="https://www.gtk.org",
            label="Visit GTK+ Homepage"
        )
        button.connect('clicked', self.yell)
        self.add(button)
    
    def yell(self, button):
        print('I WAS CLICKED')


win = LinkButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
