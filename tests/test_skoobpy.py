# Tests for the skoobpy module

# standard import
import csv

# third party import
import pytest

# skoobpy import
from skoobpy import *

@pytest.fixture
def total_books():
    user_id = 1380619
    return get_all_books(user_id)
    
@pytest.fixture
def total_desired_books():
    user_id = 1380619
    all_books = get_all_books(user_id)
    return filter_desired_books(all_books)

@pytest.fixture
def total_currently_reading_books():
    user_id = 1380619
    all_books = get_all_books(user_id)
    return filter_currently_reading_books(all_books)

# Tests
def test_total_books(total_books):
    assert len(total_books) == 619

def test_total_desired_books(total_desired_books):
    assert len(total_desired_books) == 466

def test_total_currently_reading_books(total_currently_reading_books):
    assert len(total_currently_reading_books) == 3






