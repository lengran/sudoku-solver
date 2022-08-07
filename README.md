# sudoku-solver

## Description

This is just a demo. I did this purely out of personal interest. So, I'm not sure if it will be fully implemented in the future.

For now, this solver still has its limit. It can only solve **some simple** sudoku problems (to be more specific, ones labled as easy). This program can only do inference on given info, it has no ability to search the solution space and find a feasible solution. Hopefully I will finally get it implemented one day.

## Dependency

The command line version has no dependency. Just go with the following command.

```bash
python3 solver-cli.py
```

The GUI version depends on **pylibui**. You can get it [here](https://github.com/joaoventura/pylibui). Then you can run it like this.

```bash
python3 solver-gui.py
```