@echo off

ipython.exe --profile azcamserver --TerminalInteractiveShell.term_title_format=azcamserver -i -m azcam_90prime.server -- -lab -system 6k
