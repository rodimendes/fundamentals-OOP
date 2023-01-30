from elements.lamp import Lamp

def test_creating_lamp():
    test_lamp = Lamp(110, 'E-14', 60)
    assert test_lamp.voltage == 110
    assert test_lamp.socket == 'E-14'
    assert test_lamp.wattage == 60
