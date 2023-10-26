# python-tools

A collection of small, useful and powerful Python scripts.

## Description

Please use it for daily tasks and small tasks.  
For detailed instructions on how to use each of these, See python script.

## Getting Started

### Dependencies

- Almost all Linux distributions
- Python 3.5+

For reference,the author uses the following environment.
- WSL2 Ubuntu 20.04.5 LTS
- Python 3.12

### Installing

* Temporary path addition
```
$ git clone https://github.com/Lamaglama39/python-tools.git
$ cd python-tools/<directory to used>
$ export PATH=$PATH:$(pwd)
```

* Adding a path to a configuration file
```
$ git clone https://github.com/Lamaglama39/python-tools.git
$ cd python-tools/<directory to used>
$ printf '# python-tools path\nexport PATH=\"$PATH:'"$(pwd)"\"'\n' >> ~/.bashrc
```

## Project Structure
```
.
├── LICENSE.md
├── README.md
├── cheatsheet     # Cheat sheet for various commands.
├── joke           # Funny joke script.
└── tools          # Common command line tools.
    ├── conversion # Tools for image format conversion, QR generation, etc.
    ├── math       # Mathematical Tools.
    └── utils      # Versatile command line tool.
```

## Author

[@Lamaglama39](https://twitter.com/lamaglama39)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
