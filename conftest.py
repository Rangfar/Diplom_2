import pytest
from functions.user import User
from functions.order import Order

@pytest.fixture
def user():
    user = User()
    yield user
    if hasattr(user, "token"):
        user.delete_user()

@pytest.fixture
def order():
    order = Order()
    return order