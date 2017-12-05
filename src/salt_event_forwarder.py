class SaltEventForwarder:
  
  def __init__(self, salt_api_event_url, sumo_hosted_collector):
    self.salt_api_event_url = salt_api_event_url
    self.sumo_hosted_collector = sumo_hosted_collector
  
  def run(self):
    print ("run")
