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
            self.set_secure_cookie('u', str(u.id), expires_days=30)
            self.redirect('/sys')
            return
        self.render('login.html', error='用户名或密码错误')

class GuessListHandler(sys):
    '''
    yf: 竞猜列表
    '''
    @tornado.web.authenticated
    def get(self, p=0):
        list = self.db.guess()[p: 10].object_list
        for item in list:
            item['cols'] = item['cols'].split('|')
        self.render('guess.list.html', guess=list, active="guess-list")

class GuessAddHandler(sys):
    '''
    yf: 竞猜管理
    '''
    @tornado.web.authenticated
    def get(self):
        self.render('guess.add.html', active="guess-edit")

    def post(self):
        dat = self.json_decode(self.request.body)
        data = {
            'title': dat['title'],
            'cols': dat['cols'],
            'key': dat['key'],
            'state': dat['state'],
            'expires': dat['expires'],
            'score': dat['score'],
            'reward_score': dat['reward_score'],
            'user_id': self.current_user
        }
        if 'id' in dat:
            data['id'] = dat['id']
            self.db.guess(id=data['id']).update(**data)
            self.write({'status': 1})
            return
        else:
            new_guess = self.db.guess.add(**data)
            if new_guess:
                self.write({'status': 1})
                return
        self.write({'status': 0})

class GuessEditHandler(sys):
    '''
    yf: 竞猜编辑
    '''
    @tornado.web.authenticated
    def get(self, id=0):
        guess = self.db.guess(id=id).one()
        if guess is None:
            return
        else:
            guess.cols = guess.cols.split("|")
        self.render('guess.edit.html', guess=guess, active=None)

class ResearchListHandler(sys):
    '''
    yf: 调查列表
    '''
    @tornado.web.authenticated
    def get(self, p=0):
        list = self.db.research()[p: 10].object_list
        for item in list:
            item['cols'] = item['cols'].split('|')
        self.render('research.list.html', research=list, active="research-list")

class ResearchAddHandler(sys):
    '''
    yf: 调查编辑、添加
    '''
    @tornado.web.authenticated
    def get(self):
        self.render('research.add.html', active="research-edit")

    def post(self):
        dat = self.json_decode(self.request.body)
        data = {
            'title': dat['title'],
            'cols': dat['cols'],
            'state': dat['state'],
            'expires': dat['expires'],
            'reward_score': dat['reward_score'],
            'user_id': self.current_user
        }
        if 'id' in dat:
            data['id'] = dat['id']
            self.db.research(id=data['id']).update(**data)
            self.write({'status': 1})
            return
        else:
            new_guess = self.db.research.add(**data)
            if new_guess:
                self.write({'status': 1})
                return
        self.write({'status': 0})

class ResearchEditHandler(sys):
    '''
    yf: 调查编辑页
    '''
    @tornado.web.authenticated
    def get(self, id=0):
        rs = self.db.research(id=id).one()
        if rs is None:
            return
        else:
            rs.cols = rs.cols.split("|")
        self.render('research.edit.html', research=rs, active=None)

class NotFoundHandler(sys):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/sys\">back</a>")

url_prefix = '/sys'

urls = [
    ('/?', SystemHandler),
    ('/login', LoginHandler),
    ('/guess/list', GuessListHandler),
    ('/guess/add', GuessAddHandler),
    ('/guess/edit/(?P<id>\d+)/?', GuessEditHandler),
    ('/research/list', ResearchListHandler),
    ('/research/add', ResearchAddHandler),
    ('/research/edit/(?P<id>\d+)/?', ResearchEditHandler)
]