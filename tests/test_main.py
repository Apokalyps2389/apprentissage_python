import pytest

from programme_se_presenter.main import greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
