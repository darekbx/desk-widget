from commonexception import CommonException
from credentials import Credentials
from store import Store
from secret import *

from StringIO import StringIO
import requests
import json

class JIRA:
	storePrefix = "jira"
	password = ""
	username = ""
	url = ""

	def execute(self, credentials):
		try:
			response = requests.get(self.url, auth=(self.username, credentials))
			if response.status_code != 200:
				raise Exception("Invalid response %s" % response.status_code)
			jsonResponse = response.json()
			return len(jsonResponse['issues'])

		except Exception as e:
			print e
			return CommonException(e.message)
		
	def checkForNewItems(self):
		credentials = Credentials()
		store = Store(self.storePrefix)
		jiraCredentials = credentials.decrypt(SALT, self.password)
		itemsCount = self.execute(jiraCredentials)

		if isinstance(itemsCount, CommonException):
			return itemsCount
		else:
			cache = store.load()
			if len(cache) == 0:
				cache = [0]
			store.save([itemsCount])
			diff = itemsCount - cache[0]
			return diff
