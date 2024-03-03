####################################################################
#  Cube3Writer plugin for Ultimaker Cura
# 
#  This plugin enables Cura to export to the proprietary 3D Systems 
#  .cube3 print file format.
#
#  This plugin is usually bundled with Cura-CubePrinterPlugin
#  https://github.com/mirdoc/Cura-CubePrinterPlugin/
#
#  Written by mirdoc
#
#  This plugin is released under the terms of the LGPLv3 or higher.
#  The full text of the LGPLv3 License can be found here:
#  https://github.com/mirdoc/Cura-CubePrinterPlugin/blob/master/LICENSE
####################################################################

import sys
from typing import cast, List, Optional, Dict

from io import BufferedIOBase

from UM.i18n import i18nCatalog
from UM.Message import Message
from UM.Logger import Logger
from UM.Mesh.MeshWriter import MeshWriter

from UM.PluginRegistry import PluginRegistry

from cura.Utils.Threading import call_on_qt_thread
from PyQt6.QtCore import QObject

catalog = i18nCatalog("cura")


class Cube3Writer(QObject, MeshWriter):
    def __init__(self) -> None:
        super().__init__(add_to_recent_files = False)
        self._plugin_name = "Cube3Writer"
        self._file_extension = "cube3"
        self._version = "0.2.1"
        
        # Encryption key used by BlowFish cipher
        self._encryption_key = b"221BBakerMycroft"
        
        # Used to map specific values which depend on material type
        self._material_map = {
            "PLA": {
                "material_code": "87",      # PLA Black
            },
            "ABS": {
                "material_code": "137",     # ABS Black
            }
        }

        # This array is used when parsing the g-code to skip lines
        self._skip_prefixes = [";", "G90", "G92", "M82", "M227 S128 P128"]
        
    @call_on_qt_thread
    def write(self, stream: BufferedIOBase, nodes, mode=MeshWriter.OutputMode.BinaryMode) -> bool:
        try:
            # We will use the CubeproWriter plugin to generate the output we need
            cubepro_writer = PluginRegistry.getInstance().getPluginObject("CubeproWriter")
            
            if cubepro_writer is None:
                error_message = self._plugin_name + " - Could not load print file writer. You may need to reinstall CubePrinterPlugin."
                Logger.log("e", error_message)
                cubeMeshWriter.setInformation(catalog.i18nc("@error:load", error_message))
                return False

            # Pass parameters to CubeproWriter and call processOutput
            cubepro_writer.setParams({"plugin_name": self._plugin_name, "material_map": self._material_map, "encryption_key": self._encryption_key, "skip_prefixes": self._skip_prefixes})
            return cubepro_writer.processOutput(stream, nodes, mode)
            
        except Exception as e:
            Logger.logException("w", "An exception occured in " + self._plugin_name + " while trying to create ." + self._file_extension + " file.")
            Logger.log("d", sys.exc_info()[:2])
            message = Message(catalog.i18nc("@warning:status", self._plugin_name + " experienced an error trying to create ." + self._file_extension + " file"))
            message.show()
            
            return False        
        