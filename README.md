# Usage

```
python ./LEGv8.py input
```

Make sure the ```src``` folder is in the same directory as ```LEGv8.py```

You can pass ```-udec``` ```-hex``` or ```-bin``` as an argument to the program to change register output to that format

This parser is not case sensitive, so feel free to give your shift key a rest when writing your assembly

# Debugging

Run the program with the ```-d``` flag to run in debug mode

```
python ./LEGv8.py input -d
```

You can place breakpoints by adding an '@' to the end of a non-blank line

```
ADDI X0, XZR, #1
ADDI X1, XZR, #2    @   //Execution will stop at this line
ADD X2, X0, X1
```

Valid commands when debugging are:

- ```continue``` / ```c``` : Continues execution of the program 
- ```next``` / ```n``` : Executes until the next instruction
- ```list x``` / ```l x``` : Shows x lines above and below the current instruction
- ```mode x``` / ```m x``` : Changes the output mode to x (x can  be ```dec```, ```udec```, ```hex```, or ```bin```)
- ```help``` / ```h``` : Displays these commands (In case you forget)
