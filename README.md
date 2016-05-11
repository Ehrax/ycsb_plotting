# YCSB - Plotting - Tool

## Requirements
- Python
- Argparse
- Matplotlib

## Getting Started

### Install
Just download the [latest version](https://github.com/Ehrax/ycsb_plotting.git)
```
git clone https://github.com/Ehrax/ycsb_plotting.git
cd ycsb_plotting
```

### Using YCSB - Plotting Tool
```
./plot.py [-h] [--o] [--r 'prefix'] path [path ...]
```

| Prefix | Usage |
| ------ | ----- |
| -h     | help  |
| path   | path to files or directory if you use --r |
| --r 'prefix'  | use this if you want to input several files |
| --o    | use this if you want only one output file |

#### Examples
```
./plot.py example.dat secondfile.dat
./plot.py --o example.dat secondfile.dat file.dat
./plot.py --r mongo ~/example/direcotry
./plot.py --o --r mongo ~/example/direcotry
```
