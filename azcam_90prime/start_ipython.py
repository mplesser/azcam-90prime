"""
Starts azcam_itl in new windows.

Runs azamserver or azcamconsole in Ipython under Windows or Linux.

Usage example:
>> python -m azcam_itl.start_ipython -server -system DESI
"""

import os
import sys

CONSOLE = False
SERVER = True

args = sys.argv[1:]

if "-console" in args:
    CONSOLE = True
    SERVER = False
if "-server" in args:
    CONSOLE = False
    SERVER = True

if os.name == "posix":
    AZCAM_DATAROOT = f'{os.path.abspath("data")}'
    os.environ["AZCAM_DATAROOT"] = AZCAM_DATAROOT
    print(f"AzCam data root is {AZCAM_DATAROOT}")

    if SERVER:
        command = f"ipython --profile azcamserver -i -c \"import azcam_itl.server ; from azcam.cli import *\" -- {' '.join(args)}"
    elif CONSOLE:
        command = f"ipython --profile azcamconsole -i -c \"import azcam_itl.console ; from azcam.cli import *\" -- {' '.join(args)}"
    os.system(command)

else:
    if SERVER:
        config_file = os.path.join(os.path.dirname(__file__), "ipython_config.py")
        cmds = [
            # f"ipython --profile azcamserver -i -c",
            f"ipython --profile azcamserver --config={config_file} -i -c",
            '"import azcam_itl.server ; from azcam.cli import *"',
            f" -- {' '.join(args)}",
        ]
    if CONSOLE:
        cmds = [
            "ipython --profile azcamconsole -i -c",
            '"import azcam_itl.start"',
            f" -- {' '.join(args)}",
        ]

    command = " ".join(cmds)
    print(command)
    input()
    os.system(command)

"""
    if "-console" in args:
        tabColor = "#000099"
        tabTitle = "azcamconsole"
    elif "-server" in args:
        tabColor = "#990000"
        tabTitle = "azcamserver"
    else:
        # assume console mode
        tabColor = "#000099"
        tabTitle = "azcamconsole"

        if use_venv: 
            cmds = [
                f"wt -w azcam --suppressApplicationTitle=True --title {tabTitle} --tabColor {tabColor}",
                "cmd /k",
                f'"{activator} & python -m {startmod}"',
                f"{' '.join(args)}",
            ]
        else:
            cmds = [
                f"wt -w azcam --suppressApplicationTitle=True --title {tabTitle} --tabColor {tabColor}",
                "cmd /k",
                f"python -m {startmod}",
                f"{' '.join(args)}",
            ]

"""
