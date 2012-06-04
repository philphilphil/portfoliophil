import cherrypy, os, glob, HelpClasses, Image

class PortfolioPhil(object):

	def GetGalleryLinks(self):
		outputHtml = ""
		for dirname, dirnames, filenames in os.walk('./content_portfolio'):
			for subdirname in dirnames:
				outputHtml += "<a href='gallery?folder=" + subdirname + "'>" + subdirname + "</a><br />"
		return outputHtml
	GetGalleryLinks.exposed = False

	def template(self, body):

		#Open Layout
		f = open('./layout.html')
		layoutHtml = f.read()
		layoutHtml = layoutHtml.replace("${content}", body)
		layoutHtml = layoutHtml.replace("${gallery}", self.GetGalleryLinks())
		return layoutHtml

	def index(self):
		return self.template("Hello PortfolioPhil!")
	index.exposed = True

	def blog(self):
		#Load all files in content_blog folder and output them.
		#For Later: Paging, Sorting
		blogEntrys = []
		output = ""

		#Loop throgh all files
		for files in glob.glob("./content_blog/*.txt"):
			#Read file and create a BlogEntry Help Object
			f = open(files)
			entry = HelpClasses.BlogEntry(f.readlines())
			#Append to list
			blogEntrys.append(entry)


		#ToDo: Sort Blog Entrys

		#Output entrys
		for entry in blogEntrys:
			output += entry.getBlogEntryHTML()
			output += "<br /><br />"

		return self.template(output)
	blog.exposed = True

	def gallery(self, folder):
		outputHtml = ""

		#Get the image files from the directory, only jpg right now
		for files in glob.glob("./content_portfolio/" + folder + "/*.jpg"):
			outputHtml += "<img src='" + files + "'>"

		return self.template(outputHtml)
	gallery.exposed = True

	def contact(self):
		return self.template("Hello contact!")
	contact.exposed = True

#cherrypy.config.update('conf/portfoliophil.config')
cherrypy.quickstart(PortfolioPhil(), '/', 'portfoliophil.config')

