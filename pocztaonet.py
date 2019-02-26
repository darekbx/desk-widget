from commonexception import CommonException
from credentials import Credentials
from store import Store
from secret import *

import imaplib

class PocztaOnetInfo:
	storePrefix = "pocztaonet"
	imapHost = "imap.poczta.onet.pl"
	username = ""
	password = ""

	def getUnseen(self, credentials):
		try:
			mail = imaplib.IMAP4_SSL(self.imapHost)
			mail.login(self.username, credentials)
			mail.select('inbox')

			typ, messageIDs = mail.search(None, "UNSEEN")
			messageIDsString = str(messageIDs[0])
			return messageIDsString.split(" ")
		except Exception as e:
			print e
			return CommonException(e.message)

	def checkForNewMessages(self):
		credentials = Credentials()
		store = Store(self.storePrefix)
		onetCredentials = credentials.decrypt(SALT, self.password)
		unseen = self.getUnseen(onetCredentials)

		if isinstance(unseen, CommonException):
			return unseen
		else:
			cache = store.load()
			store.save(unseen)
			diff = len(unseen) - len(cache)
			return diff
