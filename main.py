import socketserver
import socket
import time
import logging
import sipfullproxy


# ok_200 = "200 OK"
# not_acceptable_here_488 = "488 Not Acceptable Here"
# bad_request_400 = "400 Bad Request"
# unvailable_480 = "480 Temporarily Unavailable"
# server_internal_500 = "500 Server Internal Error"
# not_acceptable_406 = "406 Not Acceptable"

response_codes_dict = {
    200: "200 OK",

    400: "400 Bad Request",
    406: "406 Not Acceptable",
    480: "480 Temporarily Unavailable",
    488: "488 Not Acceptable Here",

    500: "500 Server Internal Error",
}


def main():
    print(response_codes_dict[200])
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
