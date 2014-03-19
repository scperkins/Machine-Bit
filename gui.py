#!/usr/bin/python
from gi.repository import Gtk

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title='Machine Bit')
		self.set_size_request(500,400)
		
		hbox = Gtk.Box(spacing = 10)
		hbox.set_homogeneous(False)
		vbox_column1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		vbox_column1.set_homogeneous(False)
		vbox_column2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		vbox_column2.set_homogeneous(False)
		vbox_column3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		vbox_column3.set_homogeneous(False)
		vbox_column4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		vbox_column4.set_homogeneous(False)

		hbox.pack_start(vbox_column1, True, True, 0)
		hbox.pack_start(vbox_column2, True, True, 0)
		hbox.pack_start(vbox_column3, True, True, 0)
		hbox.pack_start(vbox_column4, True, True, 0)

		#first column labels
		labelToolDiameter = Gtk.Label("Tool Diameter")
		vbox_column1.pack_start(labelToolDiameter, True, True, 0)

		labelCuttingEdges = Gtk.Label("Number of Cutting Edges")
		vbox_column1.pack_start(labelCuttingEdges, True, True, 0)

		desChipLoad = Gtk.Label("Desired Chip Load")
		vbox_column1.pack_start(desChipLoad, True, True, 0)

		labelSpindleRPM = Gtk.Label("Spindle RPM")
		vbox_column1.pack_start(labelSpindleRPM, True, True, 0)

		labelFeedRate = Gtk.Label("Feed Rate (RPM)")
		vbox_column1.pack_start(labelFeedRate, True, True, 0)

		#second column input fields
		toolDiamter = Gtk.Entry()
		vbox_column2.pack_start(toolDiamter, True, True, 0)

		cuttingEdges = Gtk.Entry()
		vbox_column2.pack_start(cuttingEdges, True, True, 0)

		chipLoad = Gtk.Entry()
		vbox_column2.pack_start(chipLoad, True, True, 0)

		spindleRPM = Gtk.Entry()
		vbox_column2.pack_start(spindleRPM, True, True, 0)

		feedRate = Gtk.Entry()
		vbox_column2.pack_start(feedRate, True, True, 0)

		#buttons
		self.button1 = Gtk.Button(label = "Calculate Chip Load")
		self.button1.connect("clicked", self.on_button1_clicked)
		vbox_column3.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button(label = "Calculate RPM")
		self.button2.connect("clicked", self.on_button2_clicked)
		vbox_column3.pack_start(self.button2, True, True, 0)

		self.button3 = Gtk.Button(label = "Calculate Feed Rate")
		self.button3.connect("clicked", self.on_button3_clicked)
		vbox_column3.pack_start(self.button3, True, True, 0)
					
		self.add(hbox)

	def on_button1_clicked(self, widget):
		print("test")

	def on_button2_clicked(self, widget):
		print("button2")

	def on_button3_clicked(self, widget):
		print("button3")
	


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()