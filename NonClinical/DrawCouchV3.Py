#!/usr/bin/python
##
##   Written By: gbee	CancerpartnersUK Ltd
##   Modified by JL     Date: 07 July 2017
##Version History:
##V1.0 created gbee
##V2.0 JL - 07 July 2017 - Added a box with density 0 to override the CT couch parts that are outside the Linac couch

##Import Sys and Os Modules
import sys
import os
import math

##Get command Line Args
Dir = sys.argv[1]
XCoord = float(sys.argv[2])
YCoord = float(sys.argv[3])
ZStart = float(sys.argv[4])
ZWidth = float(sys.argv[5])
ZSlices = float(sys.argv[6])

##Set the Sizes
CouchW = 53.0
CouchT = 5.0
CouchB = 42.0
CouchE = 2.7
CouchET = 0.45
CouchWB = 5.5
Skin = 0.12
Density0 = 0
Density1 = 0.6
Density2 = 0.08

##calculate the CT Couch override Coordinates
ctp1x = XCoord - 1
ctp1y = YCoord 
  
ctp2x = XCoord + CouchW + 1
ctp2y = YCoord
  
ctp3x = XCoord + CouchW + 1
ctp3y = YCoord - CouchT - 0.1

ctp4x = XCoord - 1
ctp4y = YCoord - CouchT - 0.1
 
ctp5x = XCoord - 1 
ctp5y = YCoord 

##calculate the Linac Couch Coordinates
p1x = XCoord 
p1y = YCoord 
  
p2x = XCoord + CouchW
p2y = YCoord
  
p3x = XCoord + CouchW
p3y = YCoord - CouchET

p4x = XCoord + CouchW - CouchE
p4y = YCoord - CouchET
 
p5x = XCoord + CouchW - CouchWB 
p5y = YCoord - CouchT 
  
p6x = XCoord + CouchWB 
p6y = YCoord - CouchT 
  
p7x = XCoord + CouchE 
p7y = YCoord - CouchET 
  
p8x = XCoord 
p8y = YCoord - CouchET 
  
p9x = XCoord 
p9y = YCoord 

##calculate the CouchIn Coordinates
sp1x = XCoord + CouchE + Skin
sp1y = YCoord  - Skin
  
sp2x = XCoord + CouchW - CouchE - Skin
sp2y = YCoord - Skin
  
sp3x = XCoord + CouchW - CouchE - Skin
sp3y = YCoord - CouchET + Skin

sp4x = XCoord  + CouchW - CouchWB - Skin
sp4y = YCoord - CouchT + Skin
 
sp5x = XCoord  + CouchWB + Skin
sp5y = YCoord - CouchT + Skin
  
sp6x = XCoord + CouchE + Skin 
sp6y = YCoord - CouchET + Skin
  
sp7x = XCoord + CouchE + Skin
sp7y = YCoord - Skin
  

##Define a function to write out the Pinnacle Script
def WScript(wStr):
	sys.stdout.write(wStr + "\n")

##Define a function to add a curve
def WCurveCT(wctZStart):
	WScript("" )
	WScript("curve={" )
	WScript("  flags =       20;" )
	WScript("  block_size =  32;" )
	WScript("  num_points =  5;" )
	WScript("  points={" )
	WScript("    " + "%.3f " % (ctp1x) + " " + "%.3f " % (ctp1y) + " " + "%.3f " % (wctZStart))
	WScript("    " + "%.3f " % (ctp2x) + " " + "%.3f " % (ctp2y) + " " + "%.3f " % (wctZStart) )
	WScript("    " + "%.3f " % (ctp3x) + " " + "%.3f " % (ctp3y) + " " + "%.3f " % (wctZStart) )
	WScript("    " + "%.3f " % (ctp4x) + " " + "%.3f " % (ctp4y) + " " + "%.3f " % (wctZStart) )
	WScript("    " + "%.3f " % (ctp5x) + " " + "%.3f " % (ctp5y) + " " + "%.3f " % (wctZStart) )
	WScript("  };" )
	WScript("};" )

	
##Define a function to add a curve
def WCurve(wZStart):
	WScript("" )
	WScript("curve={" )
	WScript("  flags =       20;" )
	WScript("  block_size =  32;" )
	WScript("  num_points =  9;" )
	WScript("  points={" )
	WScript("    " + "%.3f " % (p1x) + " " + "%.3f " % (p1y) + " " + "%.3f " % (wZStart))
	WScript("    " + "%.3f " % (p2x) + " " + "%.3f " % (p2y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p3x) + " " + "%.3f " % (p3y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p4x) + " " + "%.3f " % (p4y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p5x) + " " + "%.3f " % (p5y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p6x) + " " + "%.3f " % (p6y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p7x) + " " + "%.3f " % (p7y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p8x) + " " + "%.3f " % (p8y) + " " + "%.3f " % (wZStart) )
	WScript("    " + "%.3f " % (p9x) + " " + "%.3f " % (p9y) + " " + "%.3f " % (wZStart) )
	WScript("  };" )
	WScript("};" )


