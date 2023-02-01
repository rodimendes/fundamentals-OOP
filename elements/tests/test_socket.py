from elements.socket_type import SocketType
from elements.lamp import Lamp
from elements import colors

my_socket = SocketType("E-27")
my_lamp = Lamp(110, "E-27", 60)


def test_attach_lamp_socket():
    my_socket.attach_lamp(my_lamp)
    assert my_socket.lamp_attached == True

def test_deattached_lamp_socket():
    my_socket.deattach_lamp(my_lamp)
    assert my_socket.lamp_attached == False

def test_attach_lamp_socket_error():
    my_socket.type = "E-10"
    assert my_socket.attach_lamp(my_lamp) == f"{colors.red()}Check fit between socket and bulb.{colors.end()}"
