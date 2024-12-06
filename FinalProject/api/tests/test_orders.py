from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_id": 1,
        "customer_name": "John Doe",
        "order_date": "2023-01-01T00:00:00",
        "description": "Test order",
        "payment_type": "Credit Card",
        "promotion_key": None,
        "order_status": "Pending"
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order['customer_name'] == "John Doe"
    assert created_order['description'] == "Test order"
    assert created_order['order_date'] == "2023-01-01T00:00:00"
    assert created_order['payment_type'] == "Credit Card"
    assert created_order['promotion_key'] is None
    assert created_order['order_status'] == "Pending"
