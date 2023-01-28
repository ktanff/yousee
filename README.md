# yousee
Only "you" see!

A text steganography simply readable only by "you", no complex calculation required.

Just memorize a relatively short-length integer as a *passcode*, forever, never share it with no one.

UC hides your secret text messages in high entropy cover text using a simple steganography scheme.

## Usage:
- Secret: the text you want to hide it.
- Passcode: an integer number that uncovers the hidden message.
- KeepSpaces: (yes/no) indicates that space characters [Spc] in secret message are encoded in covering message or ignored.

## Example.
Secret: "Sharp Eye"

Passcode = 2350

Result covered text :
```
(Ss:m   I7hE1C   vprjaEge   Aj   krJM   ecpr   Qn6[_]   4nerv5u   rEtse   &7yV   euO   1e$Ae
```

That simply read by anyone  who knows the passcode, as follows;
```
(Ss:m   I7hE1C   vprjaEge   Aj   krJM   ecpr   Qn6[_]   4nerv5u   rEtse   &7yV   euO   1e$Ae
 2        3          5     0      2       3        5   0           2        3    ---       5            
```

- The above example takes that the space character is kept.
- If let KeepSpaces=No, a coverage like as follows could be resulted;
