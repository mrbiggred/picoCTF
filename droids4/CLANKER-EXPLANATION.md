# Copilot w/ GPT-5.4 Answer

I asked Copilot if I could solve this challenge without a APK emulator and it did.  When asked how it did it it gave the response below.

## Clanker Explanation

**How I solved it:** I treated the APK as a static reversing problem, not something that needed to be run. The key was realizing the Java code only gates access to the real logic, and the flag is ultimately produced inside the native library.

### 1. Decompile the APK
I used `jadx` to get readable Java from `four.apk`.

```bash
jadx -d "$(pwd)/out" "$(pwd)/four.apk"
```

That produced decompiled sources like:

- `MainActivity.java`
- `FlagstaffHill.java`

### 2. Find the app’s entry logic
In `MainActivity.java`:

```java
public void buttonClick(View view) {
    String content = this.text_input.getText().toString();
    this.text_bottom.setText(FlagstaffHill.getFlag(content, this.ctx));
}
```

That told me the interesting logic starts in:

```java
FlagstaffHill.getFlag(content, this.ctx)
```

### 3. Reverse `getFlag()`
In `FlagstaffHill.java`:

```java
public static String getFlag(String input, Context ctx) {
    StringBuilder ace = new StringBuilder("aaa");
    StringBuilder jack = new StringBuilder("aaa");
    StringBuilder queen = new StringBuilder("aaa");
    StringBuilder king = new StringBuilder("aaa");
    ace.setCharAt(0, (char) (ace.charAt(0) + 4));
    ace.setCharAt(1, (char) (ace.charAt(1) + 19));
    ace.setCharAt(2, (char) (ace.charAt(2) + 18));
    jack.setCharAt(0, (char) (jack.charAt(0) + 7));
    jack.setCharAt(1, (char) (jack.charAt(1) + 0));
    jack.setCharAt(2, (char) (jack.charAt(2) + 1));
    queen.setCharAt(0, (char) (queen.charAt(0) + 0));
    queen.setCharAt(1, (char) (queen.charAt(1) + 11));
    queen.setCharAt(2, (char) (queen.charAt(2) + 15));
    king.setCharAt(0, (char) (king.charAt(0) + 14));
    king.setCharAt(1, (char) (king.charAt(1) + 20));
    king.setCharAt(2, (char) (king.charAt(2) + 15));
    String password = "".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString());
    return input.equals(password) ? "call it" : "NOPE";
}
```

Each string starts as `"aaa"`, where `'a' = 97`. The code adds offsets to each character.

#### `ace`
- `a + 4 = e`
- `a + 19 = t`
- `a + 18 = s`

So `ace = "ets"`

#### `jack`
- `a + 7 = h`
- `a + 0 = a`
- `a + 1 = b`

So `jack = "hab"`

#### `queen`
- `a + 0 = a`
- `a + 11 = l`
- `a + 15 = p`

So `queen = "alp"`

#### `king`
- `a + 14 = o`
- `a + 20 = u`
- `a + 15 = p`

So `king = "oup"`

Then they are concatenated as:

```java
queen + jack + ace + king
```

So:

```text
alp + hab + ets + oup = alphabetsoup
```

That gave the first important result:

```text
alphabetsoup
```

At this point, `getFlag()` does **not** return the flag. It only returns:

- `"call it"` if input is correct
- `"NOPE"` otherwise

That told me there had to be another stage.

---

### 4. Notice the native library
In `MainActivity.java` there is also:

```java
System.loadLibrary("hellojni");
```

And in `FlagstaffHill.java`:

```java
public static native String cardamom(String str);
```

That means some logic lives in a native `.so` file instead of Java.

So the next target was:

```text
libhellojni.so
```

### 5. Inspect the native library
The APK contained several copies of the library for different architectures, for example:

```text
four-unzip/lib/x86_64/libhellojni.so
```

I listed its exported symbols and found these JNI/native functions:

