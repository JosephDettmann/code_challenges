from src.wide_mouthed_frog import mouth_size


def test_mouth_size():
    assert mouth_size("AlLiGaToR") == "small"
    assert mouth_size("LiOn") == "wide"
    assert mouth_size("MuShrOOm") == "wide"
    assert mouth_size("tUnA") == "wide"
    assert mouth_size("alligator") == "small"
    assert mouth_size("SmAlLeR tHaN aLlIgAtOr") == "wide"
