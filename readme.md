# Mischief

# Required Libraries

- requests
- colorama

# Example

Place a list of accounts (emails) into a json file array:

```json
[
    "test@example.com"
]
```

Then call `pymischief` and the file:

```bash
 kevin@Logan bin $ ./pymischief.py test.json
[test@example.com]========================
 000webhost [14 million accounts total]
   Domain: 000webhost.com
   2015-03-01
   Data still on web
   Hack verified by website
   Leaked data:
     - Email addresses
     - IP addresses
     - Names
     - Passwords
 8tracks [7 million accounts total]
   Domain: 8tracks.com
   2017-06-27
   Data still on web
   Hack verified by website
   Leaked data:
     - Email addresses
     - Passwords
...
Paste: test@example.com ==============
  AdHocUrl: http://siph0n.in/exploits.php?id=4560
  AdHocUrl: http://balockae.online/files/BlackMarketReloaded_users.sql
  AdHocUrl: http://siph0n.in/exploits.php?id=7854
  AdHocUrl: http://pxahb.xyz/emailpass/www.ironsudoku.com.txt
  AdHocUrl: http://pxahb.xyz/emailpass/www.optimale-praesentation.de.txt
  Pastebin: https://pastebin.com/01ywCrGV
  QuickLeak: http://quickleak.se/QtPly6aE
  Pastebin: https://pastebin.com/B8TeVHVt
  Pastebin: https://pastebin.com/VvKhYPR0
  Pastebin: https://pastebin.com/ktnvMJDH
  Pastebin: https://pastebin.com/tJmdW6sp
  Pastebin: https://pastebin.com/L730bR9a
  Pastebin: https://pastebin.com/h2KJPWJ9
  Pastebin: https://pastebin.com/0SqeEgZe
  Pastebin: https://pastebin.com/tcHtWCFD
  Pastebin: https://pastebin.com/yukVFztc
...
```

# MIT License

**Copyright (c) 2019 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
