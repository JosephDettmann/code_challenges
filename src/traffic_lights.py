def update_traffic_lights(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


    if __name__ == "__main__":
        update_traffic_lights()
        