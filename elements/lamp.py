from elements import colors

class Lamp:
    # It could has class attributes
    material = 'glass'

    # Attribute methods
    def __init__(self, voltage: int, socket, wattage: int, attached: bool = False) -> None:
        # Instance attributes
        self.voltage = voltage
        self.socket = socket
        self.wattage = wattage
        self.is_attached = attached

    def __str__(self) -> str:
        # Method to print info about created object
        return f"{colors.bold()}Lamp data:{colors.end()} \n{colors.underline()}Material:{colors.end()} {self.material}\n {colors.underline()}Voltage:{colors.end()} {self.voltage} volts\n {colors.underline()}Socket:{colors.end()} {self.socket}\n {colors.underline()}Wattage:{colors.end()} {self.wattage} watts."
