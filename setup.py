from setuptools import setup

setup(
    name="finviz_api",
    description="A Finviz-backed screener for stock tickers.",
    install_requires=["beautifulsoup4", "requests"]
)
