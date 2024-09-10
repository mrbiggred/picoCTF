The secret to this CTF, at least for me, was to check the `robots.txt` file.  Until someone suggested I try that I was stuck.

The `robots.txt` file looks like:

```txt
User-agent: *
Disallow: /instructions.txt
Disallow: /uploads/
```

You can view the instructions text file but the juicy part is the `/uploads/` folder.  This is where all the files that get uploaded will get put.

You can figure out the site is using PHP by using the [Wappalyzer](https://www.wappalyzer.com/) brower plugin or by viewing the headers in the browser develoepr tools.

The website does two checks to make sure the image is PNG.  The first is the file name must have ".png" in the file name and the second is it much and "PNG" in the first couple bytes.  These limitations can be found in the `instructions.txt` file or by experimenting by uploading different files.

The check if a file can be executed upload the [payload_info.png.php](payload_info.png.php).  Then go to `/uploads/payload_info.png.php`.  If should show the [phpinfo](https://www.php.net/manual/en/function.phpinfo.php) page.

Now that we know PHP scripts will run create a script that executes Linux commands.  In this case we need to find the flag file and after some trial and error is found at the root of the website.  Use the [payload_ls.png.php](payload_ls.png.php) to get the name of the flag file.

Assuming the flag file is `ABCDE.txt` access the file directly in the browser by going to `/ABCDE.txt`.