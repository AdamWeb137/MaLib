# MaLib
This project is a list of math  functions and tools that can be used in a Tkinter UI interface.


malib.py is the main script while all other scripts are scripts for functions such as a quadratic standard form converter.

If you add a function,

1. Add it into the funclist list
2. Add it into any lists in the funcdic that it applies to. You can add another catagory
3 In the funcfunc function (great name right?) and an elif statement
```python
elif func == '<the function name you put in funclist and funcdic here>':
      #Rest of code you want
```
Any UI elements in the function should fit under the FuncUI frame
