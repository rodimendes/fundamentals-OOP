from elements.switch import Switch
from elements.socket import Socket
from elements.power_source import PowerSource
from elements.lamp import Lamp
from elements import colors

switch = Switch()
socket = Socket("DI-38")
power = PowerSource(0)
lampada = Lamp(voltage=220, socket='DI-38', wattage=7)


def test_nothing_attached():
    assert switch.system_check_up(socket=socket) == f"{colors.red()}Connect the switch to a power source and a socket for your lamp to light up.{colors.end()}"

def test_socket_attached():
    switch.attach_socket(socket)
    assert switch.socket_attached == True
    assert switch.system_check_up(socket=socket) == f"{colors.red()}Connect the switch to a power source.{colors.end()}"

def test_socket_deattached():
    switch.deattach_socket(socket)
    assert switch.socket_attached == False

def test_power_attached():
    switch.attach_power(power)
    assert switch.power_source_attached == True
    assert switch.system_check_up(socket=socket) == f"{colors.red()}Connect the switch to a socket.{colors.end()}"

def test_power_deattached():
    switch.deattach_power(power)
    assert switch.power_source_attached == False

def test_system_without_lamp():
    switch.attach_socket(socket)
    switch.attach_power(power)
    assert switch.system_check_up(socket=socket) == f"{colors.red()}Check the connexion between the socket and its lamp.{colors.end()}"

def test_lamp_system_works():
    switch.attach_socket(socket)
    switch.attach_power(power)
    socket.attach_lamp(lampada)
    assert switch.system_check_up(socket=socket) == f"{colors.green()}System ready to work!{colors.end()}"

def test_lamp_is_on():
    switch.attach_socket(socket)
    switch.attach_power(power)
    socket.attach_lamp(lampada)
    assert switch.clicked() == f"{colors.green()}Lamp is on!{colors.end()} 💡"

def test_lamp_is_off():
    switch.attach_socket(socket)
    switch.attach_power(power)
    socket.attach_lamp(lampada)
    switch.is_on = True
    time_consumption_to_hour = 0
    assert switch.clicked() == f"{colors.green()}Lamp is off.\nIt worked for {time_consumption_to_hour:.3f} hours and it costs 0.00 euros.{colors.end()}"
