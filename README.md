# PerfectNumbers
Find perfect numbers
## Download repository
The easiest way to download this repository is to run `git clone https://github.com/LiteApplication/perfectNumbers.git` in a terminal
## Programs
This repository contains one program written in two differents languages : 
 - Python
 - C
### Python (any version)
Python program can be found on [src/Python](./src/Python).  
You need [psutil](https://pypi.org/project/psutil/) OR [python-pip](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) to run this program properly.  
To run the program, ensure that you are in src/Python (on your computer) and run `python main.py`(Default Python version), `python2 main.py`(Python2) or `python3 main.py`(Python3).  
Now, the program must ask you for the minimal value to research and the maximal. You can pass these two values as arguments. 
### C
C program can be found on [src/C](./src/C).
This program does not require any dependancy to work. 
#### Compile
First, you need a compiler depening or your operating system :
 - GCC for Linux
 - [GCC](https://github.com/not-kennethreitz/osx-gcc-installer) for OSX
 - [MingW](http://mingw-w64.org/doku.php) for Windows
 
To compile the program, ensure that you are in src/C (on your computer) and run `gcc main.c -o main` on Linux/OSX or search how to compile C programs on Windows.
#### Run
Once you have compile `main.c`, you can run it with `./main`
If you don't want to compile, you can choose a precompiled version in [/compiled](./compiled) and run it with cmd, PowerShell, Bash or watever you want. 
If you don't know which version use, select 32bits version and if you don't know your operating system, use osx if you have an iMac or windows else.

### Downloads
 - Precomiled for Windows 64bits [here](https://github.com/LiteApplication/perfectNumbers/raw/master/compiled/main-windows64.exe)
 - Precomiled for Windows 32bits [here](https://github.com/LiteApplication/perfectNumbers/raw/master/compiled/main-windows32.exe)
 - Precomiled for Linux / Mac OSX 64bits [here](https://github.com/LiteApplication/perfectNumbers/raw/master/compiled/main-linux-osx-64)
 - Precomiled for Linux / Mac OSX 32bits [here](https://github.com/LiteApplication/perfectNumbers/raw/master/compiled/main-linux-osx-32)

## License
License file is available at [/license](./LICENSE)

Repository by [LiteApplication](https://github.com/LiteApplication)
