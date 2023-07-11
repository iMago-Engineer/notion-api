import requests
import glob
import json

class Notion:
  def __init__(self, api_key) -> None:
    self.api_key = api_key
    self.headers = {
      "Accept": "application/json",
      "Notion-Version": "2022-06-28",
      "Content-Type": "application/json",
      "Authorization": "Bearer " + api_key
    }
    self.api = "https://api.notion.com/v1/"
    if len(glob.glob(".notion.cache")) != 0:
      try:
        self.cache = json.loads(open(".notion.cache", "r").read())
      except:
        print("Error: .notion.cache is corrupted. Please delete it and try again.")
        self.initialize_cache()
    else:
      self.initialize_cache()

  def initialize_cache(self):
    self.cache = dict()
    self.cache["pages"] = dict()
    self.cache["databases"] = dict()
    self.cache["blocks"] = dict()

  def save_cache(self):
    open(".notion.cache", "w").write(json.dumps(self.cache))

  def get_one_page(self, page_id):
    if page_id in self.cache["pages"].keys():
      return self.cache["pages"][page_id]
    url = "{}pages/{}".format(self.api, page_id)
    response = requests.get(url, headers=self.headers)
    self.cache["pages"][page_id] = response.json()
    self.save_cache()
    return response.json()

  def get_one_block(self, block_id):
    if block_id in self.cache["blocks"].keys():
      return self.cache["blocks"][block_id]
    url = "{}blocks/{}".format(self.api, block_id)
    response = requests.get(url, headers=self.headers)
    self.cache["blocks"][block_id] = response.json()
    self.save_cache()
    return response.json()

  def get_block_children(self, block_id):
    url = "{}blocks/{}/children?page_size=100".format(self.api, block_id)
    response = requests.get(url, headers=self.headers)
    return response.json()

  def get_database(self, database_id):
    if page_id in self.cache["databases"].keys():
      return self.cache["databases"][database_id]
    url = "{}databases/{}".format(self.api, database_id)
    response = requests.get(url, headers=self.headers)
    self.cache["databases"][database_id] = response.json()
    self.save_cache()
    return response.json()

  def query_database(self, database_id):
    url = "{}databases/{}/query".format(self.api, database_id)
    response = requests.post(url, headers=self.headers)
    return response.json()

