# azcamserver config file for 90prime

import os
import sys

import azcam
import azcam.server
import azcam.shortcuts
from azcam.tools.cmdserver import CommandServer
from azcam.tools.system import System

from azcam_arc.controller_arc import ControllerArc
from azcam_arc.exposure_arc import ExposureArc

from azcam_archon.controller_archon import ControllerArchon
from azcam_archon.exposure_archon import ExposureArchon
from azcam_archon.tempcon_archon import TempConArchon

from azcam_cryocon.tempcon_cryocon24 import TempConCryoCon24
from azcam_ds9.ds9display import Ds9Display
from azcam_imageserver.sendimage import SendImage
from azcam_focus.focus import Focus
from azcam_fastapi.fastapi_server import WebServer

# from azcam_webtools.status.status import Status

from azcam_90prime.telescope_bok import BokTCS

from azcam_90prime.instrument_pf import PrimeFocusInstrument
from azcam_90prime.instrument_pf_ngserver import PrimeFocusInstrumentUpgrade

# ****************************************************************
# parse command line arguments
# ****************************************************************
try:
    i = sys.argv.index("-system")
    option = sys.argv[i + 1]
except ValueError:
    option = "menu"
try:
    i = sys.argv.index("-datafolder")
    datafolder = sys.argv[i + 1]
except ValueError:
    datafolder = None
try:
    i = sys.argv.index("-lab")
    lab = 1
except ValueError:
    lab = 0

# ****************************************************************
# define folders for system
# ****************************************************************
azcam.db.systemname = "90prime"

azcam.db.rootfolder = os.path.abspath(os.path.dirname(__file__))
azcam.db.rootfolder = os.path.normpath(azcam.db.rootfolder).replace("\\", "/")

azcam.db.systemfolder = os.path.dirname(__file__)
azcam.db.systemfolder = azcam.utils.fix_path(azcam.db.systemfolder)

if datafolder is None:
    droot = os.environ.get("AZCAM_DATAROOT")
    if droot is None:
        droot = "/data"
    azcam.db.datafolder = os.path.join(droot, azcam.db.systemname)
else:
    azcam.db.datafolder = datafolder
azcam.db.datafolder = azcam.utils.fix_path(azcam.db.datafolder)

# ****************************************************************
# configuration menu
# ****************************************************************
print("90Prime Startup Menu\n")
menu_options = {
    "90prime (standard mode)": "normal",
    "90primeOne": "90primeone",
    "90prime with overscan rows": "overscan",
    "90prime FAST mode (with overscan rows)": "fast",
    "CSS mode": "css",
    "6k mode": "6k",
}
if option == "menu":
    option = azcam.utils.show_menu(menu_options)

CSS = 0
ARCHON = 0
if "90primeone" in option:
    parfile = os.path.join(azcam.db.datafolder, "parameters", "parameters_server_90prime_one.ini")
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90primeone_master.txt")
    timingfile = os.path.join(
        azcam.db.datafolder,
        "dspcode",
        "dspcode_90prime",
        "dsptiming_90primeone",
        "90PrimeOne_config0.lod",
    )
    azcam.db.servermode = "90primeone"
    cmdport = 2432
elif "normal" in option:
    parfile = os.path.join(
        azcam.db.datafolder, "parameters", "parameters_server_90prime_normal.ini"
    )
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90prime_master.txt")
    timingfile = os.path.join(
        azcam.db.datafolder,
        "dspcode",
        "dspcode_90prime",
        "dsptiming_90prime",
        "90Prime_config0.lod",
    )
    azcam.db.servermode = "normal"
    cmdport = 2402
elif "fast" in option:
    parfile = os.path.join(azcam.db.datafolder, "parameters", "parameters_server_90prime_fast.ini")
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90prime_master.txt")
    timingfile = os.path.join(
        azcam.db.datafolder,
        "dspcode",
        "dspcode_90prime",
        "dspcode_90prime",
        "dsptiming_fast",
        "90Prime_config1.lod",
    )
    azcam.db.servermode = "fast"
    cmdport = 2402
elif "overscan" in option:
    parfile = os.path.join(
        azcam.db.datafolder, "parameters", "parameters_server_90prime_overscan.ini"
    )
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90prime_master.txt")
    timingfile = os.path.join(
        azcam.db.datafolder,
        "dspcode",
        "dspcode_90prime",
        "dsptiming_90prime",
        "90Prime_config0.lod",
    )
    azcam.db.servermode = "overscan"
    cmdport = 2402
elif "css" in option:
    CSS = 1
    parfile = os.path.join(azcam.db.datafolder, "parameters", "parameters_server_90prime_css.ini")
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90prime_css.txt")
    timingfile = os.path.join(
        azcam.db.systemfolder,
        "dspcode",
        "dspcode_90prime",
        "dsptiming_90prime",
        "90Prime_config0.lod",
    )
    azcam.db.servermode = "CSS"
    cmdport = 2422
elif "6k" in option:
    print("90Prime for 6k CCD")
    ARCHON = 1
    parfile = os.path.join(azcam.db.datafolder, "parameters", "parameters_server_90prime_6k.ini")
    template = os.path.join(azcam.db.datafolder, "templates", "fits_template_90prime_6k.txt")
    timingfile = os.path.join(
        azcam.db.datafolder,
        "dspcode",
        "archon_6k",
        "90prime6k.acf",
    )
    azcam.db.servermode = "6k"
    cmdport = 2442
