import pytest

from main import BooksCollector

@pytest.fixture
def collector(self):
    return BooksCollector()