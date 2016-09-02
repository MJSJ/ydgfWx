# encoding: utf-8
from app.modules import base
import logging as l

class main(base):
    def render(self, template_name, **kwargs):
        super(main, self).render(template_name, **kwargs)

class MainHandler(main):
    '''
    yf: 首页
    '''
    def get(self):
        self.write("None")

class NotFoundHandler(main):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = ''

urls = [
    ('/?', MainHandler)
]