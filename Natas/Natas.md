# Natas Challenges

### Natas0

Password is in the source code

```
gtVrDuiDfck831PqWsLEZy5gyDz1clto 
```
### natas1
Source Code of the screen again
```
ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi 
```

### natas2
source code has a image. Going to the images directory is has another file with the password. Users.txt
```
sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```

### natas3
This was found in the source code. This references robots.txt
```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```
There is a hidden directory found in robots.txt
```html
User-agent: *
Disallow: /s3cr3t/
```
In this directory there is a uses.txt with the next password
```
Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```
### natas4
```html
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```
This is referencing the referer field in the request. Refreshing the page will populate the needed field.

Changing the request to the following will get you the password.

![image-20200910191407067](natas4.png)

```
Referer: http://natas5.natas.labs.overthewire.org/
```
```
iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```

### natas5 

You are greeted with the following prompt.

```
Access disallowed. You are not logged in
```

What is associated with logging in? COOKIES

Changing the loggedin cookies cookie from 0 to 1 fixes this.

![image-20200910191441513](natas5.png)

Refreshing this page after this will reveal the password.

```
aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

### natas6

A prompt for a secret appears.

We can try some stuff but nah.

Let look at the source code.

```php

<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

The php script calls for the file secrets.inc in includes directory.

The page appears blank but looking at the source code will reveal the password for the first screen.

![image-20200910191510471](natas6.png)

```
7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

### natas7

A page with 2 options.

Home and About

Clicking one adds `?page=home` and `?page=about` to the url. I smell Local File Inclusion.

```
http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../etc/natas_webpass/natas8
```

The `../` allows us to move up a directory. Lets just do it a lot to make sure we get to the top. The natas challenge web page stats we can always find the password file under `/etc/natas_webpass/` and the next level name.

![image-20200910193416105](natas7.png)

```
DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 
```

### natas8

Another Secret Page. Oh Dear. Lets take a look at the source code.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

Alright so we have a secret and we have how it got there. Lets reverse engineer. For the sake of easiness (and the fact that I am using a windows OS), lets use cyberchef to get the secret.

The order to get is base64 > Reverse String > bin2hex so we have to do it backwards. From Hex > Reverse the order > Decode base64.

![image-20200910194548812](natas8.png)

the final code is `oubWYf2kBq` which reveals the password.

```
W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```