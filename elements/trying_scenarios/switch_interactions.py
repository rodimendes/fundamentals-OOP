from elements.switch import Switch
from elements.socket_type import SocketType
from elements.power_source import PowerSource
from elements.lamp import Lamp

# Creating a new object from Switch class.
my_switch = Switch()

# Print its information.
# For now, nothing is connected to the switch.
print(my_switch)

# Socket and power source objects to be connected.
my_socket = SocketType(type="E-27")
my_power_source = PowerSource(capacity=0, connected=False) # capacity == 0, means ilimited source

print(my_switch.system_check_up(my_socket))

# Attaching...
my_switch.attach_socket(my_socket)
my_switch.attach_power(my_power_source)

# Verifying system connections
# we get an error because there is no lamp associated to a socket.
my_switch.system_check_up(socket=my_socket)

# Creating a lamp object...
my_lamp = Lamp(voltage=240, socket="E-27", wattage=7)
# and attaching it to the socket...
my_socket.attach_lamp(my_lamp)
# we get a confirmation that a lamp was attached to a switch.

# Verifying, one more time, the system connections
# we discover that the system is ready to turn on the lamp.
my_switch.system_check_up(socket=my_socket)

# Finally, we can turn the lamp on and off, obtaining a summary of consumption and the amount to be paid.
print(my_switch.clicked())
while my_switch.is_on == True:
    off = input("Turn off the light [Y / N]? ").upper().strip()
    if off[0] == "Y":
        print(my_switch.clicked())
