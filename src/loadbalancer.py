import random
import requests

from http import HTTPStatus
from flask import Flask, request

loadbalancer = Flask(__name__)

SERVICE_A = ["localhost:8081", "localhost:8082"]
SERVICE_B = ["localhost:9081", "localhost:9082"]


@loadbalancer.route("/")
def router():
  host_header = request.headers["Host"]
  
  if host_header == "www.service-a.com":
    response = requests.get(f"http://{random.choice(SERVICE_A)}")
    return response.content, response.status_code
  
  elif host_header == "www.service-b.com":
    response = requests.get(f"http://{random.choice(SERVICE_B)}")
    return response.content, response.status_code
  
  else:
    return "Not Found", HTTPStatus.NOT_FOUND