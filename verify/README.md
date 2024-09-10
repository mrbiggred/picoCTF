# Verify

The zip file contains a script that runs the decryption on a file.  The trick is to find the file that has the flag.

My solution was to use the command below:

```bash
find files/ -type f -print | xargs L1 decrypt.sh 
```

The find command will output something like:

```
files/Nel9Qkh9
files/J2taODo4
files/10tptfxh
files/IvHedMU7
files/5b3OmDaM
files/cLQTUGHU
files/fmPAeitt
...
```

`xargs L1` will take the first line from the `find` output and use it as an agrument for the `decrypt.sh` script.

I didn't do this but you could also pipe `|` the output through `grep` so you don't need to scroll through all the results.