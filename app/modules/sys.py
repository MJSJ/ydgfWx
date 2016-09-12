# encoding: utf-8
from app.modules import base
import logging as l

class sys(base):
    def render(self, template_name, **kwargs):
        super(sys, self).render(template_name, **kwargs)

class SystemHandler(sys):
    '''
    yf: 系统后台首页
    '''
    def get(self):
        u = self.get_current_user()
        if u is None:
            self.redirect('/sys/login')
        else:
            self.render('sys.html')

class LoginHandler(sys):
    '''
    yf: 后台登录
    '''
    def get(self):
        pass

class NotFoundHandler(sys):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = '/sys'

urls = [
    ('/?', SystemHandler),
    ('/login', LoginHandler)
]