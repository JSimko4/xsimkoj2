import socketserver
import socket
import time
import logging
import sipfullproxy

# response_codes_dict = {
#     200: "200 OK",
#
#     400: "400 Bad Request",
#     406: "406 Not Acceptable",
#     480: "480 Temporarily Unavailable",
#     488: "488 Not Acceptable Here",
#
#     500: "500 Server Internal Error",
# }

response_codes_dict = {
    200: "200 OK",

    400: "400 Bad Request",
    406: "406 Not Acceptable",
    480: "480 Temporarily Unavailable",
    488: "488 Not Acceptable Here",

    500: "500 Server Internal Error",
}


def main():
    print("Server spustený...\n")
    logging.basicConfig(format='%(asctime)s: %(message)s', filename='dennik.txt', level=logging.INFO, datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
