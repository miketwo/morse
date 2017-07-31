Morse Code Translator
=====================

A simple python module to translate to/from morse code.

Installation
-------------
```
pip install -e .
```

Usage
-----
```
# Translate to morse code
translate.py "text to translate"
- . -..- -|- ---|- .-. .- -. ... .-.. .- - .

# Or in reverse
translate.py -r "- . -..- -|- ---|- .-. .- -. ... .-.. .- - ."
TEXT TO TRANSLATE

# See the help for more info
translate.py -h
```

Testing
-------
```
# Install test dependences
make init

# Run pytest-watch, which will continouosly rerun tests as you develop
make test
```



License
-------

Uses the `MIT`_ license.

.. _MIT: http://opensource.org/licenses/MIT
