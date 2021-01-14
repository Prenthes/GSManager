# Game Server Manager Python

This script automate game server installation, map, mod installation and launch process. You can manage mods and maps selection in the .yml file in /confs directoru. This script is developped for a school project.

## Usage

* First run pip install -r requirements.txt // to download dependencies
* modify your_game.yml // to customise your game server
* python GSManager.py install your_game.yml // for installing server, map and mod
* python arma3.py uninstall your_game.yml // to uninstall the server
* python arma3.py start your_game.yml // to start the server
* python arma3.py stop your_game.yml // to stop the server

## CHANGELOG CURRENT 0.8

*   V0.85 : Optimizing script
*   V0.8 : Implementing public ip show in start.py, system check, modify code to add your_game.yaml as a variable for further customisation, changing name of the script
*   V0.7 : Implementing custom start, stop function
*   V0.6 : Implementing mod installation, conf.cfg auto generation
*   V0.5 : Reorganising code, implementing map downloading, renaming project
*   V0.4 : Reorganising code, implementing YAML conf file, adding uninstall function
*   V0.3 : Script now install and launch the arma3server
*   V0.2 : Now working with Py-SteamCMD-Wrapper / Implementing steamCMD / making test on dir management with python / addind list of game + steam ID for further experiments
*   V0.1 : Pseudo Script writted & testing github fonction


## License

CC BY-NC //
This license lets others remix, adapt, and build upon your work non-commercially, and although their new works must also acknowledge you and be non-commercial, they don’t have to license their derivative works on the same terms.
