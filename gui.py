#!/usr/bin/python
from gi.repository import Gtk

class Formulas:

	def calcChipLoad(self, feedRate, rpm, numCutEdges):
			return feedRate/(rpm * numCutEdges)

	def calcRPM(self, feedRate, numCutEdges, chipLoad):
		return feedRate/(numCutEdges * chipLoad)

	def calcFeedRate(self, rpm, numCutEdges, chipLoad):
		return rpm * numCutEdges * chipLoad


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

		#create first column labels
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
		adjustmentTool = Gtk.Adjustment(0.0, 0.0, 100000.0, .1, 10, 0)
		self.toolDiameter = Gtk.SpinButton()
		self.toolDiameter.set_adjustment(adjustmentTool)
		self.toolDiameter.set_digits(4)
		self.toolDiameter.set_numeric(True)
		vbox_column2.pack_start(self.toolDiameter, True, True, 0)

		adjustmentCuttingEdges = Gtk.Adjustment(0.0, 0.0, 1000000.0, .1, 10, 0)
		self.cuttingEdges = Gtk.SpinButton()
		self.cuttingEdges.set_numeric(True)
		self.cuttingEdges.set_adjustment(adjustmentCuttingEdges)
		self.cuttingEdges.set_digits(4)
		vbox_column2.pack_start(self.cuttingEdges, True, True, 0)

		adjustmentChipLoad = Gtk.Adjustment(0.0, 0.0, 1000000.0, .1, 10, 0)
		self.chipLoad = Gtk.SpinButton()
		self.chipLoad.set_numeric(True)
		self.chipLoad.set_adjustment(adjustmentChipLoad)
		self.chipLoad.set_digits(4)
		vbox_column2.pack_start(self.chipLoad, True, True, 0)

		adjustmentSpindleRPM = Gtk.Adjustment(0.0, 0.0, 1000000.0, .1, 10, 0)
		self.spindleRPM = Gtk.SpinButton()
		self.spindleRPM.set_numeric(True)
		self.spindleRPM.set_adjustment(adjustmentSpindleRPM)
		self.spindleRPM.set_digits(4)
		vbox_column2.pack_start(self.spindleRPM, True, True, 0)

		adjustmentFeedRate = Gtk.Adjustment(0.0, 0.0, 1000000.0, .1, 10, 0)
		self.feedRate = Gtk.SpinButton()
		self.feedRate.set_numeric(True)
		self.feedRate.set_adjustment(adjustmentFeedRate)
		self.feedRate.set_digits(4)
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

		#output boxes
		self.outChipLoad = Gtk.Entry()
		vbox_column4.pack_start(self.outChipLoad, True, True, 0)

		self.outRPM = Gtk.Entry()
		vbox_column4.pack_start(self.outRPM, True, True, 0)

		self.outFeedRate = Gtk.Entry()
		vbox_column4.pack_start(self.outFeedRate, True, True, 0)
		
		#draw everything to the window			
		self.add(hbox)


	def on_button1_clicked(self, widget):
		toolDiam = self.toolDiameter.get_value()
		cuttingEdges = self.cuttingEdges.get_value()
		chipLoad = self.chipLoad.get_value()
		spindleRPM = self.spindleRPM.get_value()
		feedRate = self.feedRate.get_value()

		#calculate chip load
		chipLoadFunc = Formulas()
		if spindleRPM == 0 or chipLoad == 0:
			dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, "Illegal Operand:")
			dialog.format_secondary_text("Spindle RPM and Cutting Edges must be greater than zero!")
			dialog.run()
			dialog.destroy()
		else:
			chipLoadOutput = chipLoadFunc.calcChipLoad(feedRate, spindleRPM, cuttingEdges)
			chipLoadOutput = str(chipLoadOutput)
			self.outChipLoad.set_text(chipLoadOutput)

		
	def on_button2_clicked(self, widget):
		toolDiam = self.toolDiameter.get_value()
		cuttingEdges = self.cuttingEdges.get_value()
		chipLoad = self.chipLoad.get_value()
		spindleRPM = self.spindleRPM.get_value()
		feedRate = self.feedRate.get_value()
		
		#calculate RPM
		rpmFunc = Formulas()
		if cuttingEdges == 0 or chipLoad == 0:
			dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, "Illegal Operand:")
			dialog.format_secondary_text("Chip Load and Cutting Edges must be greater than zero!")
			dialog.run()
			dialog.destroy()
		else:
			rpmOutput = rpmFunc.calcRPM(feedRate, cuttingEdges, chipLoad)
			rpmOutput = str(rpmOutput)
			self.outRPM.set_text(rpmOutput)

	def on_button3_clicked(self, widget):
		toolDiam = self.toolDiameter.get_value()
		cuttingEdges = self.cuttingEdges.get_value()
		chipLoad = self.chipLoad.get_value()
		spindleRPM = self.spindleRPM.get_value()
		feedRate = self.feedRate.get_value()
		
		feedRateFunc = Formulas()
		feedRateOutput = feedRateFunc.calcFeedRate(spindleRPM, cuttingEdges, chipLoad)
		feedRateOutput = str(feedRateOutput)
		self.outFeedRate.set_text(feedRateOutput)


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()