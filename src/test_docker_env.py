import os


def test_env_is_propagated_to_tests():
    assert os.environ["HARDCODED"] == "VALUE"
    assert "NOT_WHITELISTED" not in os.environ
    assert os.environ["WHITELISTED"] == "VALUE"
