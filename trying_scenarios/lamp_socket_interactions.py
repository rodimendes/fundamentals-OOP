from elements.lamp import Lamp
from elements.socket import Socket

# Creating a new object Lamp.
my_lamp = Lamp(voltage=240, socket="DI-38", wattage=7, attached=True)

# Print its settings.
print(my_lamp)

# Creating new object Socket.
my_socket = Socket(type="E-10")

# That object isn't suitable for the created lamp
# and returns an error when attached.
print(my_socket.attach_lamp(my_lamp))

# We can adjust the lamp socket type...
my_lamp.socket = "E-10"

# And try to connect again.
# Now it works.
print(my_socket.attach_lamp(my_lamp))
