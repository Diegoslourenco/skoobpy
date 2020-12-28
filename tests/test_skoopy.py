# Tests for the skoobpy module

import pytest
from skoobpy import get_all_books
from skoobpy import save_desired_csv

user_id = 1380619

@pytest.fixture
def create_skoopy_csv(user_id):
    return save_desired_csv(get_all_books(user_id))

# Tests
def test_skoopy_csv(user_id):

    create_skoopy_csv(user_id)

    file = open(f'book_{user_id}.csv')
    content = csv.reader(file)
    count = sum(1 for row in content)

    assert count == 467





