import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.account_dao import AccountDAO
from models.account import Account

# Просто тестовая база с другим именем
TEST_DB = "test_db_simple.db"

def test_create_account():
    dao = AccountDAO(db_name=TEST_DB)
    acc = Account(10, 1, "Test Account", 1000.0, "KGS")
    dao.create_account(acc)
    result = dao.get_account_by_id(10)
    assert result is not None
    assert result.account_name == "Test Account"

def test_update_account():
    dao = AccountDAO(db_name=TEST_DB)
    acc = dao.get_account_by_id(10)
    acc.balance = 2000.0
    dao.update_account(acc)
    updated = dao.get_account_by_id(10)
    assert updated.balance == 2000.0

def test_delete_account():
    dao = AccountDAO(db_name=TEST_DB)
    dao.delete_account(10)
    assert dao.get_account_by_id(10) is None
