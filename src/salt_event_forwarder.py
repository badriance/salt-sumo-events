import json
import requests

class SaltEventForwarder:
  
  def __init__(self, salt_api_event_url, sumo_hosted_collector, ssl_no_verify, quiet_mode, print_only):
    self.salt_api_event_url = salt_api_event_url
    self.sumo_hosted_collector = sumo_hosted_collector
    self.ssl_no_verify = ssl_no_verify
    self.skip_logging_tags = ["salt/auth"]
    self.quiet = quiet_mode
    self.print_only = print_only

  def run(self):
    self.print_message("Starting request to stream events from salt...")
    s = requests.Session()
    if self.ssl_no_verify:
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
          if not self.print_only:
            requests.post(self.sumo_hosted_collector, data = {'tag': tag, 'data': data})
          self.print_message("{0}Posted {1} to sumo with {2}\n\n".format("Would Have " if self.print_only else "",  tag, data))
          tag = ""
    except KeyboardInterrupt:
      self.print_message("Interrupt signal received. Exiting.")

  def streaming(self, session):
    headers = {'connection': 'keep-alive', 'content-type': 'application/json', 'transfer-encoding': 'chunked'}
    request = requests.Request('GET', self.salt_api_event_url, headers = headers).prepare()
    response = session.send(request, stream = True)
    json_string = ''
    for line in response.iter_lines():
      if line:
        yield line.strip()

  def print_message(self, message):
    if not self.quiet:
      print(message)