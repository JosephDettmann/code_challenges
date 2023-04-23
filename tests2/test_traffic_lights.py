from src.traffic_lights import update_traffic_lights


def test_traffic_lights():
    current = "red"
    if current == "green":
        assert update_traffic_lights(current) == "yellow"
    if current == "yellow":
        assert update_traffic_lights(current) == "red"
    if current == "red":
        assert update_traffic_lights(current) == "green"
    