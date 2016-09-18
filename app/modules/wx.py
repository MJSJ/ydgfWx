# encoding: utf-8
from app.modules import base
import logging as l
import hashlib, json

class wx(base):
    def render(self, template_name, **kwargs):
        super(wx, self).render(template_name, **kwargs)

class CheckHandler(wx):
    '''
    yf: 认证公众号
    '''
    def get(self):
        _token = "sohuweixin"
        sn = self.get_argument('signature', '')
        es = self.get_argument('echostr', '')
        a = ''.join(str(i) for i in sorted([_token, self.get_argument('timestamp', 't'), self.get_argument('nonce', 'n')]))

        if str(hashlib.sha1(a).hexdigest()) == str(sn):
            self.write(es)
        else:
            l.info("fail access")
    def post(self):
        _token = "sohuweixin"
        sn = self.get_argument('signature', '')
        es = self.get_argument('echostr', '')
        a = ''.join(str(i) for i in sorted([_token, self.get_argument('timestamp', 't'), self.get_argument('nonce', 'n')]))

        if str(hashlib.sha1(a).hexdigest()) == str(sn):
            self.write(es)
        else:
            l.info("fail access")
    def check_xsrf_cookie(self):
        pass

class AuthHandler(wx):
    '''
    yf: 网页授权获取用户基本信息
    '''
    def get(self):
        path = self.get_argument('path', '')
        if 'c' in self.session:
            pass
        else: # session 不存在
            code = self.get_argument('code', '')
            access_token = self.get_access_token(code)
            if 'errcode' in access_token:
                self.write('<h1>认证失败</h1>')
                return
            user = self.get_web_user(access_token)
            ud = self.db.client(openid=user['openid'], unionid=user['unionid']).one()
            if ud: # 已经入库的用户
                self.session["c"] = ud
            else: # 从未授权的用户
                data = {
                    "openid": user['openid'],
                    "unionid": user['unionid'],
                    "nickname": user['nickname'],
                    "sex": user['sex'],
                    "province": user['province'],
                    "city": user['city'],
                    "country": user['country'],
                    "headimgurl": user['headimgurl']
                }
                newu = self.db.client.add(**data)
                if newu:
                    self.session["c"] = data
                else:
                    self.write("Server Error!")
                    return
        self.redirect(path)
        return

class AjaxHandler(wx):
    '''
    yf: 公众号请求
    '''
    def get(self):
        self.check_tocken()
        self.write(self.getU())

    def post(self):
        l.info(self.request.headers)
        l.info(self.json_decode(self.request.body))

    def check_xsrf_cookie(self):
        pass

class NotFoundHandler(wx):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = '/wx'

urls = [
    ('?', CheckHandler),
    ('/auth?', AuthHandler),
    ('/ajax?', AjaxHandler)
]