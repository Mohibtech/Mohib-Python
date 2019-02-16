## Modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. 
* Consider a module to be the same as a code library.
* A file containing a set of functions you want to include in your application.

### platform Module
Few methods in module platform.

```python
>>> import platform
>>> print('system  :', platform.system())
>>> print('Computer :', platform.node())
>>> print('release  :', platform.release())
>>> print('version  :', platform.version())
>>> print('machine  :', platform.machine())
>>> print('processor:', platform.processor())
-----------------------------------------------
System  : Windows
Computer : MohibYoga
Release  : 10
Version  : 10.0.17134
Machine  : AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
```

### sys Module
sys module provides number of functions and variables that can be used to manipulate different parts of the Python runtime environment.  
It also allows to use stdin, stdout, stderr for standard input, output and error handling. sys.argv list contains arguments passed to python scripts. 

```python
>>> import sys
>>> sys.version
'3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]'

>>> sys.platform
'win32'

>>> sys.getdefaultencoding()
'utf-8'

>>> for i in sys.path:
        print(i)

C:\Users\Mohib\AppData\Local\Programs\Python\Python37\Lib\idlelib
C:\Users\Mohib\AppData\Local\Programs\Python\Python37\python37.zip
C:\Users\Mohib\AppData\Local\Programs\Python\Python37\DLLs
C:\Users\Mohib\AppData\Local\Programs\Python\Python37\lib
C:\Users\Mohib\AppData\Local\Programs\Python\Python37
C:\Users\Mohib\AppData\Roaming\Python\Python37\site-packages
C:\Users\Mohib\AppData\Local\Programs\Python\Python37\lib\site-packages
```

### os Module
OS module in Python provides a way of using operating system dependent
functionality. 
The functions that the OS module provides allows to interface with
underlying operating system that Python is running on – Windows, Mac or
Linux. 


```python
>>> import os
>>> os.getcwd()
'C:\\php'
```

Create new directory
```python
os.mkdir('newDir')
```

Rename an existing directory
```python
os.rename('newDir','changedDir')
```

Remove directory
```python
os.rmdir('changedDir')
```

Traversing a directory and printing all filenames including sub directories.
```python
import os
for (dirname, subshere, fileshere) in os.walk(r'C:\TECHNICAL\MS'):
    print('-----------------------------------------------------')
    print('[' + dirname + ']')
    print('-----------------------------------------------------')
    for fname in fileshere:
        print(os.path.join(dirname, fname))
```






