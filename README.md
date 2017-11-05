# Cura-Dremel-3D20-Plugin
Dremel Ideabuilder 3D20 plugin for Cura 3.x.  This code is **heavily** based upon the [cura gcode writer plugin](https://github.com/Ultimaker/Cura/tree/master/plugins/GCodeWriter) and has been hacked together in an afternoon.  I'm not responsible if you use this software and bad things happen either to you or your printer.  The software is supplied without warranty.  The software or its authors will not guarantee that it won't break your 3d printer, set it on fire, or do other bad things - please use the software responsibly. Any usage of this software is strictly at your own risk.

# Installation
1. To install, simply clone the repository onto your machine, then copy the plugins/DremelGCodeWriter folder into your <cura install>/plugins folder.

![Copy the contents of DremelGCodeWriter to the plugin directory of cura](/docs/plugindir.PNG)

2.   Copy the resources/definitions/Dremel3D20.def.json file into the <cura install>/resources/definitions folder
![Copy the contents of Dremel printer json file to the definitions directory of cura](/docs/dremelresource.PNG)

3.  You should be all set

# Usage
Once the plugin has been installed you can use it by following the steps outlined below:
1. open cura 
2. select the Dremel 3D20 as your printer (cura->preferences->printers->add)
3. select PLA as your filament type, and slice the print with the options you want. 
4. Save to file, selecting .g3drem as the output file format. 

![Save as .g3drem file](/docs/saveas.PNG)

5. Save this file to a SD card
6. Insert the SD card into your IdeaBuilder 3D20
7. Turn on the printer
8. Select the appropriate file to print
9. Click print

Enjoy!

# Note
Please note the following:
* This plugin has only been tested on Cura 3.0.4 on Windows 10.
* The Dremel 3D20 printer file json has not been optimized at all - if you have time and want to improve this file please do so and contribute the changes back.
  * While this plugin works in the basic print case, you may encounter problems with the print head crashing into your parts if you attempt to print multiple parts on the same print bed one-after-another instead of printing them all-at-once.
* The .g3drem file format is not fully understood yet - I've done a bit of reverse engineering on the file format, as described here: http://forums.reprap.org/read.php?263,785652 and have used the information I discovered to create this plugin, however there are still magic numbers in the dremel header that may or may not have an effect on the print.

# Wishlist
The following items would be great to add to this software - as I get time I'll work on them
* Optimized Dremel3D20 json file with support for Dremel brand PLA
* Addition of Dremel brand PLA
* Replace the generic bitmap with a bitmap of the actual part being printed
