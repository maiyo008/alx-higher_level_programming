# 0x11. Python - Network #1

## Resources
**Read or watch:**

* [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
* [Requests package](https://pypi.org/project/requests/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Tasks

### Tasks 0.What's my status? #0
<Details>
Write a Python script that fetches https://alx-intranet.hbtn.io/status

* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed like the following example (tabulation before -)
* You must use a with statement
</Details>

### Task 1. Response header value #0
<Details>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a with statement
</Details>

### Task 2. POST an email #0
<Details>
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

* The email must be sent in the email variable
* You must use the packages urllib and sys
* You are not allowed to import packages other than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement
* Please test your script in the sandbox provided, using the web server running on port 5000
</Details>