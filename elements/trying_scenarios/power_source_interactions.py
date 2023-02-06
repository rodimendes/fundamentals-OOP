from elements.power_source import PowerSource

# Creating a new object from PowerSource class.
# If you want to create an ilimited source,
# pass 0 into ´capacity´ parameter.
my_source = PowerSource(capacity=100)

# Print its information.
# For now, nothing is connected to the source.
print(my_source)

# Checking the energy supply type.
print(my_source.energy_supply())

# You can also estimate your monthly consumption,
# based on declared conditions.
print(my_source.estimate_monthly_consumption(13, 1, 0.15))
