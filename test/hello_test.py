


from gspread_models.hello import Hello


def test_hello():
    h = Hello()
    h.announce("NYC")
    h.departing("NYC")
