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