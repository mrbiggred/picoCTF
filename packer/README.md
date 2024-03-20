At first I tried installing Ghidra but that didn't help and was overkill.  It appears to have a bunch of complicated loops likely to confuse the decompiler.  Not sure why Ghidra didn't find strings.  Likely I don't know how to use the tool.

I left the decompiled source files in the source folder but removed the Ghider project files.

Running the out application prompts you to enter a password.  Maybe that is what the loops in the application do is check the password?

I then read the hint and decompressed the binary:

```
upx -d out out_d
```

Once decompressed I opened in a hexeditor:

```
hexedit out_d
```

Then searched for "pass" (`^W`) and found the text:

```
00095000  01 00 02 00  00 00 00 00   45 6E 74 65  72 20 74 68                                      ........Enter th
00095010  65 20 70 61  73 73 77 6F   72 64 20 74  6F 20 75 6E                                      e password to un
00095020  6C 6F 63 6B  20 74 68 69   73 20 66 69  6C 65 3A 20                                      lock this file: 
00095030  00 59 6F 75  20 65 6E 74   65 72 65 64  3A 20 25 73                                      .You entered: %s
00095040  0A 00 00 00  00 00 00 00   50 61 73 73  77 6F 72 64                                      ........Password
00095050  20 63 6F 72  72 65 63 74   2C 20 70 6C  65 61 73 65                                       correct, please
00095060  20 73 65 65  20 66 6C 61   67 3A 20 37  30 36 39 36                                       see flag: 70696
00095070  33 36 66 34  33 35 34 34   36 37 62 35  35 33 39 35                                      36f4354467b55395
00095080  38 35 66 35  35 36 65 35   30 33 34 36  33 36 62 33                                      85f556e5034636b3
00095090  31 34 65 33  36 35 66 34   32 33 31 36  65 33 34 35                                      14e365f42316e345
000950A0  32 36 39 33  33 35 33 35   66 33 36 36  36 36 36 33                                      26933535f3666663
000950B0  39 33 36 33  34 36 35 36   36 37 64 00  41 63 63 65                                      9363465667d.Acce
000950C0  73 73 20 64  65 6E 69 65   64 00 78 65  6F 6E 5F 70                                      ss denied.xeon_p
000950D0  68 69 00 68  61 73 77 65   6C 6C 00 2E  2E 2F 63 73                                      hi.haswell.../cs
```

Coping the numbers after the "flag" and pasted them in Cyber Chef.  Cyber Chef then prompted to use From Hex:

```
Hex:
7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f36666639363465667d

Flag:
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_6ff964ef}
```


