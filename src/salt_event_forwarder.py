import json
import requests

class SaltEventForwarder:
  
  def __init__(self, salt_api_event_url, sumo_hosted_collector, ssl_no_verify):
    self.salt_api_event_url = salt_api_event_url
    self.sumo_hosted_collector = sumo_hosted_collector
    self.ssl_no_verify = ssl_no_verify
    self.skip_logging_tags = ["salt/auth"]

  def run(self):
    print("Starting request to stream events from salt...")
    s = requests.Session()
    if (self.ssl_no_verify):
      s.verify = False
    tag = ""
    data = ""
    try:
      for line in self.streaming(s):
        if line.startswith("tag:"):
          if line.replace("tag:", "").strip() in self.skip_logging_tags:
            continue
          tag = line[4:].strip()
        elif tag and line.startswith("data:"):
          data = line[5:].strip()
          requests.post(self.sumo_hosted_collector, data = {'tag': tag, 'data': data})
          print("Posted {0} to sumo with {1}\n\n".format(tag, data))
          tag = ""
    except KeyboardInterrupt:
      print "Interrupt signal received. Exiting."

  def streaming(self, session):
    headers = {'connection': 'keep-alive', 'content-type': 'application/json', 'transfer-encoding': 'chunked'}
    request = requests.Request('GET', self.salt_api_event_url, headers = headers).prepare()
    response = session.send(request, stream = True)
    json_string = ''
    for line in response.iter_lines():
      if line:
        yield line.strip()

