# TIGr

Interpreter Tiny Interpreted Graphics language package (TIGr)

The structure of this project is similar to a typical Python package. Please refer to this [guide](https://docs.python-guide.org/writing/structure/) for more information.

```
.
├── README.md
├── requirements.txt (dependencies)
├── run.py (program executable for now)
└── tigr (module)
    ├── __init__.py (shell logics that call everything else)
    ├── tests (files for testings, scripts, config files)
    ├── lib (libraries)
    │   ├── drawer
    │   │   ├── __init__.py
    │   │   └── turtle_drawer.py
    │   ├── __init__.py
    │   ├── interface.py (pre-defined class behavior for drawers, parsers and source readers)
    │   ├── parser
    │   │   ├── __init__.py
    │   │   ├── peg_parser.py
    │   │   └── regex_parser.py
    │   └── source_reader
    │       ├── file_source_reader.py
    │       └── __init__.py
    └── __main__.py (not used for now)
```


## Install Dependencies
```
pip install -r requirements.txt
```

## Usage
```
python run.py <infile> <output> --arg1 foo --arg2 bar
```

## High-Level Execution Flow

run.py -> tigr/\_\_init\_\_.py -> tigr/lib/\<some source reader\> -> tigr/lib/\<some parser\> -> tigr/lib/drawer/\<some drawer\>

## Contributing

### Git collaboration
develop new features on a separate branch whose name reflects the intended feature. For example, a tkinter drawer feature will have a name tkinter_drawer.
```
# show current branch
git branch
# switch to master if needed
git checkout master
# update from github if needed (aggressive)
git pull
# create branch and switch to it
git checkout -b tkinter_drawer
# commit the changes
git add somefiles
git commit -m "commit message"
# publish it to github
git push origin <branch_name>
# and notify the change in telegram
# the owner will handle it in master branch
``` 

### drawer, parser, or source reader
When implementing a drawer, parser, or source reader, always derive from the corresponding abstract class as follows.
```
from tigr.lib.interface import Abstract<FooBar>

class FooBar(AbstractFooBar):
	def func_1():
		pass

	def func_2():
		pass
	#
	# Write implementations for all the functions in the class
	#

	def func_n():
		pass
```

### config reader
put the code in tigr/somefilename.py