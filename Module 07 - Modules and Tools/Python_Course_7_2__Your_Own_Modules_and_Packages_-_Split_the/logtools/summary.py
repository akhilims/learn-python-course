__all__ = ["headline"]

def headline(errors):
    return f"{errors} errors today"

def _tidy(text):
    return text.strip()
