# 0x00-python-hello_world
![alt_text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

* The pycodestyle
* Shell Scripts
* C Scripts

#Requirements
#Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
#Shell Scripts
Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long (wc -l file should print 2)
All your files should end with a new line
The first line of all your files should be exactly #!/bin/bash
All your files must be executable
#C Scripts
Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded

#RESOURSE
[The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)

[The Python tutorial (only the first three chapters below)](https://docs.python.org/3.4/library/dis.html)

[Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)

[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)

[An Informal Introduction to Python (Read up until “3.1.2. Strings” included)](https://docs.python.org/3/tutorial/introduction.html)

[Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/)

[Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)

[Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

[The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)

[Python Programming: An Introduction to Computer Science 3rd edition](https://nibmehub.com/opac-service/pdf/read/Python%20Programming%20_%20an%20introduction%20to%20computer%20science-%203rd%20Edition.pdf)

[The Python Guru](https://thepythonguru.com/)

[New string formatting](https://pyformat.info/)

[Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)

[Python Interpreter](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

[Python bytecode](https://docs.python.org/3.4/library/dis.html)

[How to Use the wc Command in Linux](https://www.howtogeek.com/812441/wc-command-in-linux/)

[Wc Command in Linux (Count Number of Lines, Words, and Characters)](https://linuxize.com/post/linux-wc-command/)

[wc(1) — Linux manual page](https://www.man7.org/linux/man-pages/man1/wc.1.html)

[Disassembler for Python bytecode](https://docs.python.org/3.4/library/dis.html)
```bash
#TAsk one	

#Write a Shell script that runs a Python script.

#The Python file name will be saved in the environment variable $PYFILE

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 

#task 2
#Write a Shell script that runs Python code.

#The Python code will be saved in the environment variable $PYCODE

guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'

#task 6
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!

#It’ll tell you the length of the longest line in a file
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 

#how to check lenght of chracter
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py

#let of character
guillaume@ubuntu:~/py/0x00$ wc -m 9-easter_egg.py


#Write a script that compiles a Python script file.

#The Python file name will be stored in the environment variable $PYFILE

#The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$ 
```

