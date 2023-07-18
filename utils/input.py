import re

float_regex = r"^\s*[+-]?\s*(\d+\s*\.?\s*\d*|\d*\s*\.?\s*\d+)\s*$"


def convert_expression(expression: str) -> str:
    expression = expression.replace("^", "**")
    return expression


def validate_expression(expr: str) -> str | None:
    if re.match(r"^.*[a-wy-zA-Z].*$", expr):
        return "You are only allowed to use the variable 'x'"

    try:
        x = 0
        y = eval(convert_expression(expr)) 
        if type(y) != int and type(y) != float:
            raise Exception()
    except (ZeroDivisionError,):
        pass
    except:
        return expr


def validate_x_limits(x_start: str, x_end: str) -> str | None:
    if not re.match(float_regex, x_start):
        return "Start value of x must be a valid number"

    if not re.match(float_regex, x_end):
        return "End value of x must be a valid number"

    if float(x_start) > float(x_end):
        return "Start value of x can't be greater than the end value"
