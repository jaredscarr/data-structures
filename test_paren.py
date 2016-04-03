"""Module to test paren matcher function."""


def test_balanced():
    """Assert parens are balanced."""
    from paren import match_parens
    parens = 'adf(((d)f)s)a'
    assert match_parens(parens) == 0


def test_open():
    """Assert paren are open."""
    from paren import match_parens
    parens = 'a(d(aef((aa)ad))'
    assert match_parens(parens) == 1


def test_borken():
    """Assert parens are broken."""
    from paren import match_parens
    parens = 'adf3))dadf)f(f(f(f'
    assert match_parens(parens) == -1

