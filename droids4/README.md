# Droids 4

First thing was unzip it.  Didn't see anything usefule.

Then asked the clanker how to decompile a apk and it recommend `jadx`.  Had some issues running jadx on Kali and it would not use relative paths so use absolute paths instead:

```
 jadx -d "$(pwd)/out" "$(pwd)/four.apk"
```

Poked around and found the below in FlagstaffHill.java:

```
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

I think the password is:

```
// a = 97
StringBuilder ace = new StringBuilder("aaa");      
StringBuilder jack = new StringBuilder("aaa");
StringBuilder queen = new StringBuilder("aaa");
StringBuilder king = new StringBuilder("aaa");
ace.setCharAt(0, (char) (ace.charAt(0) + 4));     // e
ace.setCharAt(1, (char) (ace.charAt(1) + 19));    // t
ace.setCharAt(2, (char) (ace.charAt(2) + 18));    // s
jack.setCharAt(0, (char) (jack.charAt(0) + 7));   // h
jack.setCharAt(1, (char) (jack.charAt(1) + 0));   // a
jack.setCharAt(2, (char) (jack.charAt(2) + 1));   // b
queen.setCharAt(0, (char) (queen.charAt(0) + 0)); // a
queen.setCharAt(1, (char) (queen.charAt(1) + 11));// l
queen.setCharAt(2, (char) (queen.charAt(2) + 15));// p
king.setCharAt(0, (char) (king.charAt(0) + 14));  // o
king.setCharAt(1, (char) (king.charAt(1) + 20));  // u
king.setCharAt(2, (char) (king.charAt(2) + 15));  // p
String password = "".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString());
return input.equals(password) ? "call it" : "NOPE";

// alphabetsoup
```

I'm assuming I need to call the method "alphabetsoup".  Likely by adding the call in the MainActivity.java file.  Problem is I don't have a apk emulator.

Asked the clanker for help and it ran commands that found the `cardomom` string.  It then figured out it was in the .so file and traced the calls in the .so file to get the answer.  The clanker (GitHub Copilot w/ ) in the CLANKER_EXPLANATION.md file.

