import machine
import socket
import uasyncio as asyncio
import ujson

LED1 = machine.Pin(2, machine.Pin.OUT)
LED2 = machine.Pin(0, machine.Pin.OUT)
LED3 = machine.Pin(4, machine.Pin.OUT)

def gpio_toggle(p):
    p.value(not p.value())


def gpio_on(p):
    p.value(0)


def gpio_off(p):
    p.value(1)


def socket_connect(address, port):
    s.settimeout(1.0)

    addr_info = socket.getaddrinfo(address, port)
    addr = addr_info[0][-1]

    try:
        print("Attempting to connect to socket server ...")
        s.connect(addr)
        print("Connection successful!")
    except Exception as e:
        print(e)


def socket_receive():
    while True:
        try:
            receive_string = s.recv(500)
            rxjsonobj = ujson.loads(receive_string)
            parse_command(rxjsonobj)
        except Exception as e:
            if errno.ETIMEDOUT:
                pass
            else:
                print(e)

        await asyncio.sleep(0.5)


class IotDevice:
    def __init__(self):
        self.LED1 = "Off"
        self.LED2 = "Off"
        self.LED3 = "Off"
        self.Temperature = 21.1
        self.Humidity = 63.4
        self.ID = "14-3826"

    def sample(self):
        self.Temperature = self.Temperature + 0.1

        if self.Temperature >= 30.0:
            self.Temperature = 15

        self.Humidity = self.Humidity + 0.5

        if self.Humidity >= 100:
            self.Humidity = 25.0


def parse_command(message):
    if "LED1" in message:
        if message["LED1"] == "On":
            gpio_on(LED1)
            Device.LED1 = "On"
            print("LED 1 On")
        else:
            gpio_off(LED1)
            Device.LED1 = "Off"
            print("LED 1 Off")

    if "LED2" in message:
        if message["LED2"] == "On":
            gpio_on(LED2)
            Device.LED2 = "On"
            print("LED 2 On")
        else:
            gpio_off(LED2)
            Device.LED2 = "Off"
            print("LED 2 Off")

    if "LED3" in message:
        if message["LED3"] == "On":
            gpio_on(LED3)
            Device.LED3 = "On"
            print("LED 3 On")
        else:
            gpio_off(LED3)
            Device.LED3 = "Off"
            print("LED 3 Off")


def socket_send(Data):
    mystring = ujson.dumps(Data)
    try:
        s.write(mystring + "\r\n")
    except Exception as e:
        if errno.ECONNRESET:
            socket_connect()
        print(e)

def system_status():
    while True:
        # Sample Sensors or get the latest result
        Device.sample()

        data = {}
        data['id'] = Device.ID
        data['temperature'] = Device.Temperature
        data['humidity'] = Device.Humidity
        data['led1'] = Device.LED1
        data['led2'] = Device.LED2
        data['led3'] = Device.LED3

        socket_send(data)

        await asyncio.sleep(0.5)


Device = IotDevice()

gpio_off(LED1)
gpio_off(LED2)
gpio_off(LED3)

s = socket.socket()
socket_connect("192.168.4.2", 1024)

# Initialize the Cooperative Scheduler and
# run the application.
loop = asyncio.get_event_loop()
loop.create_task(system_status())
loop.create_task(socket_receive())
loop.run_forever()
