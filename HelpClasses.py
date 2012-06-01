class BlogEntry(object):

	def __init__(self, content):
		self.buildBlogEntry(content)

	#Build Blog Entry
	def buildBlogEntry(self, fileContent = []):
		self.title = fileContent[0][6:]
		self.date = fileContent[1][5:]
		self.content = self.buildContent(fileContent)

	def buildContent(self, fileContent = []):
		skipFirst = 0
		content = ""

		#Skip first lines and build content
		for lines in fileContent:
			if skipFirst > 2:
				content += lines
			skipFirst += 1
	
		return content

	def getBlogEntryHTML(self):
		output = "<span style='font-size: 20px'><b>" + self.title + "</b></span> <span style='font-size: 10px'>" + self.date + "</span>"
		output += "<br />" + self.content

		return output