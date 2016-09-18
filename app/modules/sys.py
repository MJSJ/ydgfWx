# encoding: utf-8
from app.modules import base
import tornado.web
import logging as l

class sys(base):
    def render(self, template_name, **kwargs):
        super(sys, self).render('sys/'+template_name, **kwargs)

class SystemHandler(sys):
    '''
    yf: 系统后台首页
    '''
    @tornado.web.authenticated
    def get(self):
        self.render('system.html', active="none")

class LoginHandler(sys):
    '''
    yf: 后台登录
    '''
    def get(self):
        if self.current_user is None:
            self.render('login.html', error=None)
            return
        self.redirect('/sys')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        u = self.db.user(username=username, password=password).one()
        if u:
            self.set_secure_cookie('u', str(u), expires_days=30)
            self.redirect('/sys')
            return
        self.render('login.html', error='用户名或密码错误')

class GuessAddHandler(sys):
    '''
    yf: 竞猜管理
    '''
    def get(self):
        self.render('guess.add.html', active="guess-edit")

    def post(self):
        pass

class NotFoundHandler(sys):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/sys\">back</a>")

url_prefix = '/sys'

urls = [
    ('/?', SystemHandler),
    ('/login', LoginHandler),
    ('/guess/add', GuessAddHandler)
]