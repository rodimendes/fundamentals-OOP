from elements import colors

class PowerSource:

    def __init__(self, capacity: int, connected: bool = False):
        self.capacity = capacity
        self.is_conected = connected

    def energy_supply(self):
        # self.power == 0 means the source has no colors.end()
        if self.capacity == 0:
            return f'{colors.green()}System connected to a unlimited source.{colors.end()}'
        else:
            return f'{colors.yellow()}System connected to a limited source.{colors.end()}'

    def estimate_monthly_consumption(self, wattage, elapsed_daily_time, kwh_price: float):
        monthly_consumption_kwh = wattage * elapsed_daily_time * 30 / 1000
        monthly_costs = monthly_consumption_kwh * kwh_price
        return f'Based on given conditions, this lamp cost € {colors.bold()}{colors.underline()}{monthly_costs:.2f}{colors.end()} each month.'

    def __str__(self) -> str:
    # Method to print info about created object
        return f"{colors.bold()}Power source data:{colors.end()}\n {colors.underline()}Capacity:{colors.end()} {self.capacity} Watts\n {colors.underline()}Power source connected:{colors.end()} {self.is_conected}"
