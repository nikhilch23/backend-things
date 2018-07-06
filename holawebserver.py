from http.server import BaseHTTPRequestHandler, HTTPServer

 
class WebServerHandler(BaseHTTPRequestHandler):  #Inheritance concept

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)    #200 implies successful get request
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body>Hello! <a href= '/hola'> Go to Hola </a></body></html>"

                self.wfile.write(bytes(message, 'utf-8'))    #Converts the string into a byte code (a requisite for python 3.x but not of 2.x)
                print (message)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body> Hola! <a href= '/hello'> Back to Hello </a> </body></html>"

                self.wfile.write(bytes(message, 'utf-8'))    #Converts the string into a byte code (a requisite for python 3.x but not of 2.x)
                print (message)
                return    
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)   #arguments are server address and a Request handler class
        print ("Web Server running on port %s" % port)
        server.serve_forever()     #Server will keep listening till an interuption occurs
    except KeyboardInterrupt:     #Built in Keyboard interruption in python which is trigerred if the user enters ^C.
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