else:
    raise azcam.AzcamError("bad server configuration")
parfile = parfile

# ****************************************************************
# logging
# ****************************************************************
logfile = os.path.join(azcam.db.datafolder, "logs", "server.log")
azcam.db.logger.start_logging(logfile=logfile)
azcam.log("Configuring for 90prime")

# ****************************************************************
# controller
# ****************************************************************
if ARCHON:
    controller = ControllerArchon()
    controller.timing_file = timingfile
    controller.camserver.port = 4242
    controller.camserver.host = "10.0.0.2"
else:
    controller = ControllerArc()
    controller.timing_board = "arc22"
    controller.clock_boards = ["arc32"]
    controller.video_boards = ["arc47", "arc47", "arc47", "arc47"]
    controller.set_boards()
    controller.video_gain = 1
    controller.video_speed = 1
    controller.camserver.set_server("localhost", 2405)
    controller.pci_file = os.path.join(
        azcam.db.systemfolder, "dspcode", "dspcode_90prime", "dsppci", "pci3.lod"
    )
    controller.timing_file = timingfile

# ****************************************************************
# temperature controller
# ****************************************************************
if ARCHON:
    tempcon = TempConArchon(description="90prime Archon")
else:
    tempcon = TempConCryoCon24(description="90prime CryoCon")
    tempcon.control_temperature = -135.0
    # tempcon.host = "10.0.0.45"
    tempcon.host = "10.30.3.32"
    tempcon.init_commands = [
        "input A:units C",
        "input B:units C",
        "input C:units C",
        "input A:isenix 2",
        "input B:isenix 2",
        "loop 1:type pid",
        "loop 1:range mid",
        "loop 1:maxpwr 100",
    ]

# ****************************************************************
# exposure
# ****************************************************************
if ARCHON:
    exposure = ExposureArchon()
    exposure.filetype = exposure.filetypes["MEF"]
    exposure.image.filetype = exposure.filetypes["MEF"]
    # exposure.update_headers_in_background = 1
    exposure.display_image = 0
    sendimage = SendImage()
else:
    exposure = ExposureArc()
    exposure.filetype = exposure.filetypes["MEF"]
    exposure.image.filetype = exposure.filetypes["MEF"]
    exposure.update_headers_in_background = 1
    exposure.display_image = 0
    sendimage = SendImage()
if not lab:
    exposure.send_image = 1
    sendimage.set_remote_imageserver("10.30.1.2", 6543, "dataserver")

# ****************************************************************
# instrument
# ****************************************************************
instrument = PrimeFocusInstrument()
# instrument = PrimeFocusInstrumentUpgrade()

# ****************************************************************
# telescope
# ****************************************************************
telescope = BokTCS()

# ****************************************************************
# focus
# ****************************************************************
focus = Focus()
focus.focus_component = "instrument"
focus.focus_type = "step"
focus.initialize()

# ****************************************************************
# system header template
# ****************************************************************
system = System("90prime", template)
system.set_keyword("DEWAR", "90prime", "Dewar name")

# ****************************************************************
# detector
# ****************************************************************
if "90primeone" in option:
    from azcam_90prime.detector_bok90prime import detector_bok90prime_one

    exposure.set_detpars(detector_bok90prime_one)
elif "6k" in option:
    from azcam_90prime.detector_bok90prime import detector_bok90prime_6k

    exposure.set_detpars(detector_bok90prime_6k)
    exposure.fileconverter.set_detector_config(detector_bok90prime_6k)

else:
    from azcam_90prime.detector_bok90prime import detector_bok90prime

    if "overscan" in option:
        detector_bok90prime["format"] = [4032 * 2, 6, 0, 20, 4096 * 2, 0, 0, 20, 0]
    exposure.set_detpars(detector_bok90prime)

# ****************************************************************
# display
# ****************************************************************
display = Ds9Display()

# ****************************************************************
# system-specific
# ****************************************************************
if CSS:
    from azcam_90prime.css import CSS

    css = CSS()
    azcam.db.tools["css"] = css
    sendimage.set_remote_imageserver("10.30.6.2", 6543, "azcam")
    exposure.folder = "/home/css"

# ****************************************************************
# parameter file
# ****************************************************************
azcam.db.tools["parameters"].read_parfile(parfile)
azcam.db.tools["parameters"].update_pars(0, "azcamserver")

# ****************************************************************
# command server
# ****************************************************************
cmdserver = CommandServer()
cmdserver.port = cmdport
azcam.log(f"Starting cmdserver - listening on port {cmdserver.port}")
# cmdserver.welcome_message = "Welcome - azcam-itl server"
cmdserver.start()

# ****************************************************************
# web server
# ****************************************************************
if 0:
    webserver = WebServer()
    webserver.logcommands = 0
    webserver.index = os.path.join(azcam.db.systemfolder, "index_bok.html")
    webserver.port = 2403  # common port for all configurations
    webserver.start()
    webstatus = Status()
    webstatus.initialize()

# ****************************************************************
# camera server
# ****************************************************************
if ARCHON:
    pass
else:
    import azcam_90prime.restart_cameraserver

# ****************************************************************
# GUIs
# ****************************************************************
if 1:
    import azcam_90prime.start_azcamtool

# ****************************************************************
# finish
# ****************************************************************
azcam.log("Configuration complete")
