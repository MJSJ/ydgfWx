# encoding: utf-8
from torndsession.sessionhandler import SessionBaseHandler
import logging as l

class ydgf(SessionBaseHandler):
    def render(self, template_name, **kwargs):
        super(ydgf, self).render('app/'+template_name, **kwargs)

    def get_current_user(self):
        if "c" in self.session:
            return self.session["c"]
        else:
            self.session["c"] = {'id': 1, 'nickname': 'zyf', 'city': '海淀', 'province': '北京', 'country': '中国', 'score': 0, 'gold': 0 } # 这里制作假session
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