# biasedrandom
A python module for doing biased random based on the random module.

## Quickstart:
Installation with pip:
```
$ pip install biasedrandom
```
Add to python script:
```
>>> import biasedrandom
>>> br = biasedrandom.biasedrandom()
```
## Documentation - incomplete
```biasedrandom.brandrangenum(start: int, stop: int, biasednumbers: list, biaschance: int)``` -

```brandrangenum``` gives you a random between ```start``` and ```end``` but you can add ```biasednumbers``` which has a ```biaschance``` of happening instead of just a random number between ```start``` and ```end```.
 - Your ```biasednumbers``` have to be between ```start``` and ```end```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.
