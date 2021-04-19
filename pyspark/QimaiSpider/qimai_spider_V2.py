# -*- coding:UTF-8 -*-
from lxml import etree
import json

text = '''
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <link rel="icon" href="/favicon.ico" type="image/x-icon"/>
    <meta http-equiv="Content-Type" content="text/html; charset=gbk">
    <title>【北京,java招聘，求职】-前程无忧</title>
    <meta name="description" content="前程无忧为您提供最新最全的北京,java招聘，求职信息。网聚全国各城市的人才信息，找好工作，找好员工，上前程无忧。">
    <meta name="keywords" content="找工作,求职,人才,招聘">
    <meta name="mobile-agent" content="format=html5; url=https://m.51job.com/search/joblist.php?jobarea=010000&keyword=java&partner=webmeta">
    <meta name="mobile-agent" content="format=xhtml; url=https://m.51job.com/search/joblist.php?jobarea=010000&keyword=java&partner=webmeta">
    <meta name="robots" content="all">
    <meta http-equiv="Expires" content="0">
    <meta http-equiv="Cache-Control" content="no-cache">
    <meta http-equiv="Pragma" content="no-cache">
    <link rel="dns-prefetch" href="//js.51jobcdn.com">
    <link rel="dns-prefetch" href="//img01.51jobcdn.com">
    <link rel="dns-prefetch" href="//img02.51jobcdn.com">
    <link rel="dns-prefetch" href="//img03.51jobcdn.com">
    <link rel="dns-prefetch" href="//img04.51jobcdn.com">
    <link rel="dns-prefetch" href="//img05.51jobcdn.com">
    <link rel="dns-prefetch" href="//img06.51jobcdn.com">
    <script language="javascript" src="//js.51jobcdn.com/in/js/2016/jquery.js?20180319"></script>
    <script language="javascript">
    var _tkd = _tkd || []; //点击量统计用
    var lang = [];
    var supporthttps = 1; //浏览器是否支持https
    var currenthttps = (window.location.protocol === 'https:') ? '1' : '0'; //当前是否为https
    var systemtime = 1617269326416;
    var d_system_client_time = systemtime - new Date().getTime();
    var trackConfig = {
        'guid': '',
        'ip': '61.155.198.235',
        'accountid': '',
        'refpage': '',
        'refdomain': '',
        'domain': 'search.51job.com',
        'pageName': 'index.php',
        'partner': '',
        'islanding': '0',
    };
    window.cfg = {
        lang:'c',
        domain : {
            my : 'http://my.51job.com',
            login : 'https://login.51job.com',
            search : 'https://search.51job.com',
            www : '//www.51job.com',
            jobs : 'https://jobs.51job.com',
            jianli : 'https://jianli.51job.com',
            i : '//i.51job.com',
            jc : '//jc.51job.com',
            map : 'https://map.51job.com',
            m : 'https://m.51job.com',
            cdn : '//js.51jobcdn.com',
            help : 'https://help.51job.com',
            img : '//img03.51jobcdn.com',
            dj : '//dj.51job.com',
            mdj : '//mdj.51job.com',
            mq : '//mq.51job.com',
            mmq : '//mmq.51job.com',
            kbc : 'https://kbc.51job.com',
            mtr : 'https://medu.51job.com',
            tr : 'https://edu.51job.com',
        }
    };

window.cfg.lang = 'c';
window.cfg.fullLang = 'Chinese';
window.cfg.url = {
root : 'https://search.51job.com',
image : '//img02.51jobcdn.com/im/2009',
image_search : '//img02.51jobcdn.com/im/2009/search',
i : '//i.51job.com'
}
window.cfg.fileName = 'index.php';
window.cfg.root = 'https://search.51job.com';
window.cfg.root_userset_ajax = '//i.51job.com/userset/ajax';
window.cfg.isSearchDomain = '1';
window.cfg.langs = {
sqzwml : 'applyjob',
qzzwqdg : '请在要选择的职位前打勾!',
myml : 'my',
ts_qxjzw : '请选择职位',
queren : '确认',
guanbi : '关闭',
nzdnxj : '您最多能选择',
xiang : '项',
xzdq : '选择地区',
xj_xg : '选择/修改',
zycs : '主要城市',
sysf : '所有省份',
tspd : '特殊频道',
buxian : '不限',
qingxj : '请选择',
yixuan : '已选',
znlb : '职能类别',
hylb : '行业类别',
gzdd : '工作地点',
quanbu : '全部',
zhineng : '职能',
hangye : '行业',
didian : '地点',
qsrgjz : '请输入关键字',
srpcgjz : '输入排除关键字'
}
window.cfg.stype = '1';
window.cfg.isJobview = '1';
</script>
<script type="text/javascript" src="//js.51jobcdn.com/in/js/2016/pointtrack.js?20180605"></script>

    <script language="javascript" src="//js.51jobcdn.com/in/js/2016/login/jquery.placeholder.min.js"></script>
    <link href="//js.51jobcdn.com/in/resource/css/2021/search/common.e08e7725.css" rel="stylesheet">
<link href="//js.51jobcdn.com/in/resource/css/2021/search/index.68d65703.css" rel="stylesheet">
<link href="//js.51jobcdn.com/in/resource/css/2021/search/utils.header.91d43fda.css" rel="stylesheet">
</head>
<body>
<script type="text/javascript" src="//js.51jobcdn.com/in/resource/js/2021/search/utils.header.2bf76207.js"></script>
<div class="header">
    <!-- bar start -->
    <div class="bar">
        <div class="in">
            <div class="language">
                <ul id="languagelist">
                    <li class="tle"><span class="list">简</span></li><li><a href="http://big5.51job.com/gate/big5/www.51job.com/" rel="external nofollow">繁</a></li><li class="last"><a href="//www.51job.com/default-e.php" rel="external nofollow">EN</a></li>                    <script language="javascript">
                        if(location.hostname == "big5.51job.com")
                        {
                            $('#languagelist li span').html("繁");
                            $('#languagelist li:nth-child(2) a').html("简");
                            $('#languagelist li:nth-child(2) a').attr('href','javascript:void(0)');
                            $('#languagelist li:nth-child(2) a').click(function(){location.href=window.cfg.domain.www});
                            $('#languagelist li:nth-child(3) a').attr('href','javascript:void(0)');
                            $('#languagelist li:nth-child(3) a').click(function(){location.href=window.cfg.domain.www+"/default-e.php"});
                        }
                    </script>
                </ul>
            </div>
            <span class="l">&nbsp;</span>
            <div class="app">
                <ul>
                    <li><em class="e_icon"></em><a href="http://app.51job.com/index.html">APP下载</a></li>
                    <li>
                        <img width="80" height="80" src="//img04.51jobcdn.com/im/2016/code/new_app.png" alt="app download">
                        <p><a href="http://app.51job.com/index.html">APP下载</a></a></p>
                    </li>
                </ul>
            </div>
            <div class="uer">
                                    <p class="op">
                        <a href="https://login.51job.com/login.php?lang=c&url=http%3A%2F%2Fsearch.51job.com%2Flist%2F010000%2C000000%2C0000%2C00%2C9%2C99%2Cjava%2C2%2C1.html" rel="external nofollow">登录</a> / <a href="https://login.51job.com/register.php?lang=c&url=http%3A%2F%2Fsearch.51job.com%2Flist%2F010000%2C000000%2C0000%2C00%2C9%2C99%2Cjava%2C2%2C1.html" rel="external nofollow">注册</a>                    </p>
                            </div>
			<p class="rlk">
                <a href="//baike.51job.com" target="_blank">职场百科</a>
                <span class="lb">&nbsp;</span>
                <a href="//wenku.51job.com" target="_blank">职场文库</a>
                <span class="lb">&nbsp;</span>
                <a href="https://jobs.51job.com" target="_blank">招聘信息</a>                <span class="lb">&nbsp;</span>
                <a href="https://ehire.51job.com" target="_blank">企业服务</a>            </p>
        </div>
    </div>
    <!-- top end -->
    <!-- 英文版为body添加class -->
    <script>
            </script>
    <!-- nag start -->
    <div class="pop-city" style="display:none;position: absolute; z-index: 1000;" id="area_channel_layer">
    <div class="tle">
        地区选择        <em class="close" onclick="jvascript:$('#area_channel_layer,#area_channel_layer_backdrop').hide();"></em>
    </div>
    <div class="pcon">
        <div class="ht">
            <label>热门城市</label><a href="//www.51job.com/beijing/">北京</a><a href="//www.51job.com/shanghai/">上海</a><a href="//www.51job.com/guangzhou/">广州</a><a href="//www.51job.com/shenzhen/">深圳</a><a href="//www.51job.com/wuhan/">武汉</a><a href="//www.51job.com/xian/">西安</a><a href="//www.51job.com/hangzhou/">杭州</a><a href="//www.51job.com/nanjing/">南京</a><a href="//www.51job.com/chengdu/">成都</a><a href="//www.51job.com/chongqing/">重庆</a>        </div>
        <div class="cbox">
            <ul  id="area_channel_layer_list">
                <li class="on" onclick="areaChannelChangeTab('abc', this)">A B C</li>
                <li onclick="areaChannelChangeTab('def', this)">D E F</li>
                <li onclick="areaChannelChangeTab('gh', this)">G H</li>
                <li onclick="areaChannelChangeTab('jkl', this)">J K L</li>
                <li onclick="areaChannelChangeTab('mnp', this)">M N P</li>
                <li onclick="areaChannelChangeTab('qrs', this)">Q R S</li>
                <li onclick="areaChannelChangeTab('twx', this)">T W X</li>
                <li onclick="areaChannelChangeTab('yz', this)">Y Z</li>
            </ul>
            <div class="clst"  id="area_channel_layer_all">
                    <div class="e" name="area_channel_div_abc">
        <span><a href="//www.51job.com/anshan/">鞍山</a></span>
        <span><a href="//www.51job.com/anqing/">安庆</a></span>
        <span><a href="//www.51job.com/anyang/">安阳</a></span>
        <span><a href="//www.51job.com/beijing/">北京</a></span>
        <span><a href="//www.51job.com/baotou/">包头</a></span>
        <span><a href="//www.51job.com/baoding/">保定</a></span>
        <span><a href="//www.51job.com/bengbu/">蚌埠</a></span>
        <span><a href="//www.51job.com/baoji/">宝鸡</a></span>
        <span><a href="//www.51job.com/binzhou/">滨州</a></span>
        <span><a href="//www.51job.com/changchun/">长春</a></span>
        <span><a href="//www.51job.com/changsha/">长沙</a></span>
        <span><a href="//www.51job.com/chengdu/">成都</a></span>
        <span><a href="//www.51job.com/chongqing/">重庆</a></span>
        <span><a href="//www.51job.com/changzhou/">常州</a></span>
        <span><a href="//www.51job.com/changde/">常德</a></span>
        <span><a href="//www.51job.com/changshu/">常熟</a></span>
        <span><a href="//www.51job.com/cangzhou/">沧州</a></span>
        <span><a href="//www.51job.com/chaozhou/">潮州</a></span>
        <span><a href="//www.51job.com/chenzhou/">郴州</a></span>
        <span><a href="//www.51job.com/chifeng/">赤峰</a></span>
        <span><a href="//www.51job.com/chuzhou/">滁州</a></span>
        <span><a href="//www.51job.com/changzhi/">长治</a></span>
    </div>
    <div class="e" name="area_channel_div_def" style="display:none">
        <span><a href="//www.51job.com/dalian/">大连</a></span>
        <span><a href="//www.51job.com/dongguan/">东莞</a></span>
        <span><a href="//www.51job.com/dandong/">丹东</a></span>
        <span><a href="//www.51job.com/daqing/">大庆</a></span>
        <span><a href="//www.51job.com/dazhou/">达州</a></span>
        <span><a href="//www.51job.com/datong/">大同</a></span>
        <span><a href="//www.51job.com/deyang/">德阳</a></span>
        <span><a href="//www.51job.com/dezhou/">德州</a></span>
        <span><a href="//www.51job.com/dongying/">东营</a></span>
        <span><a href="//www.51job.com/errduosi/">鄂尔多斯</a></span>
        <span><a href="//www.51job.com/ezhou/">鄂州</a></span>
        <span><a href="//www.51job.com/fuzhou/">福州</a></span>
        <span><a href="//www.51job.com/foshan/">佛山</a></span>
        <span><a href="//www.51job.com/fushun/">抚顺</a></span>
        <span><a href="//www.51job.com/fuzhoue/">抚州</a></span>
        <span><a href="//www.51job.com/fuyang/">阜阳</a></span>
    </div>
    <div class="e" name="area_channel_div_gh" style="display:none">
        <span><a href="//www.51job.com/guangzhou/">广州</a></span>
        <span><a href="//www.51job.com/guiyang/">贵阳</a></span>
        <span><a href="//www.51job.com/ganzhou/">赣州</a></span>
        <span><a href="//www.51job.com/guangan/">广安</a></span>
        <span><a href="//www.51job.com/guangyuan/">广元</a></span>
        <span><a href="//www.51job.com/guigang/">贵港</a></span>
        <span><a href="//www.51job.com/guilin/">桂林</a></span>
        <span><a href="//www.51job.com/harbin/">哈尔滨</a></span>
        <span><a href="//www.51job.com/hangzhou/">杭州</a></span>
        <span><a href="//www.51job.com/hefei/">合肥</a></span>
        <span><a href="//www.51job.com/haikou/">海口</a></span>
        <span><a href="//www.51job.com/huhhot/">呼和浩特</a></span>
        <span><a href="//www.51job.com/huizhou/">惠州</a></span>
        <span><a href="//www.51job.com/hengyang/">衡阳</a></span>
        <span><a href="//www.51job.com/huaian/">淮安</a></span>
        <span><a href="//www.51job.com/huzhou/">湖州</a></span>
        <span><a href="//www.51job.com/handan/">邯郸</a></span>
        <span><a href="//www.51job.com/hanzhong/">汉中</a></span>
        <span><a href="//www.51job.com/heyuan/">河源</a></span>
        <span><a href="//www.51job.com/heze/">菏泽</a></span>
        <span><a href="//www.51job.com/hengshui/">衡水</a></span>
        <span><a href="//www.51job.com/huaihua/">怀化</a></span>
        <span><a href="//www.51job.com/huaibei/">淮北</a></span>
        <span><a href="//www.51job.com/huainan/">淮南</a></span>
        <span><a href="//www.51job.com/huanggang/">黄冈</a></span>
        <span><a href="//www.51job.com/huangshi/">黄石</a></span>
    </div>
    <div class="e" name="area_channel_div_jkl" style="display:none">
        <span><a href="//www.51job.com/jinan/">济南</a></span>
        <span><a href="//www.51job.com/jiaxing/">嘉兴</a></span>
        <span><a href="//www.51job.com/jinhua/">金华</a></span>
        <span><a href="//www.51job.com/jilin/">吉林</a></span>
        <span><a href="//www.51job.com/jiangmen/">江门</a></span>
        <span><a href="//www.51job.com/jingzhou/">荆州</a></span>
        <span><a href="//www.51job.com/jining/">济宁</a></span>
        <span><a href="//www.51job.com/jiujiang/">九江</a></span>
        <span><a href="//www.51job.com/jian/">吉安</a></span>
        <span><a href="//www.51job.com/jiaozuo/">焦作</a></span>
        <span><a href="//www.51job.com/jieyang/">揭阳</a></span>
        <span><a href="//www.51job.com/jinzhou/">锦州</a></span>
        <span><a href="//www.51job.com/jinzhong/">晋中</a></span>
        <span><a href="//www.51job.com/jingmen/">荆门</a></span>
        <span><a href="//www.51job.com/kunming/">昆明</a></span>
        <span><a href="//www.51job.com/kunshan/">昆山</a></span>
        <span><a href="//www.51job.com/kaifeng/">开封</a></span>
        <span><a href="//www.51job.com/lanzhou/">兰州</a></span>
        <span><a href="//www.51job.com/langfang/">廊坊</a></span>
        <span><a href="//www.51job.com/linyi/">临沂</a></span>
        <span><a href="//www.51job.com/luoyang/">洛阳</a></span>
        <span><a href="//www.51job.com/lianyungang/">连云港</a></span>
        <span><a href="//www.51job.com/liuzhou/">柳州</a></span>
        <span><a href="//www.51job.com/leshan/">乐山</a></span>
        <span><a href="//www.51job.com/liaocheng/">聊城</a></span>
        <span><a href="//www.51job.com/linfen/">临汾</a></span>
        <span><a href="//www.51job.com/luan/">六安</a></span>
        <span><a href="//www.51job.com/loudi/">娄底</a></span>
        <span><a href="//www.51job.com/luzhou/">泸州</a></span>
        <span><a href="//www.51job.com/luohe/">漯河</a></span>
    </div>
    <div class="e" name="area_channel_div_mnp" style="display:none">
        <span><a href="//www.51job.com/mianyang/">绵阳</a></span>
        <span><a href="//www.51job.com/maanshan/">马鞍山</a></span>
        <span><a href="//www.51job.com/maoming/">茂名</a></span>
        <span><a href="//www.51job.com/meishan/">眉山</a></span>
        <span><a href="//www.51job.com/meizhou/">梅州</a></span>
        <span><a href="//www.51job.com/nanjing/">南京</a></span>
        <span><a href="//www.51job.com/ningbo/">宁波</a></span>
        <span><a href="//www.51job.com/nanchang/">南昌</a></span>
        <span><a href="//www.51job.com/nantong/">南通</a></span>
        <span><a href="//www.51job.com/nanning/">南宁</a></span>
        <span><a href="//www.51job.com/nanchong/">南充</a></span>
        <span><a href="//www.51job.com/nanyang/">南阳</a></span>
        <span><a href="//www.51job.com/neijiang/">内江</a></span>
        <span><a href="//www.51job.com/ningde/">宁德</a></span>
        <span><a href="//www.51job.com/pingdingshan/">平顶山</a></span>
        <span><a href="//www.51job.com/putian/">莆田</a></span>
        <span><a href="//www.51job.com/puyang/">濮阳</a></span>
    </div>
    <div class="e" name="area_channel_div_qrs" style="display:none">
        <span><a href="//www.51job.com/qingdao/">青岛</a></span>
        <span><a href="//www.51job.com/quanzhou/">泉州</a></span>
        <span><a href="//www.51job.com/qinhuangdao/">秦皇岛</a></span>
        <span><a href="//www.51job.com/qingyuan/">清远</a></span>
        <span><a href="//www.51job.com/qiqihaer/">齐齐哈尔</a></span>
        <span><a href="//www.51job.com/quzhou/">衢州</a></span>
        <span><a href="//www.51job.com/qujing/">曲靖</a></span>
        <span><a href="//www.51job.com/rizhao/">日照</a></span>
        <span><a href="//www.51job.com/shanghai/">上海</a></span>
        <span><a href="//www.51job.com/shenzhen/">深圳</a></span>
        <span><a href="//www.51job.com/shenyang/">沈阳</a></span>
        <span><a href="//www.51job.com/shijiazhuang/">石家庄</a></span>
        <span><a href="//www.51job.com/suzhou/">苏州</a></span>
        <span><a href="//www.51job.com/sanya/">三亚</a></span>
        <span><a href="//www.51job.com/shaoxing/">绍兴</a></span>
        <span><a href="//www.51job.com/shantou/">汕头</a></span>
        <span><a href="//www.51job.com/shanwei/">汕尾</a></span>
        <span><a href="//www.51job.com/shangqiu/">商丘</a></span>
        <span><a href="//www.51job.com/shangrao/">上饶</a></span>
        <span><a href="//www.51job.com/shaoguan/">韶关</a></span>
        <span><a href="//www.51job.com/shaoyang/">邵阳</a></span>
        <span><a href="//www.51job.com/shiyan/">十堰</a></span>
        <span><a href="//www.51job.com/suizhou/">随州</a></span>
        <span><a href="//www.51job.com/suining/">遂宁</a></span>
        <span><a href="//www.51job.com/suqian/">宿迁</a></span>
        <span><a href="//www.51job.com/suzhoue/">宿州</a></span>
    </div>
    <div class="e" name="area_channel_div_twx" style="display:none">
        <span><a href="//www.51job.com/tianjin/">天津</a></span>
        <span><a href="//www.51job.com/taiyuan/">太原</a></span>
        <span><a href="//www.51job.com/taizhoue/">台州</a></span>
        <span><a href="//www.51job.com/tangshan/">唐山</a></span>
        <span><a href="//www.51job.com/taizhou/">泰州</a></span>
        <span><a href="//www.51job.com/tieling/">铁岭</a></span>
        <span><a href="//www.51job.com/taian/">泰安</a></span>
        <span><a href="//www.51job.com/wuhan/">武汉</a></span>
        <span><a href="//www.51job.com/wuxi/">无锡</a></span>
        <span><a href="//www.51job.com/wenzhou/">温州</a></span>
        <span><a href="//www.51job.com/urumqi/">乌鲁木齐</a></span>
        <span><a href="//www.51job.com/wuhu/">芜湖</a></span>
        <span><a href="//www.51job.com/weifang/">潍坊</a></span>
        <span><a href="//www.51job.com/weihai/">威海</a></span>
        <span><a href="//www.51job.com/weinan/">渭南</a></span>
        <span><a href="//www.51job.com/xian/">西安</a></span>
        <span><a href="//www.51job.com/xiamen/">厦门</a></span>
        <span><a href="//www.51job.com/xuzhou/">徐州</a></span>
        <span><a href="//www.51job.com/xiangyang/">襄阳</a></span>
        <span><a href="//www.51job.com/xiangtan/">湘潭</a></span>
        <span><a href="//www.51job.com/xianyang/">咸阳</a></span>
        <span><a href="//www.51job.com/xining/">西宁</a></span>
        <span><a href="//www.51job.com/xianning/">咸宁</a></span>
        <span><a href="//www.51job.com/xiaogan/">孝感</a></span>
        <span><a href="//www.51job.com/xinxiang/">新乡</a></span>
        <span><a href="//www.51job.com/xinyang/">信阳</a></span>
        <span><a href="//www.51job.com/xingtai/">邢台</a></span>
        <span><a href="//www.51job.com/xuchang/">许昌</a></span>
        <span><a href="//www.51job.com/xuancheng/">宣城</a></span>
    </div>
    <div class="e" name="area_channel_div_yz" style="display:none">
        <span><a href="//www.51job.com/yantai/">烟台</a></span>
        <span><a href="//www.51job.com/yangzhou/">扬州</a></span>
        <span><a href="//www.51job.com/yichang/">宜昌</a></span>
        <span><a href="//www.51job.com/yancheng/">盐城</a></span>
        <span><a href="//www.51job.com/yiwu/">义乌</a></span>
        <span><a href="//www.51job.com/yingkou/">营口</a></span>
        <span><a href="//www.51job.com/yinchuan/">银川</a></span>
        <span><a href="//www.51job.com/yangjiang/">阳江</a></span>
        <span><a href="//www.51job.com/yibin/">宜宾</a></span>
        <span><a href="//www.51job.com/yichune/">宜春</a></span>
        <span><a href="//www.51job.com/yiyang/">益阳</a></span>
        <span><a href="//www.51job.com/yongzhou/">永州</a></span>
        <span><a href="//www.51job.com/yulin/">玉林</a></span>
        <span><a href="//www.51job.com/yueyang/">岳阳</a></span>
        <span><a href="//www.51job.com/yuncheng/">运城</a></span>
        <span><a href="//www.51job.com/zhangzhou/">漳州</a></span>
        <span><a href="//www.51job.com/zhengzhou/">郑州</a></span>
        <span><a href="//www.51job.com/zhongshan/">中山</a></span>
        <span><a href="//www.51job.com/zhuhai/">珠海</a></span>
        <span><a href="//www.51job.com/zhenjiang/">镇江</a></span>
        <span><a href="//www.51job.com/zhuzhou/">株洲</a></span>
        <span><a href="//www.51job.com/zhanjiang/">湛江</a></span>
        <span><a href="//www.51job.com/zhaoqing/">肇庆</a></span>
        <span><a href="//www.51job.com/zhangjiagang/">张家港</a></span>
        <span><a href="//www.51job.com/zibo/">淄博</a></span>
        <span><a href="//www.51job.com/zaozhuang/">枣庄</a></span>
        <span><a href="//www.51job.com/zhangjiakou/">张家口</a></span>
        <span><a href="//www.51job.com/zhoukou/">周口</a></span>
        <span><a href="//www.51job.com/zhumadian/">驻马店</a></span>
        <span><a href="//www.51job.com/zunyi/">遵义</a></span>
    </div>
            </div>
            <div class="clear"></div>
        </div>
    </div>
</div>

<div id="area_channel_layer_backdrop" class="layer_back_drop_class" style="z-index:999;position:absolute;z-index:999;left:0;top:0;display:none"></div>
<script>

    $(document).ready(function(){
        $(window).resize(function(){
            if(!$("#area_channel_layer").is(":hidden"))
            {
                setLayerPosition();
            }
        });
    });

    window.areaChannelChangeTab = function(sName, oEvent)
    {
        $("#area_channel_layer_all").children().hide();
        $("#area_channel_layer_list").children().removeClass("on");
        $(oEvent).addClass("on");
        $("#area_channel_layer_all").children("div[name='area_channel_div_" + sName + "']").show();
        $("#area_channel_layer_backdrop").show();
    };

    window.openAreaChannelLayer = function()
    {
        setLayerPosition();
        $("#area_channel_layer,#area_channel_layer_backdrop").show();
    };

    window.setLayerPosition = function()
    {
        var dl = $(document).scrollLeft();
        var dt = $(document).scrollTop();
        var ww = $(document).width();
        var dwh = $(document).height();
        var wwh = $(window).height();
        var ow = $("#area_channel_layer").width();
        var oh = $("#area_channel_layer").height();
        var fLeft = (ww - ow) / 2 + dl;
        var fTop = (wwh - oh) * 382 / 1000 + dt;//黄金比例
        $("#area_channel_layer").css({'left': Math.max(parseInt(fLeft), dl), 'top': Math.max(parseInt(fTop), dt)});
        $("#area_channel_layer_backdrop").css({'width': ww + 'px', 'height': dwh + 'px'});
    }
</script>    <div class="nag" id="topIndex">
        <div class="in">
            <a href="//www.51job.com"><img class="logo" id="logo" width="90" height="40" src="//img05.51jobcdn.com/im/2016/logo/logo_blue.png" alt="前程无忧"></a>
                                                                                <img class="slogen" id="slogen" width="162" height="17" src="//img01.51jobcdn.com/im/2016/header/slogen.png?1544426366">
                            
            <!-- Jobs频道使用 start -->
                        <!-- Jobs频道使用 end -->
            
<p class="nlink">
    <a class="" href="//www.51job.com/">首页</a>
    <a class="on" href="https://search.51job.com">职位搜索</a>
    <a class="" href="javascript:openAreaChannelLayer();">地区频道</a>
    <a class="" href="https://edu.51job.com" target="_blank">无忧学院</a>
    <a class="" href="https://mkt.51job.com/careerpost/default_res.php">职场资讯</a>
    <a class="" href="https://xy.51job.com/default-xs.php">校园招聘</a>
    <a href="http://my.51job.com/my/gojingying.php?direct=https%3A%2F%2Fwww.51jingying.com%2Fcommon%2Fsearchcase.php%3F5CC4CE%3D1008" target="_blank">无忧精英</a>
</p>        </div>
    </div>
    <!-- nag end -->
    </div><input type="hidden" id="pageCode" value="10101">

<div class="j_loading" id="loading_div">
    <div class="rotate">
        <div></div>
        <div></div>
    </div>
    正在加载...
</div>
<div id="app"></div>

<script type="text/javascript">
window.__SEARCH_RESULT__ = {"top_ads":[],"auction_ads":[{"type":"auction_ads","jt":"5","tags":["hurry"],"ad_track":"1","jobid":"130012243","coid":"4000430","effect":"1","is_special_job":"1","job_href":"https:\/\/jobs.51job.com\/beijing-sjsq\/130012243.html?s=sou_sou_soulb&t=5","job_name":"后端开发工程师（电商）","job_title":"后端开发工程师（电商）","company_href":"https:\/\/jobs.51job.com\/all\/co4000430.html","company_name":"中铁建网络信息科技有限公司","providesalary_text":"1-2万\/月","workarea":"010700","workarea_text":"北京-石景山区","updatedate":"04-01","iscommunicate":"","companytype_text":"国企","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 14:03:38","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 通讯补贴 绩效奖金 定期体检","jobwelf_list":["五险一金","通讯补贴","绩效奖金","定期体检"],"attribute_text":["北京-石景山区","3-4年经验","本科","招3人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":"35146357"}],"market_ads":[],"engine_search_result":[{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128002595","coid":"1991749","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/128002595.html?s=sou_sou_soulb&t=0","job_name":"阿里影业-高级Java开发工程师-北京","job_title":"阿里影业-高级Java开发工程师-北京","company_href":"https:\/\/jobs.51job.com\/all\/co1991749.html","company_name":"阿里巴巴集团","providesalary_text":"","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 11:10:23","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","3-4年经验","本科","招若干人"],"companysize_text":"10000人以上","companyind_text":"互联网\/电子商务","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"119241090","coid":"2188650","effect":"1","is_special_job":"1","job_href":"http:\/\/dhl.51job.com\/sc\/show_job_detail.php?jobid=119241090","job_name":"JAVA 工程师","job_title":"JAVA 工程师","company_href":"http:\/\/dhl.51job.com","company_name":"中外运-敦豪(DHL-Sinotrans)","providesalary_text":"1.5-2万\/月","workarea":"011400","workarea_text":"北京-大兴区","updatedate":"04-01","iscommunicate":"","companytype_text":"合资","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 16:53:27","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-大兴区","3-4年经验","本科","招1人"],"companysize_text":"5000-10000人","companyind_text":"交通\/运输\/物流","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130612295","coid":"2471571","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130612295.html?s=sou_sou_soulb&t=0","job_name":"JAVA工程师","job_title":"JAVA工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2471571.html","company_name":"武汉佰钧成技术有限责任公司","providesalary_text":"1.5-2万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 15:41:02","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-海淀区","3-4年经验","本科","招若干人"],"companysize_text":"10000人以上","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130601226","coid":"156141","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-dxq\/130601226.html?s=sou_sou_soulb&t=0","job_name":"JAVA开发工程师(J26781)","job_title":"JAVA开发工程师(J26781)","company_href":"https:\/\/jobs.51job.com\/all\/co156141.html","company_name":"京东方科技集团股份有限公司","providesalary_text":"1.5-2.8万\/月","workarea":"011400","workarea_text":"北京-大兴区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"6","issuedate":"2021-04-01 13:48:35","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-大兴区","5-7年经验","本科","招2人"],"companysize_text":"10000人以上","companyind_text":"电子技术\/半导体\/集成电路","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"124781086","coid":"6037863","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/124781086.html?s=sou_sou_soulb&t=0","job_name":"Java后端开发","job_title":"Java后端开发","company_href":"https:\/\/jobs.51job.com\/all\/co6037863.html","company_name":"华夏银行股份有限公司信用卡中心","providesalary_text":"","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"国企","degreefrom":"6","workyear":"4","issuedate":"2021-04-01 12:39:13","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","2年经验","本科","招若干人"],"companysize_text":"5000-10000人","companyind_text":"金融\/投资\/证券","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130620075","coid":"4197127","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/130620075.html?s=sou_sou_soulb&t=0","job_name":"Java技术经理","job_title":"Java技术经理","company_href":"https:\/\/jobs.51job.com\/all\/co4197127.html","company_name":"南京英诺森软件科技有限公司","providesalary_text":"2.5-3.2万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"6","issuedate":"2021-04-01 17:10:33","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 年终奖金 定期体检","jobwelf_list":["五险一金","补充医疗保险","年终奖金","定期体检"],"attribute_text":["北京","5-7年经验","本科","招1人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"124648972","coid":"3960270","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/124648972.html?s=sou_sou_soulb&t=0","job_name":"JAVA开发工程师","job_title":"JAVA开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co3960270.html","company_name":"北京瑞尼尔技术有限公司","providesalary_text":"0.8-2万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"3","issuedate":"2021-04-01 16:56:05","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 年终奖金 专业培训 带薪年假 绩效奖金","jobwelf_list":["五险一金","餐饮补贴","年终奖金","专业培训","带薪年假","绩效奖金"],"attribute_text":["北京-海淀区","1年经验","本科","招2人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"121835723","coid":"5819023","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/121835723.html?s=sou_sou_soulb&t=0","job_name":"Java\/JSP程序员","job_title":"Java\/JSP程序员","company_href":"https:\/\/jobs.51job.com\/all\/co5819023.html","company_name":"北京华电园信息技术有限公司","providesalary_text":"6-8千\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"3","issuedate":"2021-04-01 16:46:25","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 交通补贴 年终奖金","jobwelf_list":["五险一金","交通补贴","年终奖金"],"attribute_text":["北京-海淀区","1年经验","本科","招50人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129436901","coid":"2270049","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cpq\/129436901.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2270049.html","company_name":"北京赛博兴安科技有限公司","providesalary_text":"1-2万\/月","workarea":"011300","workarea_text":"北京-昌平区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"4","issuedate":"2021-04-01 16:38:38","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 交通补贴 餐饮补贴 通讯补贴 绩效奖金 年终奖金 弹性工作 定期体检 员工旅游","jobwelf_list":["五险一金","补充医疗保险","交通补贴","餐饮补贴","通讯补贴","绩效奖金","年终奖金","弹性工作","定期体检","员工旅游"],"attribute_text":["北京-昌平区","2年经验","本科","招2人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"125904725","coid":"419990","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/125904725.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发工程师","job_title":"Java高级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co419990.html","company_name":"震坤行工业超市（上海）有限公司","providesalary_text":"2.5-5万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 16:26:15","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","3-4年经验","本科","招10人"],"companysize_text":"1000-5000人","companyind_text":"互联网\/电子商务","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130614356","coid":"6441691","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-dcq\/130614356.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/coUjIFZVA3BToCYQ1nUzc.html","company_name":"深圳曜石软件有限公司","providesalary_text":"0.8-2.4万\/月","workarea":"010100","workarea_text":"北京-东城区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"4","issuedate":"2021-04-01 16:02:16","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 员工旅游 股票期权 年终奖金 定期体检 专业培训","jobwelf_list":["五险一金","补充医疗保险","员工旅游","股票期权","年终奖金","定期体检","专业培训"],"attribute_text":["北京-东城区","2年经验","本科","招1人"],"companysize_text":"","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"125869138","coid":"5900941","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-dcq\/125869138.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5900941.html","company_name":"中科软科技股份有限公司","providesalary_text":"0.8-1.3万\/月","workarea":"010100","workarea_text":"北京-东城区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 15:41:29","isFromXyz":"","isIntern":"0","jobwelf":"餐饮补贴 通讯补贴 五险一金","jobwelf_list":["餐饮补贴","通讯补贴","五险一金"],"attribute_text":["北京-东城区","3-4年经验","大专","招若干人"],"companysize_text":"10000人以上","companyind_text":"计算机服务(系统、数据服务、维修)","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128253057","coid":"6279467","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/128253057.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co6279467.html","company_name":"北京鼎力天拓科技有限公司","providesalary_text":"0.8-1.5万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"3","issuedate":"2021-04-01 15:36:58","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 绩效奖金 年终奖金 加班补助 餐饮补贴 周末双休","jobwelf_list":["五险一金","绩效奖金","年终奖金","加班补助","餐饮补贴","周末双休"],"attribute_text":["北京-海淀区","1年经验","本科","招若干人"],"companysize_text":"少于50人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129960370","coid":"3386257","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/129960370.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师(中级）","job_title":"Java开发工程师(中级）","company_href":"https:\/\/jobs.51job.com\/all\/co3386257.html","company_name":"上海塔罗信息技术有限公司","providesalary_text":"1-1.7万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 15:27:32","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 补充公积金","jobwelf_list":["五险一金","补充医疗保险","补充公积金"],"attribute_text":["北京-海淀区","3-4年经验","大专","招若干人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130610700","coid":"3303178","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130610700.html?s=sou_sou_soulb&t=0","job_name":"Java中级开发工程师(互联网）","job_title":"Java中级开发工程师(互联网）","company_href":"https:\/\/jobs.51job.com\/all\/co3303178.html","company_name":"武汉合力亿捷科技有限公司","providesalary_text":"1-1.5万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"4","issuedate":"2021-04-01 15:22:00","isFromXyz":"","isIntern":"0","jobwelf":"补充医疗保险 五险一金 通讯补贴 年终奖金 定期体检","jobwelf_list":["补充医疗保险","五险一金","通讯补贴","年终奖金","定期体检"],"attribute_text":["北京-海淀区","2年经验","本科","招2人"],"companysize_text":"500-1000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"112159887","coid":"5439248","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/112159887.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5439248.html","company_name":"北京后来科技有限公司","providesalary_text":"0.6-1.5万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"3","issuedate":"2021-04-01 15:17:32","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-海淀区","1年经验","大专","招若干人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":["communicate"],"ad_track":"","jobid":"130220197","coid":"3260078","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/130220197.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co3260078.html","company_name":"上海致宇信息技术有限公司","providesalary_text":"1-2万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"1","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 15:11:34","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 年终奖金 专业培训","jobwelf_list":["五险一金","年终奖金","专业培训"],"attribute_text":["北京-朝阳区","3-4年经验","本科","招若干人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130605074","coid":"6063217","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-xcq\/130605074.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co6063217.html","company_name":"珠海市华盛达科技有限公司","providesalary_text":"1.2-2.2万\/月","workarea":"010200","workarea_text":"北京-西城区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 14:27:15","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 绩效奖金 定期体检","jobwelf_list":["五险一金","补充医疗保险","绩效奖金","定期体检"],"attribute_text":["北京-西城区","3-4年经验","本科","招3人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128038558","coid":"290276","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/128038558.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师(北京）","job_title":"Java开发工程师(北京）","company_href":"https:\/\/jobs.51job.com\/all\/co290276.html","company_name":"深圳市长亮科技股份有限公司","providesalary_text":"1.5-3万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"4","issuedate":"2021-04-01 13:57:34","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 通讯补贴 员工旅游 定期体检 股票期权 年终奖金 绩效奖金 弹性工作","jobwelf_list":["五险一金","餐饮补贴","通讯补贴","员工旅游","定期体检","股票期权","年终奖金","绩效奖金","弹性工作"],"attribute_text":["北京","2年经验","本科","招6人"],"companysize_text":"1000-5000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129128706","coid":"6340777","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/129128706.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co6340777.html","company_name":"北京商联达科技有限公司上海分公司","providesalary_text":"0.8-1万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"3","issuedate":"2021-04-01 13:34:51","isFromXyz":"","isIntern":"0","jobwelf":"五险一金","jobwelf_list":["五险一金"],"attribute_text":["北京-海淀区","1年经验","大专","招2人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129752435","coid":"229057","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/129752435.html?s=sou_sou_soulb&t=0","job_name":"Java中级开发工程师","job_title":"Java中级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co229057.html","company_name":"上海羽裳信息科技有限公司","providesalary_text":"1.5-2万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 12:24:02","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","3-4年经验","本科","招若干人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130599001","coid":"5415345","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130599001.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5415345.html","company_name":"北京绥通科技发展有限公司","providesalary_text":"1.2-2.4万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 12:01:44","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-海淀区","3-4年经验","本科","招1人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"111793271","coid":"2011611","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/111793271.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发工程师","job_title":"Java高级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2011611.html","company_name":"北京聚源锐思数据科技有限公司","providesalary_text":"1.5-2.5万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 11:30:00","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 年终奖金 定期体检 弹性工作 交通补贴 餐饮补贴 通讯补贴 员工旅游","jobwelf_list":["五险一金","年终奖金","定期体检","弹性工作","交通补贴","餐饮补贴","通讯补贴","员工旅游"],"attribute_text":["北京-海淀区","3-4年经验","本科","招1人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130591087","coid":"5142614","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/130591087.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5142614.html","company_name":"上海治熵信息科技有限公司","providesalary_text":"1.3-1.7万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 11:18:34","isFromXyz":"","isIntern":"0","jobwelf":"年终奖金 绩效奖金 弹性工作 五险一金","jobwelf_list":["年终奖金","绩效奖金","弹性工作","五险一金"],"attribute_text":["北京","3-4年经验","大专","招1人"],"companysize_text":"少于50人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130593027","coid":"2662475","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130593027.html?s=sou_sou_soulb&t=0","job_name":"中高级Java开发工程师","job_title":"中高级Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2662475.html","company_name":"北京新榕基业软件技术有限公司","providesalary_text":"1-2万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 11:15:51","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 年终奖金 带薪年假","jobwelf_list":["五险一金","年终奖金","带薪年假"],"attribute_text":["北京-海淀区","3-4年经验","本科","招3人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"126984910","coid":"1203988","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-syq\/126984910.html?s=sou_sou_soulb&t=0","job_name":"java软件工程师（工作地：北京）","job_title":"java软件工程师（工作地：北京）","company_href":"https:\/\/jobs.51job.com\/all\/co1203988.html","company_name":"上海锐道信息技术有限公司","providesalary_text":"0.8-1万\/月","workarea":"011200","workarea_text":"北京-顺义区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"3","issuedate":"2021-04-01 11:02:50","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 员工旅游 专业培训 年终奖金 定期体检 弹性工作","jobwelf_list":["五险一金","员工旅游","专业培训","年终奖金","定期体检","弹性工作"],"attribute_text":["北京-顺义区","1年经验","大专","招若干人"],"companysize_text":"50-150人","companyind_text":"计算机服务(系统、数据服务、维修)","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"118302533","coid":"5185978","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/118302533.html?s=sou_sou_soulb&t=0","job_name":"Java高级工程师","job_title":"Java高级工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5185978.html","company_name":"北京万华恒信信息技术有限公司","providesalary_text":"1.5-1.7万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 10:37:13","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 补充医疗保险 员工旅游 交通补贴 绩效奖金 年终奖金 定期体检","jobwelf_list":["五险一金","补充医疗保险","员工旅游","交通补贴","绩效奖金","年终奖金","定期体检"],"attribute_text":["北京-朝阳区","3-4年经验","大专","招1人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130589873","coid":"2274319","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-ftq\/130589873.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2274319.html","company_name":"上海速强信息技术股份有限公司","providesalary_text":"1-1.5万\/月","workarea":"010600","workarea_text":"北京-丰台区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 10:35:41","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 员工旅游 绩效奖金 年终奖金 定期体检 生日礼券 节日福利 带薪休假 团队聚餐 荐才奖","jobwelf_list":["五险一金","员工旅游","绩效奖金","年终奖金","定期体检","生日礼券","节日福利","带薪休假","团队聚餐","荐才奖"],"attribute_text":["北京-丰台区","3-4年经验","本科","招若干人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130587716","coid":"4389218","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-dcq\/130587716.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co4389218.html","company_name":"北京腾信软创科技股份有限公司","providesalary_text":"1.2-1.6万\/月","workarea":"010100","workarea_text":"北京-东城区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 10:04:25","isFromXyz":"","isIntern":"0","jobwelf":"定期体检 五险一金 员工旅游 交通补贴 餐饮补贴 专业培训","jobwelf_list":["定期体检","五险一金","员工旅游","交通补贴","餐饮补贴","专业培训"],"attribute_text":["北京-东城区","3-4年经验","大专","招2人"],"companysize_text":"500-1000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130386263","coid":"2665718","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/130386263.html?s=sou_sou_soulb&t=0","job_name":"中高级Java开发工程师","job_title":"中高级Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2665718.html","company_name":"奔讯电子科技（北京）有限公司","providesalary_text":"1.1-1.8万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"外资（非欧美）","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 10:03:48","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 定期体检 出国机会 员工旅游","jobwelf_list":["五险一金","定期体检","出国机会","员工旅游"],"attribute_text":["北京-朝阳区","3-4年经验","本科","招1人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130587441","coid":"642236","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/130587441.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co642236.html","company_name":"北京神州泰岳软件股份有限公司","providesalary_text":"1-2万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 10:00:32","isFromXyz":"","isIntern":"0","jobwelf":"补充医疗保险 餐饮补贴 员工旅游 定期体检 年终奖金","jobwelf_list":["补充医疗保险","餐饮补贴","员工旅游","定期体检","年终奖金"],"attribute_text":["北京-朝阳区","3-4年经验","本科","招2人"],"companysize_text":"1000-5000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"126299860","coid":"6145211","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/126299860.html?s=sou_sou_soulb&t=0","job_name":"java开发与实施工程师","job_title":"java开发与实施工程师","company_href":"https:\/\/jobs.51job.com\/all\/co6145211.html","company_name":"北京恒信启华信息技术有限公司","providesalary_text":"0.8-1.6万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"4","issuedate":"2021-04-01 09:45:37","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-海淀区","2年经验","大专","招6人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130168643","coid":"2496950","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130168643.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发工程师","job_title":"Java高级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2496950.html","company_name":"联合永道（上海）信息技术有限公司","providesalary_text":"1-1.5万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"5","issuedate":"2021-04-01 09:45:24","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 周末双休 节日福利 带薪年假 专业培训 弹性工作","jobwelf_list":["五险一金","餐饮补贴","周末双休","节日福利","带薪年假","专业培训","弹性工作"],"attribute_text":["北京-海淀区","3-4年经验","大专","招若干人"],"companysize_text":"500-1000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130585784","coid":"2630431","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/130585784.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2630431.html","company_name":"北京昆仑海岸传感技术有限公司","providesalary_text":"1.5-3万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"10","issuedate":"2021-04-01 09:40:39","isFromXyz":"","isIntern":"0","jobwelf":"做五休二 带薪年假 五险一金 绩效奖金","jobwelf_list":["做五休二","带薪年假","五险一金","绩效奖金"],"attribute_text":["北京-海淀区","无需经验","大专","招5人"],"companysize_text":"150-500人","companyind_text":"仪器仪表\/工业自动化","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"121127832","coid":"5800797","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/121127832.html?s=sou_sou_soulb&t=0","job_name":"Java中级开发工程师","job_title":"Java中级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5800797.html","company_name":"北京智盟信通科技有限公司","providesalary_text":"0.8-1.6万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 09:30:40","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 年终奖金 定期体检","jobwelf_list":["五险一金","餐饮补贴","年终奖金","定期体检"],"attribute_text":["北京","3-4年经验","本科","招4人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"108919124","coid":"5308460","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-ftq\/108919124.html?s=sou_sou_soulb&t=0","job_name":"Java工程师","job_title":"Java工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5308460.html","company_name":"北京联宇信通科技有限公司","providesalary_text":"5-7千\/月","workarea":"010600","workarea_text":"北京-丰台区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"4","issuedate":"2021-04-01 09:25:57","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 年终奖金 带薪年假 周末双休","jobwelf_list":["五险一金","餐饮补贴","年终奖金","带薪年假","周末双休"],"attribute_text":["北京-丰台区","2年经验","大专","招1人"],"companysize_text":"少于50人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130581544","coid":"5488639","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/130581544.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发","job_title":"Java高级开发","company_href":"https:\/\/jobs.51job.com\/all\/co5488639.html","company_name":"明略科技集团","providesalary_text":"1.9-3.5万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 09:12:54","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","3-4年经验","本科","招10人"],"companysize_text":"1000-5000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"127389850","coid":"2911570","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/127389850.html?s=sou_sou_soulb&t=0","job_name":"高级Java工程师","job_title":"高级Java工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2911570.html","company_name":"电讯盈科科技(北京)有限公司","providesalary_text":"3-4万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"6","issuedate":"2021-04-01 09:11:19","isFromXyz":"","isIntern":"0","jobwelf":"周末双休 弹性工作 意外险 节日福利 带薪年假 五险一金","jobwelf_list":["周末双休","弹性工作","意外险","节日福利","带薪年假","五险一金"],"attribute_text":["北京","5-7年经验","本科","招若干人"],"companysize_text":"10000人以上","companyind_text":"通信\/电信运营、增值服务","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129555687","coid":"2579807","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/129555687.html?s=sou_sou_soulb&t=0","job_name":"Java后端开发工程师","job_title":"Java后端开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2579807.html","company_name":"中国国际图书贸易集团有限公司","providesalary_text":"1-1.5万\/月","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"国企","degreefrom":"6","workyear":"3","issuedate":"2021-04-01 09:10:40","isFromXyz":"","isIntern":"0","jobwelf":"带薪年假 绩效奖金 餐饮补贴 高温补贴 定期体检 带薪培训 六险两金 年终奖金 工会福利","jobwelf_list":["带薪年假","绩效奖金","餐饮补贴","高温补贴","定期体检","带薪培训","六险两金","年终奖金","工会福利"],"attribute_text":["北京","1年经验","本科","招1人"],"companysize_text":"1000-5000人","companyind_text":"贸易\/进出口","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129521967","coid":"4466201","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/129521967.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co4466201.html","company_name":"北京医信天下数据技术有限公司","providesalary_text":"1-2万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 08:50:12","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 绩效奖金 年终奖金 带薪年假 周末双休 年底十三薪","jobwelf_list":["五险一金","绩效奖金","年终奖金","带薪年假","周末双休","年底十三薪"],"attribute_text":["北京-朝阳区","3-4年经验","本科","招1人"],"companysize_text":"50-150人","companyind_text":"互联网\/电子商务","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128945523","coid":"3551230","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-dcq\/128945523.html?s=sou_sou_soulb&t=0","job_name":"急招Java软件开发工程师","job_title":"急招Java软件开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co3551230.html","company_name":"北京创思恒通科技有限公司","providesalary_text":"0.8-1.5万\/月","workarea":"010100","workarea_text":"北京-东城区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"4","issuedate":"2021-04-01 08:30:31","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 专业培训 绩效奖金 交通补贴 公司团建 年终奖金","jobwelf_list":["五险一金","餐饮补贴","专业培训","绩效奖金","交通补贴","公司团建","年终奖金"],"attribute_text":["北京-东城区","2年经验","大专","招5人"],"companysize_text":"少于50人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128602339","coid":"5725901","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/128602339.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5725901.html","company_name":"航科院（北京）科技发展有限公司","providesalary_text":"1.5-2万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 08:30:22","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 年终奖金 定期体检 绩效奖金 专业培训","jobwelf_list":["五险一金","餐饮补贴","年终奖金","定期体检","绩效奖金","专业培训"],"attribute_text":["北京-朝阳区","3-4年经验","本科","招1人"],"companysize_text":"50-150人","companyind_text":"航天\/航空","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"123349952","coid":"5110289","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-cyq\/123349952.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发工程师","job_title":"Java高级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5110289.html","company_name":"北京优捷信达信息科技有限公司","providesalary_text":"1.3-1.8万\/月","workarea":"010500","workarea_text":"北京-朝阳区","updatedate":"04-01","iscommunicate":"","companytype_text":"合资","degreefrom":"6","workyear":"6","issuedate":"2021-04-01 07:22:34","isFromXyz":"","isIntern":"0","jobwelf":"周末双休 带薪年假 五险一金 全勤奖 节日福利 餐饮补贴","jobwelf_list":["周末双休","带薪年假","五险一金","全勤奖","节日福利","餐饮补贴"],"attribute_text":["北京-朝阳区","5-7年经验","本科","招若干人"],"companysize_text":"少于50人","companyind_text":"计算机服务(系统、数据服务、维修)","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129796678","coid":"6321310","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/129796678.html?s=sou_sou_soulb&t=0","job_name":"高级Java开发工程师","job_title":"高级Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co6321310.html","company_name":"北京轩宇信息技术有限公司","providesalary_text":"","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"国企","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 04:54:20","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","3-4年经验","本科","招2人"],"companysize_text":"","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":["xyz"],"ad_track":"","jobid":"127655184","coid":"6084594","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing\/127655184.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师（北京）","job_title":"Java开发工程师（北京）","company_href":"https:\/\/jobs.51job.com\/all\/co6084594.html","company_name":"北京京东世纪贸易有限公司","providesalary_text":"","workarea":"010000","workarea_text":"北京","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"10","issuedate":"2021-04-01 04:53:24","isFromXyz":"1","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京","无需经验","本科","招若干人"],"companysize_text":"","companyind_text":"贸易\/进出口","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"121268087","coid":"5832219","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-hdq\/121268087.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co5832219.html","company_name":"北京汉诺威尔能源科技有限公司","providesalary_text":"1-2万\/月","workarea":"010800","workarea_text":"北京-海淀区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 16:20:11","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 员工旅游 定期体检 年终奖金 绩效奖金 节日福利 商业保险 人文关怀","jobwelf_list":["五险一金","员工旅游","定期体检","年终奖金","绩效奖金","节日福利","商业保险","人文关怀"],"attribute_text":["北京-海淀区","3-4年经验","本科","招5人"],"companysize_text":"少于50人","companyind_text":"互联网\/电子商务","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"129625762","coid":"3122414","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-sjsq\/129625762.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co3122414.html","company_name":"北京扶远清隆科贸有限公司","providesalary_text":"0.8-1万\/月","workarea":"010700","workarea_text":"北京-石景山区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"6","workyear":"3","issuedate":"2021-04-01 15:44:14","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 员工旅游 交通补贴 专业培训 定期体检 绩效奖金 年终奖金 餐饮补贴 通讯补贴","jobwelf_list":["五险一金","员工旅游","交通补贴","专业培训","定期体检","绩效奖金","年终奖金","餐饮补贴","通讯补贴"],"attribute_text":["北京-石景山区","1年经验","本科","招1人"],"companysize_text":"150-500人","companyind_text":"医疗设备\/器械","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"128894443","coid":"4139728","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-syq\/128894443.html?s=sou_sou_soulb&t=0","job_name":"Java高级开发工程师","job_title":"Java高级开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co4139728.html","company_name":"北京鸿链科技有限公司","providesalary_text":"1.3-1.8万\/月","workarea":"011200","workarea_text":"北京-顺义区","updatedate":"04-01","iscommunicate":"","companytype_text":"合资","degreefrom":"6","workyear":"6","issuedate":"2021-04-01 15:06:14","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 绩效奖金 年终奖金 弹性工作 定期体检 双休 节日福利","jobwelf_list":["五险一金","绩效奖金","年终奖金","弹性工作","定期体检","双休","节日福利"],"attribute_text":["北京-顺义区","5-7年经验","本科","招5人"],"companysize_text":"50-150人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"130553568","coid":"105547","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-syq\/130553568.html?s=sou_sou_soulb&t=0","job_name":"北京-java工程师","job_title":"北京-java工程师","company_href":"https:\/\/jobs.51job.com\/all\/co105547.html","company_name":"北京先进数通信息技术股份公司","providesalary_text":"1-1.5万\/月","workarea":"011200","workarea_text":"北京-顺义区","updatedate":"04-01","iscommunicate":"","companytype_text":"上市公司","degreefrom":"6","workyear":"5","issuedate":"2021-04-01 14:29:00","isFromXyz":"","isIntern":"0","jobwelf":"五险一金 餐饮补贴 定期体检 年终奖金 生日礼金 节日福利 定期团建","jobwelf_list":["五险一金","餐饮补贴","定期体检","年终奖金","生日礼金","节日福利","定期团建"],"attribute_text":["北京-顺义区","3-4年经验","本科","招2人"],"companysize_text":"1000-5000人","companyind_text":"计算机软件","adid":""},{"type":"engine_search_result","jt":"0","tags":[],"ad_track":"","jobid":"102485248","coid":"2115192","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/beijing-ftq\/102485248.html?s=sou_sou_soulb&t=0","job_name":"Java开发工程师","job_title":"Java开发工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2115192.html","company_name":"北京友恒通科技有限责任公司","providesalary_text":"1.5-2.5万\/月","workarea":"010600","workarea_text":"北京-丰台区","updatedate":"04-01","iscommunicate":"","companytype_text":"民营公司","degreefrom":"5","workyear":"4","issuedate":"2021-04-01 14:03:00","isFromXyz":"","isIntern":"0","jobwelf":"","jobwelf_list":[""],"attribute_text":["北京-丰台区","2年经验","大专","招2人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""}],"jobid_count":"7356","banner_ads":"<div class=\"mainleft s_search search_btm0\" id=\"banner_ads\">\r\n                                        <table border=0 cellspacing=0 cellpadding=4><tr>\n\t<td><a adid=\"34817821\" onmousedown=\"return AdsClick(34817821)\" href=\"https:\/\/companyadc.51job.com\/companyads\/2020\/hz\/34817769\/index.htm\" title=\"浙江天下网商网络传媒有限公司\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img05.51jobcdn.com\/im\/images\/ads\/35\/34818\/34817821\/tx150-60.gif\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n\t<td><a adid=\"33917329\" onmousedown=\"return AdsClick(33917329)\" href=\"https:\/\/companyadc.51job.com\/companyads\/ads\/34\/33918\/33917329\/index.htm\" title=\"古驰（中国）贸易有限公司\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img05.51jobcdn.com\/im\/images\/ads\/34\/33918\/33917329\/gc60.gif\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n\t<td><a adid=\"33823418\" onmousedown=\"return AdsClick(33823418)\" href=\"https:\/\/companyadc.51job.com\/companyads\/ads\/34\/33824\/33823418\/index.htm\" title=\"奥乐齐商业（上海）有限公司\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img05.51jobcdn.com\/im\/images\/ads\/34\/33824\/33823418\/150.jpg\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n\t<td><a adid=\"34817799\" onmousedown=\"return AdsClick(34817799)\" href=\"https:\/\/companyadc.51job.com\/companyads\/2020\/nb\/34817765\/index.htm\" title=\"宁波生久柜锁有限公司\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img05.51jobcdn.com\/im\/images\/ads\/35\/34818\/34817799\/sj150-60.gif\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n\t<td><a adid=\"33645618\" onmousedown=\"return AdsClick(33645618)\" href=\"https:\/\/companyadc.51job.com\/companyads\/ads\/34\/33646\/33645586\/index.htm\" title=\"上海绿光教育培训有限公司\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img05.51jobcdn.com\/im\/images\/ads\/34\/33646\/33645618\/aa.gif\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n\t<td><a adid=\"\" onmousedown=\"return AdsClick()\" href=\"https:\/\/mkt.51job.com\/pc\/wechat\/index.html\" title=\"微信服务号\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img01.51jobcdn.com\/im\/mkt\/tg\/2018banner\/ggsc\/150_60.gif \" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\n<\/tr>\n<\/table>                    <table border=0 cellspacing=0 cellpadding=4>\r\n                        <tr>\r\n                            <td><a href=\"https:\/\/edu.51job.com\" target=\"_blank\" onfocus=\"blur()\"><img src=\"\/\/img04.51jobcdn.com\/im\/mkt\/zn\/train\/20200618\/ad\/eduad.png\" border=\"0\" width=\"150\" height=\"60\"><\/a><\/td>\r\n                        <\/tr>\r\n                    <\/table>\r\n                                <\/div>","is_collapseexpansion":"","co_ads":[],"keyword_recommendation":{"title":"猜你喜欢","data_type":"1","keyword":"java","data":[{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 开发","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 开发"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E9%25AB%2598%25E7%25BA%25A7,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 高级","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 高级"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E5%25AE%259E%25E4%25B9%25A0,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 实习","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 实习"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E5%2588%259D%25E7%25BA%25A7,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 初级","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 初级"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E4%25B8%25AD%25E7%25BA%25A7,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 中级","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 中级"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2BWeb,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java Web","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava Web"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E5%2590%258E%25E5%258F%25B0,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 后台","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 后台"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Java%2B%25E6%259E%25B6%25E6%259E%2584,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Java 架构","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJava 架构"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,J2EE,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"J2EE","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJ2EE"},{"href":"https:\/\/search.51job.com\/list\/010000,000000,0000,00,9,99,Javascript,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=","text":"Javascript","click":"15\u001a1\u001a1617269326368\u001a\u001ac49dbc1581b595d5b9415cf1e4649f05\u001a61.155.198.235\u001a1\u001ajava\u001aJava 开发,Java 高级,Java 实习,Java 初级,Java 中级,Java Web,Java 后台,Java 架构,J2EE,Javascript\u001aJavascript"}]},"search_condition":{"lang":"c","keywordtype":"2","ord_field":"0","jobarea":"010000","curr_page":"1","district":"000000","dibiaoid":"0","postchannel":"0000","reservechannel":"00000000","issuedate":"9","providesalary":"99","degreefrom":"99","companysize":"99","cotype":"99","workyear":"99","industrytype":"00","funtype":"0000","jobterm":"99","keyword":"java","welfare":"","address":"","line":"","confirmdate":"9","radius":"-1","lonlat":"0,0"},"searched_condition":"java(全文)+北京","curr_page":"1","total_page":"148","keyword_ads":[],"job_search_assistance":[{"url":"https:\/\/i.51job.com\/payservice\/optimizeresume\/introduce.php?lang=c&mark=jlyh_pcsearch","img":"\/\/img01.51jobcdn.com\/im\/mkt\/tg\/2021banner\/jl_3\/960_540.jpg?1615963439","txt":"一次完美简历升级，成为offer收割机","vtxt":"高薪求职第一步","startdate":"2021-02-01","enddate":"2021-12-31","indexform":"","isdefault":"0"},{"url":"http:\/\/trace.51job.com\/mktrace.php?tag=lagoupc001&u=aHR0cHM6Ly9lZHUuNTFqb2IuY29tL2xlc3Nvbl9kZXRhaWwucGhwP2xlc3NvbmlkPTM3MDA1&k=1723ecdccac56be829f70a5cf594c656","img":"\/\/img01.51jobcdn.com\/im\/mkt\/zn\/banner\/2020\/0916\/lg\/fenxi960.png?1613636635","txt":"数据分析薪资高、人才缺口大","vtxt":"Top20%学员大厂定向直推","startdate":"2021-02-01","enddate":"2021-12-31","indexform":"","isdefault":"0"},{"url":"https:\/\/edu.51job.com\/lesson_detail.php?lessonid=36401","img":"\/\/img01.51jobcdn.com\/im\/images\/2020\/bj\/1012\/1.png?1613636627","txt":"3天提升3大核心求职技能","vtxt":"简历制作 面试通关 职业规划","startdate":"2021-02-01","enddate":"2021-12-31","indexform":"","isdefault":"0"}],"seo_title":"【北京,java招聘，求职】-前程无忧","seo_description":"前程无忧为您提供最新最全的北京,java招聘，求职信息。网聚全国各城市的人才信息，找好工作，找好员工，上前程无忧。","seo_keywords":"找工作,求职,人才,招聘"}</script>
<div class="clear"></div>
<a href="#top" id="goTop" style="display: none;">回到<br>顶部</a>
<a href="//i.51job.com/userset/advice.php?from=search" target="_blank" class="dw_fb"></a>
<div class="bottombox">
    <div class="in">
        <div class="bmad">
            <!-- BANNER 广告 -->
            <div class="mainleft s_search search_btm0" id="banner_ads">
                                        <table border=0 cellspacing=0 cellpadding=4><tr>
	<td><a adid="34817821" onmousedown="return AdsClick(34817821)" href="https://companyadc.51job.com/companyads/2020/hz/34817769/index.htm" title="浙江天下网商网络传媒有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/35/34818/34817821/tx150-60.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33917329" onmousedown="return AdsClick(33917329)" href="https://companyadc.51job.com/companyads/ads/34/33918/33917329/index.htm" title="古驰（中国）贸易有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33918/33917329/gc60.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33823418" onmousedown="return AdsClick(33823418)" href="https://companyadc.51job.com/companyads/ads/34/33824/33823418/index.htm" title="奥乐齐商业（上海）有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33824/33823418/150.jpg" border="0" width="150" height="60"></a></td>
	<td><a adid="34817799" onmousedown="return AdsClick(34817799)" href="https://companyadc.51job.com/companyads/2020/nb/34817765/index.htm" title="宁波生久柜锁有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/35/34818/34817799/sj150-60.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33645618" onmousedown="return AdsClick(33645618)" href="https://companyadc.51job.com/companyads/ads/34/33646/33645586/index.htm" title="上海绿光教育培训有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33646/33645618/aa.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="" onmousedown="return AdsClick()" href="https://mkt.51job.com/pc/wechat/index.html" title="微信服务号" target="_blank" onfocus="blur()"><img src="//img01.51jobcdn.com/im/mkt/tg/2018banner/ggsc/150_60.gif " border="0" width="150" height="60"></a></td>
</tr>
</table>                    <table border=0 cellspacing=0 cellpadding=4>
                        <tr>
                            <td><a href="https://edu.51job.com" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/mkt/zn/train/20200618/ad/eduad.png" border="0" width="150" height="60"></a></td>
                        </tr>
                    </table>
                                </div>            <!-- 广告 end -->
            <div class="clearbox"></div>
        </div>
        <div class="tResult_bottom_roll  tResult_bottom_roll_w ">
            <!--地区招聘 start -->
            <div class="rollBox">
                <div  id="announcement">
    <div  id="announcementbody">
                                                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川招聘</a></li>                </ul>
            
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川人才网</a></li>                </ul>
            			<ul><li style="font-size:14px;color:#666;">简历模板</li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/">个人简历模板</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/fengmian/">简历封面</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/biaoge/">简历表格</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/jianlifanwen/">简历范文</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/jianliyangben/">简历样本</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/gaoxiao/">高校简历</a></li>
				<li class="st_one"><a target="_blank" href="https://jianli.51job.com/zhuanye/">专业简历</a></li>
			</ul>
    </div>
</div>            </div>
            <!--地区招聘 end-->
            <div class="rollBox">
    <h3>个人简历模版-简历指导</h3>
    <div class="rollBox_twoRow f14">
        <div id="resumeGuideTopicsBody">
        </div>
        <div id="resumeGuideTopics" style="display:none">
        <div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/fengmian/" title="简历封面"><strong>简历封面</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/fengmian/9795.html" title="[简历封面下载]机会">[简历封面下载]机...</a></li><li><a target="_blank" href="//jianli.51job.com/jianlifanwen/" title="简历范文"><strong>简历范文</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianlifanwen/14367.html" title="图书编目加工部主管简历范文">图书编目加工部主...</a></li><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1329.html" title="互联网开发个人简历表格">互联网开发个...</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/128.html" title="中国现当代文学简历样本">中国现当代文学简...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/193.html" title="南昌航空大学高校简历模版">南昌航空大学...</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/196.html" title="冶金工程专业">冶金工程专业</a></li><li><a target="_blank" href="//jianli.51job.com/xiaohui/" title="高校校徽下载"><strong>高校校徽下载</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/xiaohui/347.html" title="深圳大学">深圳大学</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/126.html" title="业务员简历样本">业务员简历样本</a></li></ul></div><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1323.html" title="电子商务专业本科毕业生个人简历表格">电子商务专业...</a></li><li><a target="_blank" href="//jianli.51job.com/xiaohui/" title="高校校徽下载"><strong>高校校徽下载</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/xiaohui/346.html" title="上海理工大学">上海理工大学</a></li><li><a target="_blank" href="//jianli.51job.com/fengmian/" title="简历封面"><strong>简历封面</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/fengmian/9801.html" title="[简历封面下载]激情">[简历封面下载]激...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/211.html" title="杭州师范大学高校简历模版">杭州师范大学...</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/187.html" title="经营管理专业">经营管理专业</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/104.html" title="人力资源总监简历样本">人力资源总监简历...</a></li><li><a target="_blank" href="//jianli.51job.com/jianlifanwen/" title="简历范文"><strong>简历范文</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianlifanwen/14356.html" title="商务总监简历范文">商务总监简历范文</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/192.html" title="广播电视新闻专业">广播电视新闻...</a></li></ul></div><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1271.html" title="应届毕业生个人简历表格">应届毕业生个...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/128.html" title="同济大学高校简历模版">同济大学高校...</a></li></ul></div>        </div>
    </div>
</div>        </div>
    </div>
</div>


<div class="footer">
    <div class="in">
        <div class="nag">
            <div class="e e_first">
                <label>销售热线：</label>400-886-0051&nbsp;&nbsp;027-87810888<br>
                <label>客服热线：</label>400-620-5100<br>
                <label>Email：</label><a href="mailto:club@51job.com" rel="external nofollow">club@51job.com</a>（个人）<br>
                <a href="mailto:hr@51job.com" rel="external nofollow">hr@51job.com</a>（公司）            </div>
            <div class="e">
                <strong>简介</strong><br>
                <a href="//www.51job.com/bo/AboutUs.php" target="_blank">关于我们</a><br>
                <a href="//www.51job.com/bo/service.php" target="_blank">服务声明</a><br>
                <a href="//www.51job.com/bo/private.php" target="_blank">隐私条款</a><br>
                <a href="https://media.51job.com/media.php" target="_blank">媒体报道</a><br>
                <a href="https://ir.51job.com/ir/IRMain.php" target="_blank">Investor Relations</a>
            </div>
            <div class="e">
                <strong>合作</strong><br>
                <a href="//www.51job.com/bo/jobs/new_joinus.php" target="_blank">加入我们</a><br>
                <a href="//www.51job.com/bo/contact.php" target="_blank">联系我们</a><br>
                <a href="//www.51job.com/link.php" target="_blank">友情链接</a>            </div>
            <div class="e">
                <strong>帮助</strong><br>
                <a href="https://help.51job.com/home.html" target="_blank">帮助中心</a><br>
                <a href="https://help.51job.com/qa.html?from=b" target="_blank">常见问题</a><br>
                <a href="https://help.51job.com/guide.html?from=d" target="_blank">新手引导</a>            </div>
            <div class="e">
                <strong>导航</strong><br>
                <a href="//www.51job.com/sitemap/site_Navigate.php" target="_blank">网站地图</a><br>
                <a href="https://search.51job.com" target="_blank">职位搜索</a><br>
                <a href="//i.51job.com/resume/resume_center.php?lang=c">简历中心</a>            </div>
            <div class="code c_first">
                <img width="80" height="80" src="//img06.51jobcdn.com/im/2016/code/new_app.png" alt="APP下载">
                <span><a href="http://app.51job.com/index.html">APP下载</a></span>
            </div>
            <div class="code">
                <img width="80" height="80" src="//img01.51jobcdn.com/im/2016/code/web_fuwuhao_bottom.png" alt="微信服务号">
                <span>微信服务号</span>
            </div>
            <div class="clear"></div>
        </div>

        <p class="note nag">
            <span>未经51Job同意，不得转载本网站之所有招聘信息及作品 | 无忧工作网版权所有&copy;1999-2021</span>
    </p>    </div>
</div>
</body>
</html><!--引用js-->
<script type="text/javascript" src="//js.51jobcdn.com/in/resource/js/2021/search/common.f182f3d4.js"></script>
<script type="text/javascript" src="//js.51jobcdn.com/in/resource/js/2021/search/index.b1d5970a.js"></script>
<script>
App.$on('fetchDataEnd', function (data) {
    $('#banner_ads').html(data.banner_ads);
});
</script>
'''

html = etree.HTML(text)
result = html.xpath("//script[@type='text/javascript']/text()")#将*改为li，表示只获取名称为li的子孙节点
print(str(result[0]).split("total_page\":\"")[1].split("\"")[0])


# print(result.decode('UTF-8'))