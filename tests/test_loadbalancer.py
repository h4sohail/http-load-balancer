import pytest

from http import HTTPStatus

from src.loadbalancer import loadbalancer


@pytest.fixture
def client():
  with loadbalancer.test_client() as client:
    yield client


def test_host_routing_dogs(client):
  result = client.get("/", headers={"Host": "www.service-a.com"})
  assert b"This is the dogs application" in result.data


def test_host_routing_cats(client):
  result = client.get("/", headers={"Host": "www.service-b.com"})
  assert b"This is the cats application" in result.data


def test_host_routing_notfound(client):
  result = client.get("/", headers={"Host": "www.not-a-service.com"})
  assert b"Not Found" in result.data
  assert HTTPStatus.NOT_FOUND == result.status_code


def test_path_routing_dogs(client):
  result = client.get("/dogs")
  assert b"This is the dogs application" in result.data

  
def test_path_routing_cats(client):
  result = client.get("/cats")
  assert b"This is the cats application" in result.data


def test_path_routing_service_notfound(client):
  result = client.get("/not-a-service")
  assert b"Not Found" in result.data
  assert 404 == result.status_code