from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..models import resources as model
from ..controllers import resources as controller

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_resource(db_session):
    resource_data = {
        "item": "Tomato",
        "amount": 100
    }

    resource_object = model.Resource(**resource_data)

    created_resource = controller.create(db_session, resource_object)

    assert created_resource is not None
    assert created_resource.item == "Tomato"
    assert created_resource.amount == 100

def test_read_all_resources(db_session):
    db_session.query(model.Resource).all.return_value = [
        model.Resource(id=1, item="Tomato", amount=100),
        model.Resource(id=2, item="Lettuce", amount=50)
    ]

    resources = controller.read_all(db_session)

    assert len(resources) == 2
    assert resources[0].item == "Tomato"
    assert resources[0].amount == 100
    assert resources[1].item == "Lettuce"
    assert resources[1].amount == 50