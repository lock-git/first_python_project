import mitmproxy.http
from mitmproxy import ctx
import json

filter_host='www.iesdouyin.com' #目标主机
url_paths='/web/api/v2/aweme/post/?user_id=' # 网页 路径指纹


class Counter:
    def __init__(self):
        self.num = 0
    def request(self, flow: mitmproxy.http.HTTPFlow):
        global filter_host,url_paths
        if flow.request.host != filter_host or not flow.request.path.startswith(url_paths):
            return
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass
    def response(self, flow: mitmproxy.http.HTTPFlow):
        global filter_host,url_paths
        if flow.request.host != filter_host or not flow.request.path.startswith(url_paths):
            return
        text = flow.response.get_text()
        texts = self.deal_content(text)
        if not texts:
            print('null')
            return
        for a,b in texts:
            print(a)
            print(b)
            print('\n')
    def deal_content(self, a):
        b=json.loads(a)
        c=b.get('aweme_list')
        if not c:#c --> list of dicts
            return ''
        print('Found {} results.\n'.format(len(c)))
        rst=[]
        for i in c:
            j=i['statistics']
            info='播放次数:{} 评论数:{} 分享:{} 转发:{} 挖掘:{}'.format(j['play_count'],j['comment_count'],j['share_count'],j['forward_count'],j['digg_count'])
            #k=i['video']['download_addr']['url_list']
            #k=i['video']['play_addr_lowbr']['url_list']
            k=i['video']['play_addr']['url_list']
            ll='\n'.join(k)
            rst.append((info,ll))
        return rst

addons = [
    Counter(),
    Joker(),
]