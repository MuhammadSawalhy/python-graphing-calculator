from utils.input import *


def test_convert_expression():
    expr = "asdf9834798.asdfklj0 w389472 9834= - 234=234"
    assert convert_expression(expr) == expr
    assert convert_expression(
        "2*x^3 + 4*x^2 - 7*x + 5") == "2*x**3 + 4*x**2 - 7*x + 5"
    assert convert_expression("x^3 + 2*x^2 + x") == "x**3 + 2*x**2 + x"
    assert convert_expression("3*x^2") == "3*x**2"


def test_validate_expression():
    # Valid expressions
    assert validate_expression("2*x^3 + 4*x^2 - 7*x + 5") is None
    assert validate_expression("3*x^2") is None
    assert validate_expression("x^3 + 2*x^2 + x") is None
    assert validate_expression("2 + 3") is None
    assert validate_expression("1/0") is None
    assert validate_expression("x + 1/x") is None
    # Invalid expressions
    assert validate_expression(
        "2*x + 3*y") == "You are only allowed to use the variable 'x'"


def test_validate_x_limits():
    # Valid x limits
    assert validate_x_limits('1.0', '2.0') is None
    assert validate_x_limits('1.0', '1.0') is None
    assert validate_x_limits('0', '1.0') is None
    assert validate_x_limits('-10', '10') is None
    # Invalid x limits
    assert type(validate_x_limits('-', '10')) is str
    assert type(validate_x_limits('2.0', '1.0')) is str
    assert type(validate_x_limits('a', '2.0')) is str
    assert type(validate_x_limits('1.0', 'b')) is str
