# EDDecompiler

This project is forked from [Ouroboros/EDDecompiler](https://github.com/Ouroboros/EDDecompiler) and [illidan2004/EDDecompiler](https://github.com/illidan2004/EDDecompiler).

It can be used to decompile/recompile script files of PSP & PC games *Zero/Ao no Kiseki* and PC game *Trails in the Sky* series(Published by Xseed). This fork adds support for the Japanese version of the PS Vita Trails in the Sky Evolution series as well as Zero no Kiseki Evolution. 

Just give the usage here:   
## 1. Install python3   
And install missing libs with this command:   
```
    pip3 install xmltodict aiohttp rsa hexdump
```

## 2. clone **EDDecompiler** and **PyLibs**   
```
    git clone https://github.com/the-database/EDDecompiler   
    git clone https://github.com/ZhenjianYang/PyLibs   
```

## 3. Decompile
### *Trails in the Sky FC Evolution*:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python .\ED6FCEvoScenarioScript.py --gp="<game data folder>" <script file or folder>
```
### *Trails in the Sky SC Evolution*:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python .\ED6SCEvoScenarioScript.py --gp="<game data folder>" <script file or folder>
```
### *Trails in the Sky the 3rd Evolution*:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python .\ED63RDEvoScenarioScript.py --gp="<game data folder>" <script file or folder>
```
### *Zero no Kiseki Evolution*:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python .\ZeroEvoScenarioScript.py --cp=<codepage> <scripts folder> 
```

The game data folder refers to the folder containing the scenario folder (data, data_sc, or data_3rd). This must be extracted from the data.psarc file. 

Decompiled scripts will have a filename like **xxxx.py** (xxxx stands for the script's name).

## 4. Recompile   
***Trails in the Sky Evolution*** series:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python <decompiled script file> --gp=<game folder> <output folder>
```
### ***Zero no Kiseki Evolution***:   
```
    set PYTHONPATH=EDDecompiler/Decompiler;PyLibs
    python <decompiled script file> --cp=<codepage> <output folder>
```
