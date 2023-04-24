from src.traffic_lights import update_traffic_lights


def test_update_traffic_lights():
    assert update_traffic_lights("green") == "yellow"
    assert update_traffic_lights("yellow") == "red"
    assert update_traffic_lights("red") == "green"
