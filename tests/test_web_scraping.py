from web_scraping import __version__

from web_scraping.scraper import get_citations_needed_report, get_citations_needed_count

def test_version():
    assert __version__ == '0.1.0'


def test_length():
    expected = 5
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Petra')
    assert expected == actual

def test_preceding_passage():

    expected = open("test.txt", "r")
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/Petra')

    assert expected.read() == actual