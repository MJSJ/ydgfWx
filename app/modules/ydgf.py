# encoding: utf-8
from app.modules import base
import logging as l

class ydgf(base):
    def render(self, template_name, **kwargs):
        super(ydgf, self).render('app/'+template_name, **kwargs)

    def get_current_user(self):
        if "c" in self.session:
            return self.session["c"]
        else:
            return None

class HomeHandler(ydgf):
    '''
    yf: 首页
    '''
    def get(self):
        c = self.current_user
        if c:
            script = "window.user = {" + \
                "id: '"+str(c['id'])+"'," + \
                "gold: '"+str(c['gold'])+"'," + \
                "score: '"+str(c['score'])+"'," + \
                "nickname: '"+c['nickname']+"'," + \
                "headimgurl: '"+c['headimgurl']+"'," + \
                "province: '"+c['province']+"'," + \
                "city: '"+c['city']+"'," + \
                "country: '"+c['country']+"'}"
            self.render('base.html', cli=script)
        else:
            self.render('base.html', cli="window.user = null")

class NotFoundHandler(ydgf):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = '/ydgf'

urls = [
    ('/?', HomeHandler)
]