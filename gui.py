#!/usr/bin/python
from gi.repository import Gtk

class formulas:

	# def __init__(self, toolDiam, feedRate, rpm, numCutEdges, spindleRPM):
	# 	self.toolDiam = toolDiam
	# 	self.feedRate = feedRate
	# 	self.rpm = rpm
	# 	self.numCutEdges = numCutEdges
	# 	self.spindleRPM = spindleRPM

	def calcChipLoad(self, feedRate, rpm, numCutEdges):
		return feedRate/(rpm * numCutEdges)


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
		self.toolDiameter = Gtk.Entry()
		vbox_column2.pack_start(self.toolDiameter, True, True, 0)

		self.cuttingEdges = Gtk.Entry()
		vbox_column2.pack_start(self.cuttingEdges, True, True, 0)

		self.chipLoad = Gtk.Entry()
		vbox_column2.pack_start(self.chipLoad, True, True, 0)

		self.spindleRPM = Gtk.Entry()
		vbox_column2.pack_start(self.spindleRPM, True, True, 0)

		self.feedRate = Gtk.Entry()
		vbox_column2.pack_start(self.feedRate, True, True, 0)

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
		toolDiam = self.toolDiameter.get_text()
		toolDiam = float(toolDiam)
		cuttingEdges = self.cuttingEdges.get_text()
		cuttingEdges = float(cuttingEdges)
		chipLoad = self.chipLoad.get_text()
		chipLoad = float(chipLoad)
		spindleRPM = self.spindleRPM.get_text()
		spindleRPM = float(spindleRPM)
		feedRate = self.feedRate.get_text()
		feedRate = float(feedRate)

		chipLoadFunc = formulas()
		chipLoadOutput = chipLoadFunc.calcChipLoad(feedRate, spindleRPM, cuttingEdges)
		print chipLoadOutput

		
	def on_button2_clicked(self, widget):
		print("button2")

	def on_button3_clicked(self, widget):
		print("button3")
	


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()