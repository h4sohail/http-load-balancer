import random
import requests
import yaml
import os
import sys

from http import HTTPStatus
from flask import Flask, request

loadbalancer = Flask(__name__)


def load_configuration(path):
  with open(path) as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
  return config

try:
  config = load_configuration("loadbalancer.yml")
except FileNotFoundError:
  print("Please provide a configuration file")
  sys.exit(-1)


@loadbalancer.route("/")
def host_router():
  """[summary]

  Returns:
      [type]: [description]
  """
  host_header = request.headers["Host"]
  for entry in config["hosts"]:
    if host_header == entry["host"]:
      response = requests.get(f"http://{random.choice(entry['servers'])}")
      return response.content, response.status_code
  else:
    return "Not Found", HTTPStatus.NOT_FOUND


@loadbalancer.route("/<path>")
def path_router(path):
  """[summary]

  Returns:
      [type]: [description]
  """
  for entry in config["paths"]:
    if ("/" + path) == entry["path"]:
      response = requests.get(f"http://{random.choice(entry['servers'])}")
      return response.content, response.status_code

  return "Not Found", HTTPStatus.NOT_FOUND