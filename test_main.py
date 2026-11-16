
import pytest

from main import calcular_area


def test_calcular_area():
    resultado = calcular_area(5, 4)
    assert resultado == 20


def test_area_decimal():
    resultado = calcular_area(2.5, 4)
    assert resultado == pytest.approx(10.0)


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 4)


def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(5, 0)
