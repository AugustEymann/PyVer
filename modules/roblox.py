import json,bs4,requests

class robloxUser():
	def __init__(self,id):
		self.id = id
	
	def getStatus(self):
		request = requests.get('https://roblox.com/users/' + self.id + '/profile')
		pageData = bs4.BeautifulSoup(request.text, features='html.parser')
		hiddenData = pageData.find('div', {'data-profileuserid' : self.id})
		return hiddenData['data-statustext']

	def getDescription(self):
		request = requests.get('https://roblox.com/users/' + self.id + '/profile')
		pageData = bs4.BeautifulSoup(request.text, features='html.parser')
		return pageData.find('span', {'class' : 'profile-about-content-text linkify'}).getText()

	def getImage(self, imageType):
		if str.lower(imageType) == 'headshot':
			return 'https://www.roblox.com/headshot-thumbnail/image?userId=' + self.id + '&width=420&height=420&format=png'
		elif str.lower(imageType) == 'bust':
			return 'https://www.roblox.com/bust-thumbnail/image?userId=' + self.id + '&width=420&height=420&format=png'
		else:
			return 'Select Headshot or Bust'