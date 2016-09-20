# encoding: utf-8
from app.modules import base
import logging as l

class api(base):
    def render(self, template_name, **kwargs):
        super(api, self).render('api/'+template_name, **kwargs)

class GuessJsonHandler(api):
    '''
    yf: 根据id获取竞猜内容
    '''
    def get(self, id=0):
        guess = self.db.guess(id=id).one()
        if guess:
            cols = guess['cols'].split('|')
            if len(cols) >= 1:
                guess['cols'] = guess['cols'].split('|')
            else:
                guess.cols = []
            self.write({'data': guess})
        else:
            self.write({'data': None})

class ResearchJsonHandler(api):
    '''
    yf: 根据id获取调查内容
    '''
    def get(self, id=0):
        research = self.db.research(id=id).one()
        if research:
            cols = research['cols'].split('|')
            if len(cols) >= 1:
                research['cols'] = research['cols'].split('|')
            else:
                research.cols = []
            self.write({'data': research})
        else:
            self.write({'data': None})

class ProductsJsonHandler(api):
    '''
    yf: 根据页数P获取商品列表
    '''
    def get(self, p=1):
        data = self.db.product(state=1)[int(p): 10]
        list = data.object_list
        for item in list:
            item['imgs'] = item['imgs'].split('|')
        self.write({'data': list, 'prev': data.prevpage, 'next': data.nextpage})

class ProductJsonHandler(api):
    '''
    yf: 根据ID获取单个商品
    '''
    def get(self, id=0):
        p = self.db.product(id=id).one()
        if p:
            imgs = p['imgs'].split('|')
            if len(imgs) >= 1:
                p['imgs'] = p['imgs'].split('|')
            else:
                p['imgs'] = []
            self.write({'data': p})
        else:
            self.write({'data': None})

class NotFoundHandler(api):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = '/api'

urls = [
    ('/guess(?P<id>[\-\d]+).json', GuessJsonHandler),
    ('/research(?P<id>[\-\d]+).json', ResearchJsonHandler),
    ('/products.json', ProductsJsonHandler),
    ('/products(?P<p>[\-\d]+).json', ProductsJsonHandler),
    ('/product(?P<id>[\-\d]+).json', ProductJsonHandler)
]