##Define a function to add a curve
def WCurveIn(wiZStart):
	WScript("" )
	WScript("curve={" )
	WScript("  flags =       20;" )
	WScript("  block_size =  32;" )
	WScript("  num_points =  7;" )
	WScript("  points={" )
	WScript("    " + "%.3f " % (sp1x) + " " + "%.3f " % (sp1y) + " " + "%.3f " % (wiZStart))
	WScript("    " + "%.3f " % (sp2x) + " " + "%.3f " % (sp2y) + " " + "%.3f " % (wiZStart) )
	WScript("    " + "%.3f " % (sp3x) + " " + "%.3f " % (sp3y) + " " + "%.3f " % (wiZStart) )
	WScript("    " + "%.3f " % (sp4x) + " " + "%.3f " % (sp4y) + " " + "%.3f " % (wiZStart) )
	WScript("    " + "%.3f " % (sp5x) + " " + "%.3f " % (sp5y) + " " + "%.3f " % (wiZStart) )
	WScript("    " + "%.3f " % (sp6x) + " " + "%.3f " % (sp6y) + " " + "%.3f " % (wiZStart) )
	WScript("    " + "%.3f " % (sp7x) + " " + "%.3f " % (sp7y) + " " + "%.3f " % (wiZStart) )
	WScript("  };" )
	WScript("};" )
	

WScript("//Automatic Script Output by Python DrawCouchv2.py")
WScript("//modified by JL 07072017 original by gbee 22082013")
WScript("//-----------------------------------------------------" )
WScript("//  Beginning of ROI: CouchCT" )
WScript("//-----------------------------------------------------" )
WScript("" )
WScript("   roi={" )
WScript("           name: CouchCT" )
WScript("           flags =          16;" )
WScript("           color:           inverse_grey" )
WScript("           box_size =       5;" )
WScript("           line_2d_width =  1;" )
WScript("           line_3d_width =  1;" )
WScript("           paint_brush_radius =  0.4;" )
WScript("           paint_allow_curve_closing = 1;" )
WScript("           lower =          0;" )
WScript("           upper =          750;" )
WScript("           radius =         0;" )
WScript("           density =        " + "%.2f" % (Density0) + ";" )
WScript("           density_units:   g/cm^3" )
WScript("           override_data =  1;" )
WScript("           invert_density_loading =  0;" )
WScript("           volume =         0;" )
WScript("           pixel_min =      0;" )
WScript("           pixel_max =      0;" )
WScript("           pixel_mean =     0;" )
WScript("           pixel_std =      0;" )
WScript("           num_curve =      " + "%.0f" % (ZSlices) + ";" )
WScript("           bBEVDRROutline =       0;" )

WCurveCT(ZStart)
counter0 = 1
while (counter0 < ZSlices):
	Position = ZStart + (counter0 * ZWidth)
 	WCurveCT(Position)
 	counter0 = counter0 + 1
WScript("}; // End of ROI CouchCT" )	
	
		
WScript("//Automatic Script Output by Python DrawCouch.py")
WScript("//-----------------------------------------------------" )
WScript("//  Beginning of ROI: Couch" )
WScript("//-----------------------------------------------------" )
WScript("" )
WScript("   roi={" )
WScript("           name: Couch" )
WScript("           flags =          16;" )
WScript("           color:           grey" )
WScript("           box_size =       5;" )
WScript("           line_2d_width =  1;" )
WScript("           line_3d_width =  1;" )
WScript("           paint_brush_radius =  0.4;" )
WScript("           paint_allow_curve_closing = 1;" )
WScript("           lower =          0;" )
WScript("           upper =          750;" )
WScript("           radius =         0;" )
WScript("           density =        " + "%.2f" % (Density1) + ";" )
WScript("           density_units:   g/cm^3" )
WScript("           override_data =  1;" )
WScript("           invert_density_loading =  0;" )
WScript("           volume =         0;" )
WScript("           pixel_min =      0;" )
WScript("           pixel_max =      0;" )
WScript("           pixel_mean =     0;" )
WScript("           pixel_std =      0;" )
WScript("           num_curve =      " + "%.0f" % (ZSlices) + ";" )
WScript("           bBEVDRROutline =       0;" )

WCurve(ZStart)
counter = 1
while (counter < ZSlices):
	Position = ZStart + (counter * ZWidth)
 	WCurve(Position)
 	counter = counter + 1
WScript("}; // End of ROI Couch" )


WScript("//-----------------------------------------------------" )
WScript("//  Beginning of ROI: CouchIn" )
WScript("//-----------------------------------------------------" )
WScript("" )
WScript("   roi={" )
WScript("           name: CouchIn" )
WScript("           flags =          16;" )
WScript("           color:           grey" )
WScript("           box_size =       5;" )
WScript("           line_2d_width =  1;" )
WScript("           line_3d_width =  1;" )
WScript("           paint_brush_radius =  0.4;" )
WScript("           paint_allow_curve_closing = 1;" )
WScript("           lower =          0;" )
WScript("           upper =          750;" )
WScript("           radius =         0;" )
WScript("           density =        " + "%.4f" % (Density2) + ";" )
WScript("           density_units:   g/cm^3" )
WScript("           override_data =  1;" )
WScript("           invert_density_loading =  0;" )
WScript("           volume =         0;" )
WScript("           pixel_min =      0;" )
WScript("           pixel_max =      0;" )
WScript("           pixel_mean =     0;" )
WScript("           pixel_std =      0;" )
WScript("           num_curve =      " + "%.0f" % (ZSlices) + ";" )
WScript("           bBEVDRROutline =       0;" )
WCurveIn(ZStart)
counter2 = 1
while (counter2 < ZSlices):
	Position = ZStart + (counter2 * ZWidth)
 	WCurveIn(Position)
 	counter2 = counter2 + 1
WScript("}; // End of ROI CouchIn" )