- `Java_com_hellocmu_picoctf_FlagstaffHill_cardamom`
- `Java_com_hellocmu_picoctf_FlagstaffHill_cilantro`
- `Java_com_hellocmu_picoctf_FlagstaffHill_fenugreek`
- `Java_com_hellocmu_picoctf_FlagstaffHill_paprika`
- `Java_com_hellocmu_picoctf_FlagstaffHill_sesame`

Plus helper functions like:

- `pepper`
- `unscramble`
- `chervil`
- `basil`
- `sumac`
- `oregano`

That confirmed the hidden work happens in the native layer.

### 6. Reverse `cardamom`
Disassembling `Java_com_hellocmu_picoctf_FlagstaffHill_cardamom` showed this high-level pattern:

1. Receive input string from Java
2. Check it with a helper function
3. If valid, call `pepper`
4. If invalid, return `"try again"`

So `cardamom()` is essentially:

```c
if (input_is_correct) {
    return pepper(input);
} else {
    return "try again";
}
```

### 7. Determine what input `cardamom` expects
The helper used by `cardamom` is `chervil`. Reversing `chervil` showed it reconstructs the same string we already found in Java:

```text
alphabetsoup
```

So the native function is expecting:

```text
cardamom("alphabetsoup")
```

That matched the Java-side result and confirmed the path forward.

### 8. Reverse `pepper`
The `pepper` function was the important one. Its structure was:

1. Load a blob of bytes from `.rodata`
2. Duplicate the user input string
3. Call a helper named `unscramble`

`unscramble` does a simple repeated XOR:

```c
output[i] = encoded[i] ^ key[i % key_length]
```

where:

- `encoded` = bytes embedded in `.rodata`
- `key` = the input string
- input string here = `alphabetsoup`

So `pepper("alphabetsoup")` is really:

```text
XOR(encoded_bytes, "alphabetsoup")
```

### 9. Extract the encoded bytes from `.rodata`
From the native library’s read-only data section, the `pepper` blob begins at offset `0x1aa0` and is `0x1f` bytes long.

Those bytes were:

```python
[
    0x11, 0x05, 0x13, 0x07, 0x22, 0x36, 0x23, 0x0f,
    0x1d, 0x00, 0x01, 0x5e, 0x11, 0x0d, 0x02, 0x1c,
    0x08, 0x01, 0x10, 0x18, 0x12, 0x1d, 0x19, 0x09,
    0x4f, 0x1f, 0x19, 0x04, 0x0d, 0x1b, 0x18,
]
```

### 10. Decode with XOR
I decoded them with the repeating key `alphabetsoup`:

```python
key = b"alphabetsoup"

pepper_blob = bytes([
    0x11, 0x05, 0x13, 0x07, 0x22, 0x36, 0x23, 0x0f,
    0x1d, 0x00, 0x01, 0x5e, 0x11, 0x0d, 0x02, 0x1c,
    0x08, 0x01, 0x10, 0x18, 0x12, 0x1d, 0x19, 0x09,
    0x4f, 0x1f, 0x19, 0x04, 0x0d, 0x1b, 0x18,
])

decoded = bytes(b ^ key[i % len(key)] for i, b in enumerate(pepper_blob))
print(decoded.decode())
```

That produced:

```text
picoCTF{not.particularly.silly}
```

---

## Why no emulator was needed
An emulator would only have helped if we wanted to click through the app interactively. But the APK already contained everything needed:

- Java logic in decompiled classes
- native logic in `libhellojni.so`
- encoded flag bytes in `.rodata`

So the whole challenge was solvable by **static analysis** alone.

## Final reasoning chain
The full solve path was:

1. Decompile APK with `jadx`
2. Inspect `MainActivity`
3. Reverse `FlagstaffHill.getFlag()`
4. Recover `alphabetsoup`
5. Notice `cardamom()` is native
6. Reverse `libhellojni.so`
7. Confirm `cardamom` expects `alphabetsoup`
8. Extract `pepper`’s encoded bytes from `.rodata`
9. XOR-decode them with `alphabetsoup`
10. Recover the flag

**Flag:**
```text
picoCTF{not.particularly.silly}
```