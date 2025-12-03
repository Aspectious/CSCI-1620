import pytest;

def test_func():
    with pytest.raises(TypeError):
        print(int("poo"))
