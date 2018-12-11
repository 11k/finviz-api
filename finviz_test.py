import unittest

from finviz_api import finviz
import finviz_api.filters as ff

class FilterTest(unittest.TestCase):
    def setUp(self):
        self.random_filters = [
            ff.MarketCap.OVER_300_MIL,
            ff.Price.UNDER_20
        ]

    def test_query_string(self):
        filter = finviz.Filter(self.random_filters)
        joined_filters = ",".join([f.value for f in self.random_filters])
        self.assertEqual(filter.for_query_string(), joined_filters)

    def test_without_filters(self):
        filter = finviz.Filter()
        self.assertEqual(filter.for_query_string(), "")

class FinvizTest(unittest.TestCase):
    def setUp(self):
        FINVIZ_SAMPLE_FILE_NAME = "finviz_sample_response.html"

        with open(FINVIZ_SAMPLE_FILE_NAME, "r") as file:
            self.sample_response = file.read()

        self.tickers_in_sample = [
            "A",    "AA",   "AAAU", "AABA", "AAC",
            "AADR", "AAL",  "AAMC", "AAME", "AAN",
            "AAOI", "AAON", "AAP",  "AAPL", "AAT",
            "AAU",  "AAWW", "AAXJ", "AAXN", "AB"
        ]

    def test_parse_tickers(self): 
        parsed_tickers = finviz._parse_tickers(self.sample_response)
        self.assertEqual(parsed_tickers, self.tickers_in_sample)

class SortTest(unittest.TestCase):
    def setUp(self):
        self.change_sort = ff.Sort.CHANGE

    def test_ascending(self):
        change_ascending = "change"
        self.assertEqual(self.change_sort.asc(), change_ascending)

    def test_descending(self):
        change_descending = "-change"
        self.assertEqual(self.change_sort.desc(), change_descending)

if __name__ == "__main__":
    unittest.main()

