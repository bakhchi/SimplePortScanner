# Zachary Bakhchi ECE-303 Programming Assignment 1
# - 
# Simple Port Scanner

This is a simple port scanner written in Python that runs on the command line. It utilizes the following libraries:
- `socket` (Port scanning capabilities)
- `argparse` (Allows for the addition of arguments to the program)
- `threading` (Greatly increases the speed of the program)

The program is capable of:
- Scanning the ports of external and internal networks
- Using an input file for multiple calls with different arguments
- Outputting results to another file
- Determining what process is running on a specific port

Included in this repository are the program itself and this README file.

## Usage

The program can be run using the following command:

```sh
py portscanner.py
```

(Can be `py`, `python`, or `python3` depending on the system)

As mentioned before, the program is capable of optional arguments. Running `py portscanner.py --help` displays the following:

```sh
-h, --help            show this help message and exit
--ports PORTS [PORTS ...]
            Scan the listed ports (1 2 3 ...). Scans 1-1024 by default
--ip IP               Scan a target host. localhost by default.
--input INPUT         Read a list of ports from a file
--output OUTPUT       Write the results to a file
```

## Libraries

Each library (`socket`, `argparse`, and `threading`) comes with Python installations by default. Their documentation can be found below:
- [Socket library documentation](https://docs.python.org/3/library/socket.html)
- [Threading library documentation](http://docs.python.org/3/library/threading.html)
- [Argparse library documentation](https://docs.python.org/3/library/argparse.html)

## Testing

To test the accuracy of the program, another website was used. This website also provided a basic list of ports and their default processes, which was implemented in this program:
- [Port Scanner](https://dnschecker.org/port-scanner.php)
