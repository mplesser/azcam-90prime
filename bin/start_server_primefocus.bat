@echo off

ipython.exe --profile azcamserver --TerminalInteractiveShell.term_title_format=azcamserver -i -m azcam_bok.primefocus.server -- -system normal
