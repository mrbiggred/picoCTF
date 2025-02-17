Watch me fail to solve this issue on [here](https://youtu.be/AT8w2fsgzsA).  I have figured out that I need to use a `%n` `printf` exploit to overwrite a function pointer to print out the flag.  I think I need use the payload in the `printf(buf)` call to overwrite the call to the `puts(normal_string)`.

```c
	fgets(buf, 1024, stdin);
	printf(buf);

	puts(normal_string);
```

I'm not sure sure why it gives me the address of the `setvbuf`.  I'm guessing I need inject that into the payload but not sure why or how yet.  Have to think about this for a while.