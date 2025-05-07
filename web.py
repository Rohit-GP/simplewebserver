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