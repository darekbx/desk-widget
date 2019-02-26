import os
import pickle

class Store:

	preferencesDir = "preferences"
	preferencesFileSufix = ".dat"
	prefix = None

	def __init__(self, prefix):
		self.prefix = prefix

	def save(self, value):
		if not os.path.exists(self.preferencesDir):
			os.makedirs(self.preferencesDir)
		fw = open(self.getPath(), 'wb')
		pickle.dump(value, fw)
		fw.close()

	def load(self):
		if not os.path.exists(self.preferencesDir):
			return []
		if not os.path.exists(self.getPath()):
			return []
		fd = open(self.getPath(), 'rb')
		return pickle.load(fd)

	def getPath(self):
		return os.path.join(self.preferencesDir, self.prefix + self.preferencesFileSufix)