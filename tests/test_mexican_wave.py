from src.mexican_wave import wave


def test_wave():
    assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("joseph") == [
        "Joseph",
        "jOseph",
        "joSeph",
        "josEph",
        "josePh",
        "josepH",
    ]
    assert wave("ely") == ["Ely", "eLy", "elY"]
    assert wave("sempiternal") == [
        "Sempiternal",
        "sEmpiternal",
        "seMpiternal",
        "semPiternal",
        "sempIternal",
        "sempiTernal",
        "sempitErnal",
        "sempiteRnal",
        "sempiterNal",
        "sempiternAl",
        "sempiternaL",
    ]
    assert wave("cheat") == ["Cheat", "cHeat", "chEat", "cheAt", "cheaT"]
