# EX01 Developing a Simple Webserver
## Date: 07-05-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:

### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

Name : Rohit GP

Ref no / Reg no : 24900185 / 212224220082

```
from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content for the web page
content = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            body {
                background-color: rgb(222, 219, 219);
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            h1 {
                background-color: black;
                color: white;
                text-align: center;
                padding: 10px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            b {
                color: blue;
            }
            .done {
                color: indianred;
                text-decoration: none;
            }
            div {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 20px 50px;
                box-shadow: 4px 4px 4px gray;
                margin: 20px auto;
                max-width: 600px;
            }
        </style>
    </head>
    <body>
        <h1><strong>DEVICE CONFIGURATION</strong></h1>
        <div>
            <ul>
                <b>Device name:</b> GPR <hr>
                <b>Processor:</b> 12th Generation Intel® Core™ i7 processor <hr>
                <b>Installed RAM:</b> 16.0 GB (15.7 GB usable) <hr>
                <b>Device ID:</b> 15EEA3B2-7EF5-4DEC-903D-577382C3C005 <hr>
                <b>Product ID:</b> 00342-42709-07393-AAOEM <hr>
                <b>System type:</b> 64-bit operating system, x64-based processor <hr>
                <b>Pen and touch:</b> No pen or touch input is available for this display <hr>
                <br>
                <b class="done">Done by:</b> ROHIT GP - 24900185
            </ul>
        </div>
    </body>
</html>
"""

# Custom HTTP request handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

# Server configuration
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

![alt text](<Screenshot 2025-05-07 094035.png>)

![alt text](<Screenshot 2025-05-07 094117.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
