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
    assert wave("MeXiCaN wAvE") == [
        "Mexican wave",
        "mExican wave",
        "meXican wave",
        "mexIcan wave",
        "mexiCan wave",
        "mexicAn wave",
        "mexicaN wave",
        "mexican Wave",
        "mexican wAve",
        "mexican waVe",
        "mexican wavE",
    ]
