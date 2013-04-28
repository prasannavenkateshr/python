#!/usr/bin/env python

import gtk
import sys
import pygtk
pygtk.require('2.0')
import gobject
import webkit
from webkit import WebView
import pango
from inspector import Inspector

def go_button(widget):
    address = urlbar.get_text()
    if address.startswith("http://"):
        surfer.open(address)
    elif address.startswith("https://"):
        surfer.open(address)
    else:
        address = "http://" + address
        urlbar.set_icon_from_stock(0,gtk.STOCK_INFO)
        urlbar.set_text(address)
  surfer.open(address)

def go_backbutton(widget):
    surfer.go_back()

def go_forwardbutton(widget, data=None):
    surfer.go_forward()

def go_refbutton(widget):
    surfer.reload()

def go_homebutton(widget):
    surfer.go_home()

def go_stopbutton(widget):
    surfer.stop_loading()

def seturl(widget, data=None):
    urlbar.set_text( widget.get_main_frame().get_uri() )
    back.set_sensitive(surfer.can_go_back())
    forward.set_sensitive(surfer.can_go_forward())
    #urlbar.set_icon_from_file("globe.png")
    

def title_chg(view, frame, title):
    window.set_title(("%s - Waterske Surfer") % title)

def add_tab_cb(button):
    surfer.emit(new_tab)

def load_progress_amount(webview, amount):
    notify.set_fraction(amount/100.0)
  
def load_started(webview, frame):
    notify.set_visible(True)

def load_finished(webview, frame):
    notify.set_visible(False)

def delete_event(widget, event, data=None):
    return False

def estimated_load(widget):
    surfer.get_estimated_load_progress()

def on_destroy(widget, event):
    gtk.main_quit()

def on_close_clicked(tab_label, notebook, tab_widget):
    notebook.remove_page(notebook.page_num(tab_widget))



__gsignals__ = { "close-clicked": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ()),}
gobject.threads_init()
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_icon_from_file("ico_surf.png")
window.set_title("Waterske Surfer") 
window.set_default_size(1300, 900)
window.set_resizable(True)
window.connect("delete_event", delete_event)
window.set_position(gtk.WIN_POS_CENTER)

surfer = webkit.WebView()
settings = surfer.get_settings()
settings.set_property('enable-default-context-menu', True)
settings.set_property('enable-developer-extras', True)
settings.set_property('enable-scripts', True)
settings.set_property('minimum-font-size', 10)
settings.set_property('javascript-can-open-windows-automatically', True)
settings.set_property('enforce-96-dpi', True)
settings.set_property('enable-spatial-navigation', True)
settings.set_property('enable-file-access-from-file-uris', True)
settings.set_property('enable-universal-access-from-file-uris', True)
settings.set_property('enable-site-specific-quirks', True)
settings.set_property('enable-private-browsing', True)
settings.set_property('enable-plugins', True)
settings.set_property('enable-page-cache', True)
settings.set_property('enable-dom-paste', True)


settings.set_property('enable-spell-checking', True)
settings.set_property('auto-resize-window', True)
surfer.set_settings(settings)

toolbar = gtk.Toolbar()

notify = gtk.ProgressBar()
notify.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
notify.min_horizontal_bar_height = 16

back = gtk.ToolButton(gtk.STOCK_GO_BACK)
back.show()
back.set_sensitive(False)
back.connect("clicked", go_backbutton)

forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
forward.show()
forward.set_sensitive(False)
forward.connect("clicked", go_forwardbutton)

urlbar = gtk.Entry()
urlbar.connect("activate", go_button)
urlbar.set_sensitive(True)

ref = gtk.ToolButton(gtk.STOCK_REFRESH)
ref.show()
ref.connect("clicked", go_refbutton)

stop = gtk.ToolButton(gtk.STOCK_STOP)
stop.show()
stop.connect("clicked", go_stopbutton)

addTabButton = gtk.ToolButton(gtk.STOCK_ADD)
addTabButton.connect("clicked", add_tab_cb)
#addTabButton.show()

settButton = gtk.ToolButton(gtk.STOCK_PROPERTIES)
settButton.connect("clicked", add_tab_cb)
#settButton.show()

scroller = gtk.ScrolledWindow(None, None)
scroller.add(surfer)

surfer.connect("load-progress-changed", load_progress_amount)
surfer.connect("load-started", load_started)
surfer.connect("load-finished", load_finished)

notebook = gtk.Notebook()
#window.add(notebook)

header = gtk.VBox()
header.set_size_request( 0,15)
header1= gtk.HBox()

header.pack_start(header1, False)
#header.pack_start(toolbar, False, True, 0)
header1.pack_start(back, False)
header1.pack_start(forward, False)
header1.pack_start(urlbar)
header1.pack_start(ref, False)
header1.pack_start(stop, False)
header1.pack_start(notify, False, False, 8)
#header1.pack_start(addTabButton, False)
#header1.pack_start(settButton, False)
header.add(scroller)

surfer.connect("load_committed", seturl)
surfer.connect("title-changed", title_chg)
window.add(header)

window.connect("destroy", lambda w: gtk.main_quit())
window.show_all()


gtk.main()

