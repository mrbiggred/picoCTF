# Format String 2

After I failed at solving [Format String 3](../format_string_3/README.md) I figured I would try 2 and see if it helps with 3.

It did kind-of help.  Took me over [two hours](https://youtu.be/3dNMOff-Gp0) to solve the problem but I got it done.  Had some help with [pwntools](https://docs.pwntools.com/).

The short version is to first figure out where the buffer is using [find_address](find_address.py) script.  Look at the output and count the offset to `0x70257025` which is `%p`.  Offsets are the number of `0x<something>` or `(null)`.

In my case it was 14 but because I miss counted I thought it was 13 for a while.  If this next part fails double check your count.

Next run [hack](hack.py) script which uses pwntools to build a payload to overwrite the `sus` variable on the local copy of the exe.  It should run and show test flag stored in [flag.txt](flag.txt).

If that works run the [remote_hack](remote_hack.py).  You will need to update it with the port of your instance.