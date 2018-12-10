import requests
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(".", "delete")),
        logging.StreamHandler()
    ])

with open('ignored_gav.txt', 'r') as source:
	for line in source:
		line = line.strip("\n")
		group_id, artifact_id, artifact_type, version = line.split(":")
		url = "https://nx-ubs.murex.com/service/rest/beta/search?repository=temp-releases&group=" + group_id + "&name=" + artifact_id + "&version=" + version
		response = requests.get(url).json()
		
		
		if response['items'] :
			for item in response['items']:
				id = item['id']
				url_delete = "https://nx-ubs.murex.com/service/rest/beta/components/" + id
				logging.info("Deleting " + line + " with URL "+ url_delete)
				requests.delete(url_delete, auth=HTTPBasicAuth("deploy", "d3pl0y"))
				logging.info( "Deleted " + line)
		else :
			logging.info(url + " returned no items ")
#curl -X GET 'https://nx-ubs.murex.com/service/rest/beta/search?repository=temp-releases&group=actuate&name=rsse&version=10.0'
#curl -X DELETE -u deploy:d3pl0y 'https://nx-ubs.murex.com/service/rest/beta/components/dGVtcC1yZWxlYXNlczo0YjM3ODY1MzU5MWM2NzIyZGZiNWFlNDgzM2MzNGU3NA'