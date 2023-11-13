# NOTE: This module is deprecated and will no longer be maintained. I do not recommend using this module as the code is very amateur, and not very efficient.

# biasedrandom

A python module for doing biased random based on the random module.

## Quickstart:

Add to python script:
```
>>> import biasedrandom
>>> br = biasedrandom.biasedrandom()
```
## Documentation
### ```brandrangenum(start: int, stop: int, biasednumbers: list, biaschance: int)```

```brandrangenum``` gives you a random between ```start``` and ```end``` but you can add ```biasednumbers``` which has a ```biaschance``` of happening instead of just a random number between ```start``` and ```end```.
 - Your ```biasednumbers``` have to be between ```start``` and ```end```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.


### ```dbrandrangemol(start: int, stop: int, biasmorethan: int, biaslessthan: int, biaschance: int)```

```dbrandrangemol``` gives you a random number between ```start``` and ```end``` but you can have it biased to a certain range ```biasmorethan``` and ```biaslessthan``` which has a ```biaschance``` of happening instead of just a random number between ```start``` and ```end```.
 - Your ```biasmorethan``` has to be more than ```start``` and less than ```end``` and less than ```biaslessthan```
 - Your ```biaslessthan``` has to be more than ```start``` and less than ```end``` and more than ```biasmorethan```
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

### ```brandintnum(start: int, stop: int, biasednumbers: list, biaschance: int)```

```brandintnum``` is basically ```brandrangenum``` but with the ```stop``` + 1.
 - Your ```biasednumbers``` have to be between ```start``` and ```end```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

### ```brandintmol(start: int, stop: int, morethan: int, lessthan: int, biaschance: int)```

```brandintmol``` is basically ```dbrandrangemol``` but with the ```stop``` + 1.
 - Your ```biasednumbers``` have to be between ```start``` and ```end```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

### ```bchoice(choices: list, biasedchoices: list, biaschance: int)```

```bchoice``` gives you a random item from a list (```choices```) but you can make it biased to ```biasedchoices```, which has a ```biaschance``` of happening instead of just a random item from ```choices```.
 - All your ```biasedchoices``` have to be in your ```choices```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

### ```bsample(sequence: list, size: int, biasedchoices: list, biaschance: int)```

```bsample``` gives you a random sample from your ```sequence```  but it has a ```biaschance``` of being for your ```biasedchoices```
 - All your ```biasedchoices``` have to be in your ```sequence```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.
 - ```size``` can't be bigger that the length of the ```biasedchoices```.

### ```brandom(biasednumbers: list, biaschance: int)```

```brandom``` gives you a random floating point number between 0 and 1 but it has a ```biaschance``` of being one of the numbers in your ```biasednumbers```
 - All your ```biasednumbers``` have to be between 0 and 1.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

### ```buniform(start: int, stop: int, biasednumbers: list, biaschance: int)```

```buniform``` gives you a randon floating point number between, and included ```start``` and ```stop``` but it has a ```biaschance``` of being one of the numbers in your ```biasednumbers```
 - All your ```biasednumbers``` have to be between ```start``` and ```stop```.
 - Your ```biaschance``` has to be less than 100 and more than or equal to 0.

