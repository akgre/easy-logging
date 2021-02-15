# setup-logging
Easy setup for a simple management free logger which can be added to any project. Includes a GUI

Two loggers are set up for the project, one to record console information to a file and another to file that allows for in depth debugging. 

Quite console can be use if they user wants to use the project as a background task or to only show information in a GUI but would still like to record logs.

The first time you call the setup it will open up a GUI which will allow you to configure your logging.

![setup_gui](C:\Users\Zircon\Desktop\python_projects\setup-logging\docs\img\setup_gui.PNG)

## Usage
In your project add:
```Python
from loguru import logger
from setup_logging import setup_logging
```
At the beginning of your program call the setup
```Python
setup_logging(project_name='project')
```
Then replace your print statements with either ```logger.info()``` or ```logger.debug()```

For sub-modules, if you add ```from loguru import logger``` and use the logger the formatting will be the same for the whole program.

## Requirements

* `Louguru` [Loguru Github](https://github.com/Delgan/loguru)
* `pysimplegui` [PySimpleGUI Github](https://github.com/PySimpleGUI/PySimpleGUI)
* `toml` [TOML Github](https://github.com/toml-lang/toml)