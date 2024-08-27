def foo():
    return 42

def str_to_int(s:str | float) -> int:
    try:
        if isinstance(s, str) and "." in s:
            return str_to_int(float(s))
        return int(s)
    except ValueError:
        return None