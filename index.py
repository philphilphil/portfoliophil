import cherrypy, os, glob, HelpClasses

class PortfolioPhil(object):

	def template(self, body):

		#Open Layout
		f = open('./layout.html')
		layoutHtml = f.read()

		return layoutHtml.replace("${content}", body)

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

	def gallery(self):
		return self.template("Hello gallery!")
	gallery.exposed = True

	def contact(self):
		return self.template("Hello contact!")
	contact.exposed = True

#cherrypy.config.update('conf/portfoliophil.config')
cherrypy.quickstart(PortfolioPhil(), '/', 'portfoliophil.config')

