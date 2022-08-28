from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client


def OnDataReceive(addr, *data):
    """ Send received message. """
    oscClient.send_message(addr, data)


if __name__ == "__main__":
    address = "127.0.0.1"
    server_port = 7001
    client_port = 8001

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/test", OnDataReceive)

    oscServer=osc_server.ThreadingOSCUDPServer((address,server_port), dispatcher)
    oscClient=udp_client.SimpleUDPClient(address, client_port)

    print("Serving on {}".format(oscServer.server_address))
    oscServer.serve_forever()