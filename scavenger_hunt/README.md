# Scavenger Hunt

Look at the HTML, see the first part of the flag an HTML comment:

```
<!-- Here's the first part of the flag: picoCTF{t -->
```

Look at the JS and notice a hint to look at robotx.txt:

```
/* How can I keep Google from indexing my website? */
```

Found the 3rd part in the robots.txt:

```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

Found part 2 in the ccs:

```
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

Look at the .htaccess file:

```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

Part 5 is in the .DS_Store file:

```
Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```

Flag is: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}


ask@saturdaymp.com