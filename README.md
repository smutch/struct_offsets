Struct offsets
==============

Simply print out all the members of a struct with their byte offsets.

Requirements
------------

* Python 3.x
* [Jinja2](http://jinja.pocoo.org/)
* [pyclibrary](https://github.com/MatthieuDartiailh/pyclibrary)
* A C compiler
* Make

Usage
-----

``` sh
make header=header.h struct=foobar incdirs="-I/path/to/some/3rd_party/library/include -I/and/another/include"
```
