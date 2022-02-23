import socketserver
import time
import logging
import sipfullproxy

HOST, PORT = "147.175.191.134", 5060
response_codes_dict = {
    200: "200 OK",

    400: "400 Bad Request",
    406: "406 Not Acceptable",
    480: "480 Temporarily Unavailable",
    488: "488 Not Acceptable Here",

    500: "500 Server Internal Error",
}


def main():
    print("Poznámka --> aby server fungoval správne je nutné aby premenná HOST obsahovala IP adresu zariadenia"
          " na ktorom je spustený server.")
    logging.basicConfig(format='%(asctime)s: %(message)s', filename='dennik.txt', level=logging.INFO, datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
