from datetime import datetime
from elements import colors


class Switch:

    def __init__(self) -> None:
        self.power_source_attached = False
        self.socket_attached = False
        self.system_works = False
        self.is_on = False
        self.start = ""
        self.end = ""

    def attach_socket(self, socket):
        socket.is_connected = True
        self.socket_attached = True

    def deattach_socket(self, socket):
        socket.is_connected = False
        self.socket_attached = False

    def attach_power(self, power):
        power.is_conected = True
        self.power_source_attached = True

    def deattach_power(self, power):
        power.is_conected = False
        self.power_source_attached = False

    def system_check_up(self, socket):
        if self.power_source_attached == False and self.socket_attached == False:
            return f"{colors.red()}Connect the switch to a power source and a socket for your lamp to light up.{colors.end()}"
        elif self.power_source_attached == True and self.socket_attached == False:
            return f"{colors.red()}Connect the switch to a socket.{colors.end()}"
        elif self.power_source_attached == False and self.socket_attached == True:
            return f"{colors.red()}Connect the switch to a power source.{colors.end()}"
        elif self.power_source_attached == True and self.socket_attached == True and socket.lamp_attached == False:
            return f"{colors.red()}Check the connexion between the socket and its lamp.{colors.end()}"
        else:
            self.system_works = True
            return f"{colors.green()}System ready to work!{colors.end()}"

    def clicked(self):
        if self.system_works == True and self.is_on == False:
            self.start = datetime.now().replace(microsecond=0)
            self.is_on = True
            return f"{colors.green()}Lamp is on!{colors.end()} 💡"
        elif self.system_works == True and self.is_on == True:
            self.end = datetime.now().replace(microsecond=0)
            self.is_on = False
            time_consumption_to_hour = (self.end - self.start).total_seconds() / (60 * 60)
            final_price = self.price_current_consumption(duration=time_consumption_to_hour)
            return f"{colors.green()}Lamp is off.\nIt worked for {time_consumption_to_hour:.3f} hours and it costs {final_price:.2f} euros.{colors.end()}"
        else:
            print(f"{colors.red()}Check the connections and try again. Try .system_check_up(socket) to investigate the problem.{colors.end()}")

    def price_current_consumption(self, duration):
        kwh_price = 0.15 # We could try with an API or web scraping from a real source price
        final_price = round(duration, 3) * kwh_price
        return final_price

    def __str__(self) -> str:
        # Method to print info about created object
        return f"{colors.bold()}Switch data:{colors.end()}\n {colors.underline()}Power source attached:{colors.end()} {self.power_source_attached}\n {colors.underline()}Socket attached:{colors.end()} {self.socket_attached}\n {colors.underline()}System working:{colors.end()} {self.system_works}\n {colors.underline()}System is on:{colors.end()} {self.is_on}"
