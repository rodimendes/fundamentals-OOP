from elements.power_source import PowerSource
from elements import colors

power = PowerSource(capacity=100, connected=True)


def test_energy_supply_type():
    assert power.capacity == 100
    assert power.is_conected == True

def test_check_energy_supply_type():
    assert power.energy_supply() == f'{colors.yellow()}System connected to a limited source.{colors.end()}'

def test_estimate_monthly_consuption_using_4h_per_day():
    assert power.estimate_monthly_consumption(100, 4, 0.15) == f'Based on given conditions, this lamp cost € {colors.bold()}{colors.underline()}1.80{colors.end()} each month.'
