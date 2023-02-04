from src.messagers.messagers import AbstractNotificator
import pytest


def test_abstract_messager():
    with pytest.raises(TypeError):
        example_notificator = AbstractNotificator()