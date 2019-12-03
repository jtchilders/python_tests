A test to see if setting an environment variable using `os.environ` in python can be seen by a compiled c-library.

build the library using `build.sh`

then run `python test.py`

I found on Theta, with gcc 4.8.5 and python 3.7 that the output was:
`TEST :Hello` 

so the set environment variable was picked up by the compiled c-library
