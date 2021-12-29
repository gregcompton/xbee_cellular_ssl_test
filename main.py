
# TODO: Replace with the serial port where your local module is connected to.
COMPORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
# TODO: Replace with the phone number of the device to send the SMS to.
PHONE = "15551234567"
# TODO: Optionally, replace with the text of the SMS.
SMS_TEXT = "For the win"

def send_text():
    print(" +-------------------------------------+")
    print(" | XBee Python Library Send SMS Sample |")
    print(" +-------------------------------------+\n")

    from digi.xbee.devices import CellularDevice

    device = CellularDevice(COMPORT, BAUD_RATE)
    print('device instantiated')
    print(type(device))
    if device is not None:
        print('device is not None')
        pass
    else:
        print('device is None')

    try:
        print('try opening device')
        device.open()
        print('device opened')
    except Exception as e:
        print('Failed to open device')
        print(e)
        if device is not None and device.is_open():
            device.close()
            print('device closed')
        else:
            print('either device was None or it was not open')
        return


    try:
        print("Sending SMS to %s >> %s..." % (PHONE, SMS_TEXT))

        device.send_sms(PHONE, SMS_TEXT)

        print("Success")
    except Exception as e:
        print('Failed to send text')
        print(e)
    finally:
        if device is not None and device.is_open():
            device.close()
            print('device closed')
        else:
            print('either device was None or it was not open')
        return


def ssl_socket_example_get():
    print('Begin SSL socket GET example')
    from digi.xbee import xsocket
    from digi.xbee.devices import CellularDevice
    from digi.xbee.models.protocol import IPProtocol

    HOST = '' # todo: insert your host here
    PORT = 443
    gatewayid = '4bf926abf9b3'  # this is a special case for my route
    ROUTE = '' # todo: insert your route here

    GETREQUEST = 'GET %s HTTP/1.1\r\nHost: %s\r\n' \
                 'Connection: close\r\n' \
                 'Content-Type: application/json\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate, br\r\n' \
                 'Content-Length: 0\r\n\r\n'\
                 % (ROUTE, HOST)
    print('\n****************************\nGETREQUEST:')
    print(GETREQUEST, '\n****************************')

    print('opening xbee')
    xbee = CellularDevice(COMPORT, BAUD_RATE)
    xbee.open()
    print('xbee is open')

    print('creating socket')
    with xsocket.socket(xbee, IPProtocol.TCP_SSL) as sock:
        # Connect the socket.
        sock.connect((HOST, PORT))

        # Send an HTTP request.
        # sock.send(REQUEST.encode("utf8"))
        sock.send(GETREQUEST.encode("utf8"))
        # sock.sendall(GETREQUEST.encode("utf8"))

        # Receive and print the response.
        # data = sock.recv(1024)
        data = sock.recv(4096)
        print(data.decode("utf8"))

    print("Finished")

def socket_example_get():
    print('Begin chatt365 socket GET example')
    from digi.xbee import xsocket
    from digi.xbee.devices import CellularDevice
    from digi.xbee.models.protocol import IPProtocol

    HOST = "domain.com"  # todo: insert your host here e.g.  domain.com
    PORT = 80
    ROUTE = '/api/device/0013A20041DB3485' # todo: insert your route here e.g. /api/device/0013A20041DB3485
    GETREQUEST = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (ROUTE, HOST)

    print('opening xbee')
    xbee = CellularDevice(COMPORT, BAUD_RATE)
    xbee.open()
    print('xbee is open')

    print('creating socket')
    with xsocket.socket(xbee, IPProtocol.TCP) as sock:
        # Connect the socket.
        sock.connect((HOST, PORT))

        # Send an HTTP request.
        # sock.send(REQUEST.encode("utf8"))
        sock.send(GETREQUEST.encode("utf8"))

        # Receive and print the response.
        data = sock.recv(1024)
        print(data.decode("utf8"))

    print("Finished")

def main():
    # send_text()
    # socket_example_get()
    ssl_socket_example_get()

if __name__ == '__main__':
    main()
