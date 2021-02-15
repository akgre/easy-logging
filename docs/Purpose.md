# Purpose
To create a simple method for logging in python scripts aimed at novice developers making small scripts.

## Problem 
When novice developers start making scripts they are focused on quickly making something work, however, without a plan their scripts can become unmaintainable and absorb a disproportionate amount of their time. Here are some of the common pitfall of logging that the developers fall into.

1. Only using print. Using print is quick but very easily becomes useless. There is no output file so can only be seen on the current screen so if it closes that information is lost. There is also no way of setting levels so is not able to choose between displaying information or debugging. 
2. Writing to a text file. Setting up a useful logger can be intricate and as a workaround will create a function to log some variables to a file. This will normally only contain information to solve a specific problem and minimal in guiding the dev to fixing an issue. This will also be an issue with traceability of script runs as this will not hold enough information of the script run to replicate the run.
3. Using a single log file. If a dev has created logging but log everything to one file it will either get overwritten if they don't copy it to a backup or many log files will be created in the script root and will flood the project with log files.

## Solution

1. Create 2 log files. One for reflecting exactly what the user saw in the console and a second to show the debug information. If a dev sees a problem then the can cross-reference the console to the debug.
2. Add meta data to the debug. This will add information of time and where the line of code was executed so the dev can easily look it up in the script.
3. Automatically Organise the log files. The files will be automatically stored in an associated log file with the project file name. They will also be date and time stamped for traceability.
4. Have a GUI that clearly shows the logging options and can be easily modified.
5. Able to set the logging options if the dev would like to control the logging via their script.

## Conclusion

Have a one line approach to having automatically logged scripts will help developers immensely with debugging and maintaining their scripts.

