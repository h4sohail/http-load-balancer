import pytest

from http import HTTPStatus

from src.loadbalancer import loadbalancer


@pytest.fixture
def client():
  with loadbalancer.test_client() as client:
    yield client


def test_host_routing_dashboard(client):
  result = client.get("/", headers={"Host": "www.service-a.com"})
  assert b"This is the dashboard application" in result.data


def test_host_routing_store(client):
  result = client.get("/", headers={"Host": "www.service-b.com"})
  assert b"This is the store application" in result.data


def test_host_routing_notfound(client):
  result = client.get("/", headers={"Host": "www.not-a-service.com"})
  assert b"Not Found" in result.data
  assert HTTPStatus.NOT_FOUND == result.status_code