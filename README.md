# __lxivChing__
## _the minified, terminal-friendldy I Ching algorithm_
---

### What is this I Ching thing?
* (Quick reference)[https://en.wikipedia.org/wiki/I_Ching]
* Sources for an in-depth reference:
  * (Biroco)[https://www.biroco.com/yijing/index.htm]
  * (The Gnostic Book Of Changes)[https://www.jamesdekorne.com/GBCh/GBCh.htm]


### Usage:
1. make sure (Python 3.10+)[https://www.python.org/] is installed
2. change directory into the package path: `cd /path/to/lxivChing`
3. run `python3 lxiv-ching {optional_flags}{query}` where:
   * _{query}_ - optional question/query input
   * _{optional flags}_:
      * --nh - dont write to history .txt file

### __demo:__
```
$ python3.10 lxivChing "test query" 
Query: test query
  2022-06-15T11:56:
  19->29
  Lines_to_read: 1, 5
Commentary: original hexagram's changing lines apply. the uppermost line of the two is most important
```


