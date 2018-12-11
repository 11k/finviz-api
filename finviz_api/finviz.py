from bs4 import BeautifulSoup
import requests

class Filter:
    def __init__(self, *args):
        self.filters = [filter.value for filter in list(args)]

    def for_query_string(self):
        """Returns a Finviz-ready string for use in a screener request."""
        return ",".join(self.filters)

def fetch_tickers(filters=None, sort=None):
    """
    Takes a list of filter enums and returns a list of matching tickers.

    Parameters
    ----------
    filters : list
        A list of filter enums from the `finviz_api.filters` module.

    Returns
    -------
    list
        A list of ticker strings.
    """
    BASE_URL = "https://finviz.com/screener.ashx"
    API_VERSION = 111

    filter = Filter(filters)
    response = requests.get(
        BASE_URL,
        params={
            "v": API_VERSION,
            "f": filter.for_query_string(),
            "o": sort
        }
    )
    response.raise_for_status()

    return _parse_tickers(response.text)

def _parse_tickers(html):
    """Extracts tickers from a Finviz screener HTML page."""
    TICKER_ELEMENT_CLASS = "screener-link-primary"

    soup = BeautifulSoup(html, "html.parser") 
    return [e.getText() for e in soup.find_all(class_=TICKER_ELEMENT_CLASS)]

