"""Module to test paren matcher function."""


def test_balanced():
    """Assert parens are balanced."""
    from paren import match_parens
    parens = '((()))'
    assert match_parens(parens) == 0


def test_open():
    """Assert paren are open."""
    from paren import match_parens
    parens = '(((()))'
    assert match_parens(parens) == 1


def test_borken():
    """Assert parens are broken."""
    from paren import match_parens
    parens = ')))((('
    assert match_parens(parens) == -1

