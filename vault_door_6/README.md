# Vault Door 6

Download the java file.  See there is a XOR method.

```java
byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x67, 0x65, 0x67, 0x62, 0x6c, 0x6d, 0x66,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
```

And = When both are true (both 1)
Or  = When either or both are true (either 1)
XoR = When only one is true

To reverse and XoR just do another XoR.  For example:

```
0x36:   00111011
0x55:   01010101
        --------
        01101110 = n in ascii
```

Use CyberChef to find the answer:

https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'55'%7D,'Standard',false)&input=M2IgNjUgMjEgYSAzOCAwMCAzNiAxZCBhIDNkIDYxIDI3IDExIDY2IDI3IGEgMjEgMWQgNjEgM2IgYSAyZCA2NSAyNyBhIDY3IDY1IDY3IDYyIDZjIDZkIDY2
