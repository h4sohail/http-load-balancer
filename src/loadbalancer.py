import random
import requests

from http import HTTPStatus
from flask import Flask, request

loadbalancer = Flask(__name__)

DOG_SERVERS = ["localhost:8081", "localhost:8082"]
CAT_SERVERS = ["localhost:9081", "localhost:9082"]


@loadbalancer.route("/")
def router():
  """[summary]

  Returns:
      [type]: [description]
  """
  host_header = request.headers["Host"]
  
  if host_header == "www.service-a.com":
    response = requests.get(f"http://{random.choice(DOG_SERVERS)}")
    return response.content, response.status_code
  
  elif host_header == "www.service-b.com":
    response = requests.get(f"http://{random.choice(CAT_SERVERS)}")
    return response.content, response.status_code
  
  else:
    return "Not Found", HTTPStatus.NOT_FOUND


@loadbalancer.route("/dogs")
def dogs():
  """[summary]

  Returns:
      [type]: [description]
  """
  response = requests.get(f"http://{random.choice(DOG_SERVERS)}")
  return response.content, response.status_code


@loadbalancer.route("/cats")
def cats():
  """[summary]

  Returns:
      [type]: [description]
  """
  response = requests.get(f"http://{random.choice(CAT_SERVERS)}")
  return response.content, response.status_code
