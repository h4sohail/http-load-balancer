import random
import requests

from http import HTTPStatus
from flask import Flask, request

loadbalancer = Flask(__name__)

DASHBOARD_SERVERS = ["localhost:8081", "localhost:8082"]
STORE_SERVERS = ["localhost:9081", "localhost:9082"]


@loadbalancer.route("/")
def router():
  host_header = request.headers["Host"]
  
  if host_header == "www.dashboard.store.com":
    response = requests.get(f"http://{random.choice(DASHBOARD_SERVERS)}")
    return response.content, response.status_code
  
  elif host_header == "www.store.com":
    response = requests.get(f"http://{random.choice(STORE_SERVERS)}")
    return response.content, response.status_code
  
  else:
    return "Not Found", HTTPStatus.NOT_FOUND