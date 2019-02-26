from commonexception import CommonException
from gmail import GmailInfo
from pocztaonet import PocztaOnetInfo
from jira import JIRA
from flag import Flag

import time

# TODO 
# type secret pin with buttons and display
# some animation / information / other ideas when widget is in idle state

class Widget:

    checkInterval = 10
    errors = []
    flag = None

    def __init__(self):
        self.flag = Flag()

    def run(self):
        self.flag.forceHideFlag()
        while True:
            print "Checking..."
            self.errors = []
            self.flag.hideFlag()

            self.notifyNew(self.checkGmail(), "gmail")
            self.notifyNew(self.checkPocztaOnet(), "pocztaonet")
            self.notifyNew(self.checkJIRA(), "jira")

            self.notifyError()
            self.flag.showFlag()

            time.sleep(self.checkInterval)

    def checkGmail(self):
        newMessages = GmailInfo().checkForNewMessages()
        if isinstance(newMessages, CommonException):
            self.errors.append(newMessages)
            return 0
        else:
            return newMessages

    def checkPocztaOnet(self):
        newMessages = PocztaOnetInfo().checkForNewMessages()
        if isinstance(newMessages, CommonException):
            self.errors.append(newMessages)
            return 0
        else:
            return newMessages

    def checkJIRA(self):
        newItems = JIRA().checkForNewItems()
        if isinstance(newItems, CommonException):
            self.errors.append(newItems)
            return 0
        else:
            return newItems

    def notifyNew(self, count, provider):
        if count <= 0:
            return False
        self.flag.updateFlag(True)
        # TODO: 
        # - refresh display
        print "%s: %s" % (provider, count)
        return True

    def notifyError(self):
        if len(self.errors) == 0:
            return False
        # TODO: 
        # - refresh display
        print "Errors: %s" % len(self.errors)
        return True

widget = Widget()
widget.run()