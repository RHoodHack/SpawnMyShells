[![GitHub license](https://img.shields.io/github/license/internetwache/GitTools.svg)](https://github.com/internetwache/GitTools/blob/master/LICENSE.md)
 

# SpawnMyShells

This script will facilitate the generation of all your reverse shells

### INSTALL

    git clone https://github.com/RHoodHack/SpawnMyShells.git
    cd SpawnMyShells
    chmod +x SpawnMyShells.py

### Usage


```
$ ./SpawnMyShells.py -h

usage: SpawnMyShells.py [-h] (-i IP | -I INTERFACE) -p PORT [-L] [-W] [--b64] [-t TOOL] [-q]

Fast reverse Shell Generator

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Ip to connect
  -I INTERFACE, --interface INTERFACE
                        select ip of interface to connect
  -p PORT, --port PORT  select port to connect
  -L                    generate Windows Payload
  -W                    generate Linux Payload
  --b64                 generate base64 encoded Windows payload
  -t TOOL, --tool TOOL  specify a tool
  -q, --quiet           don't display logo and useful commands
```

## Demo

Here's a small demo of **SpawnMyShells** :

![Demo](https://github.com/RHoodHack/SpawnMyShells/raw/master/ressources/image1.png)


## Requirements
* Python 3+

# License

All tools are licensed using the MIT license. See [LICENSE.md](LICENSE.md)

# References

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

https://www.asafety.fr/reverse-shell-one-liner-cheat-sheet/