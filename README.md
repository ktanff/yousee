# yousee
Only "you" see!

A text steganography simply readable only by "you", no complex calculation required.

Just memorize a relatively short-length integer as a *passcode*, forever for yourself, but never share it with no one.

UC hides your secret text messages in high entropy cover text using a simple steganography scheme.

## Usage:
- *Secret*: the text you want to hide it.
- *Passcode*: an integer number that uncovers the hidden message.
- *KeepSpaces*: (yes/no) indicates that space characters [Spc] in secret message are encoded in covering message or to be ignored.

## Example.
Secret: "Sharp Eye"

Passcode = 2350

A covered text might be resulted as follows;
```
(Ss:m   I7hE1C   vprjaEge   Aj   krJM   ecpr   Qn6[_]   4nerv5u   rEtse   &7yV   euO   1e$Ae
```

That simply is read by anyone who knows the *passcode*, as follows;
```
(Ss:m   I7hE1C   vprjaEge   Aj   krJM   ecpr   Qn6[_]   4nerv5u   rEtse   &7yV   euO   1e$Ae
 2        3          5     0      2       3        5   0           2        3    ---       5
 S        h          a            r       p       ' '              E        y              e
```

- The above example assumes that the space character is kept.
- Let KeepSpaces=No, a coverage message might lbe like as follows;



```
qSd=aAAk   brhVi}e   QtLu   r-zxact   jm7>y   Nro   bgp   dI@   ac9pEhg   85]_.   ty   Fue7ss|
```
