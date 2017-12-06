# salt-sumo-events
Salt-Api events streamed over HTTP(S) forwarded to a SumoLogic hosted appender.

## WARNING  SALT EVENTS CAN CONTAIN SENSITIVE INFORMATION  WARNING

## Local development/run the container

### Required software
* VirtualBox
* Vagrant
* Python (for local dev only)

### Running with Vagrant
In order to run this application you will need to update vagrant/env_file.txt setting the two variables to actual real values for your setup. 
Once these values are set, you can run vagrant up to build the docker host, and start the container which will run the python program.

### Running with python

	usage: main.py [-h] [--ignore_ssl] [--print_only] [--quiet]
	               salt_api_event_url sumologic_hosted_collector_url
	
	Salt-Api event forwarding to SumoLogic
	
	positional arguments:
	  salt_api_event_url    URL for your Salt API event end point
	  sumologic_hosted_collector_url
	                        URL for your sumologic hosted collector
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --ignore_ssl          Ignore any SSL complaints with HTTPS connections
	  --print_only          Do not send anything to sumologic, only print output
	                        to console
	  --quiet               Do not print output to console
