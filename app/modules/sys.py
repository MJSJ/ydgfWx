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
    def get(self, p=1):
        data = self.db.guess().sort(create_time='DESC')[int(p): 10]
        list = data.object_list
        for item in list:
            item['cols'] = item['cols'].split('|')
        self.render('guess.list.html', guess=list, active="guess-list", prevpage=data.prevpage, nextpage=data.nextpage)

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
    def get(self, p=1):
        data = self.db.research().sort(create_time='DESC')[p: 10]
        list = data.object_list
        for item in list:
            item['cols'] = item['cols'].split('|')
        self.render('research.list.html', research=list, active="research-list", prevpage=data.prevpage, nextpage=data.nextpage)

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

class ClientListHandler(sys):
    '''
    yf: 用户列表
    '''
    @tornado.web.authenticated
    def get(self, p=1):
        data = self.db.client().sort(score='DESC')[p: 10]
        list = data.object_list
        self.render('client.list.html', clients=list, active="client-list", prevpage=data.prevpage, nextpage=data.nextpage)

class ProductAddHandler(sys):
    @tornado.web.authenticated
    def get(self):
        self.render('product.add.html', active='product-add')

    def post(self):
        dat = self.json_decode(self.request.body)
        data = {
            'name': dat['name'],
            'imgs': dat['imgs'],
            'num': dat['num'],
            'score': dat['score'],
            'gold': dat['gold'],
            'state': dat['state']
        }
        if 'id' in dat:
            data['id'] = dat['id']
            self.db.product(id=dat['id']).update(**data)
            self.write({'status': 1})
            return
        else:
            newp = self.db.product.add(**data)
            if newp:
                self.write({'status': 1})
                return
        self.write({'status': 0})

class ProductListHandler(sys):
    '''
    yf: 商品列表
    '''
    @tornado.web.authenticated
    def get(self, p=1):
        data = self.db.product().sort(state='DESC')[p: 10]
        list = data.object_list
        for item in list:
            item['imgs'] = item['imgs'].split('|')
        self.render('product.list.html', products=list, active="product-list", prevpage=data.prevpage, nextpage=data.nextpage)

class ProductEditHandler(sys):
    '''
    yf: 商品编辑页
    '''
    @tornado.web.authenticated
    def get(self, id=0):
        p = self.db.product(id=id).one()
        if p is None:
            return
        else:
            p.imgs = p.imgs.split("|")
        self.render('product.edit.html', product=p, active=None)

class OrderListHandler(sys):
    '''
    yf: 订单列表
    '''
    def get(self, p=1):
        data = self.db.order().sort(create_time='DESC')[p: 10]
        list = data.object_list
        self.render('order.list.html', orders=list, active='order-list', prevpage=data.prevpage, nextpage=data.nextpage)

class NotFoundHandler(sys):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/sys\">back</a>")

url_prefix = '/sys'

urls = [
    ('/?', SystemHandler),
    ('/login', LoginHandler),
    ('/guess/list-(?P<p>[\-\d]+)', GuessListHandler),
    ('/guess/list', GuessListHandler),
    ('/guess/add', GuessAddHandler),
    ('/guess/edit/(?P<id>\d+)/?', GuessEditHandler),
    ('/research/list-(?P<p>[\-\d]+)', ResearchListHandler),
    ('/research/list', ResearchListHandler),
    ('/research/add', ResearchAddHandler),
    ('/research/edit/(?P<id>\d+)/?', ResearchEditHandler),
    ('/client/list-(?P<p>[\-\d]+)', ClientListHandler),
    ('/client/list', ClientListHandler),
    ('/product/add', ProductAddHandler),
    ('/product/edit/(?P<id>\d+)/?', ProductEditHandler),
    ('/product/list-(?P<p>[\-\d]+)', ProductListHandler),
    ('/product/list', ProductListHandler),
    ('/order/list', OrderListHandler),
    ('/order/list-(?P<p>[\-\d]+)', OrderListHandler)
]