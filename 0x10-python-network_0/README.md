# 0x10. Python - Network #0

## Resources
**Read or watch:**

* [HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
* [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

## Tasks

### Task 0. cURL body size
<Details>
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

* The size must be displayed in bytes
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
</Details>

### Task 1. cURL to the end
<Details>
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

* Display only body of a 200 status code response
* You have to use curl
</Details>

### Task 2. cURL Method
<Details>
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

* You have to use curl
</Details>

### Task 3. cURL only methods
<Details>
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

* You have to use curl
</Details>

### Task 4. cURL headers
<Details>
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

* A header variable X-School-User-Id must be sent with the value 98
* You have to use curl
</Details>

### Task 5. cURL POST parameters
<Details>
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

* A variable email must be sent with the value test@gmail.com
* A variable subject must be sent with the value I will always be here for PLD
* You have to use curl
</Details>