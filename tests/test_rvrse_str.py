from src.rvrse_str import rvrse_str


def test_rvrse_str():
    assert rvrse_str("tree") == "eert"
    assert rvrse_str("children") == "nerdlihc"
    assert rvrse_str("hello") == "olleh"
    assert rvrse_str("antidisestablishmentarianism") == "msinairatnemhsilbatsesiditna"
    assert rvrse_str("hippocampus") == "supmacoppih"
