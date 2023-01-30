from elements import colors


class Socket:

    def __init__(self, type: str):
        self.type = type
        self.switch_connected = False
        self.lamp_attached = False

    def attach_lamp(self, lamp):
        if self.type == lamp.socket:
            lamp.is_attached = True
            self.lamp_attached = True
            return f"{colors.green()}Lamp connected!{colors.end()}"
        else:
            return f"{colors.red()}Check fit between socket and bulb.{colors.end()}"

    def deattach_lamp(self, lamp):
        lamp.is_attached = False
        self.lamp_attached = False
        print(f'{colors.blue()}Lamp disconnected!{colors.end()}')

    def __str__(self) -> str:
        # Method to print info about created object
        return f"{colors.bold()}Socket data:{colors.end()}\n {colors.underline()}Type:{colors.end()} {self.type}\n {colors.underline()}Switch connected:{colors.end()} {self.switch_connected}\n {colors.underline()}Lamp attached:{colors.end()} {self.lamp_attached}"
