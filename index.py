import cherrypy, os

class PortfolioPhil(object):

	def template(self, body):
		f = open('layout.html')
		layoutHtml = f.read()

		return layoutHtml.replace("${content}", body)
		
		#return "<html><head><title>PortfolioPhil</title></head><body><h3>PortfolioPhil Alpha 0.1</h3>"+body+"</body></html>"

	def index(self):
		return self.template("Hello PortfolioPhil!")
	index.exposed = True

	def blog(self):
		return self.template("blog")
	blog.exposed = True

	def gallery(self):
		return self.template("Hello gallery!")
	gallery.exposed = True

	def contact(self):
		return self.template("Hello contact!")
	contact.exposed = True

#cherrypy.config.update('conf/portfoliophil.config')
cherrypy.quickstart(PortfolioPhil(), '/', 'portfoliophil.config')