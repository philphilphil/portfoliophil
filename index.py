import cherrypy, os, glob, HelpClasses
from PIL import Image
import EXIF

class PortfolioPhil(object):

	#Unexposed Help Class
	def GetGalleryLinks(self):
		outputHtml = ""
		for dirname, dirnames, filenames in os.walk('./content_portfolio'):
			for subdirname in dirnames:
				outputHtml += "<a href='gallery?folder=" + subdirname + "'>" + subdirname + "</a><br />"
		return outputHtml
	GetGalleryLinks.exposed = False

	#Unexposed Help Class
	def CreateThumbnail(self, file):
		im = Image.open(file)
		# don't save if thumbnail already exists
		if not file.endswith("_thumb.jpg"):
			# convert to thumbnail image
			im.thumbnail((200, 200), Image.ANTIALIAS)

			# prefix thumbnail file and save
			im.save(file + "_thumb.jpg", "JPEG")
			return
	CreateThumbnail.exposed = False
	
	#Checks if there are thumbnails to create and if yes it creates them
	def CreateThumbnailsOutOfThumbOrdner(self):
		
		#Get the image files from the directory, only jpg right now
		for files in glob.glob("./createThumbnails/*.jpg"):
			self.CreateThumbnail(files)
		
			if  not files.endswith("_thumb.jpg"):
				continue;
		
	CreateThumbnailsOutOfThumbOrdner.exposed = False

	def template(self, body):

		#Open Layout
		f = open('./layout.html')
		layoutHtml = f.read()
		layoutHtml = layoutHtml.replace("${content}", body)
		layoutHtml = layoutHtml.replace("${gallery}", self.GetGalleryLinks())
		return layoutHtml

	def index(self):
		
		self.CreateThumbnailsOutOfThumbOrdner()
		
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
		outputHtml = "<div class='imageRow'>"

		#Get the image files from the directory, only jpg right now
		for files in glob.glob("./content_portfolio/" + folder + "/*.jpg"):

			if  not files.endswith("_thumb.jpg"):
				continue;

			#f = open(files.replace("_thumb.jpg",""), 'rb')
			#tags = EXIF.process_file(f, strict=True)
			#for tag in tags.keys():
			#	print ("Key:"+ tag + " data: " + str(tags[tag]))

			outputHtml += "<div class='single'>"
			outputHtml += "<a href='" + files.replace("_thumb.jpg","") + "' rel='lightbox[gallery]' title='"+os.path.basename(files).replace(".jpg_thumb.jpg","")+"'><img src='" + files + "'></a>"
			outputHtml +="</div>"

		outputHtml += "</div>"
		return self.template(outputHtml)
	gallery.exposed = True

	def contact(self):
		return self.template("Hello contact!")
	contact.exposed = True

#cherrypy.config.update('conf/portfoliophil.config')
cherrypy.quickstart(PortfolioPhil(), '/', 'portfoliophil.config')