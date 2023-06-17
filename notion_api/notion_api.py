import requests

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

  def get_one_page(self, page_id):
    url = "{}pages/{}".format(self.api, page_id)
    response = requests.get(url, headers=self.headers)
    return response.json()

  def get_database(self, database_id):
    url = "{}databases/{}".format(self.api, database_id)
    response = requests.get(url, headers=self.headers)
    return response.json()

  def query_database(self, database_id):
    url = "{}databases/{}/query".format(self.api, database_id)
    response = requests.post(url, headers=self.headers)
    return response.json()
