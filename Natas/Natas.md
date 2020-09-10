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

TBD