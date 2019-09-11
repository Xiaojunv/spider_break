import re

import execjs
import requests,redis
from ip_pool.ip_redis import get_ip
from fake_useragent import UserAgent



def get_data(url):

    headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }


    data = requests.get(url,headers=headers,timeout=2)
    if data.status_code == 200:
        dytk = ''.join(re.findall("dytk: '(.+?)'",data.text))
        tac = ''.join(re.findall("<script>tac='(.+?)'</script>",data.text))
        uid = ''.join(re.findall('uid: "(.+?)"',data.text))
        # print(data.text)
        return dytk,tac,uid
    else:
        return get_data(url)




def get_dyList(dytk,tac,uid,url):

    js1  = """
    
    tac= '%s';
    function getdytk(){
        return '%s';
    }
    function getuid(){
        return '%s';
    }
    """%(tac,dytk,uid)

    js2= r"""
function generateSignature(userId) {
navigator = {
appCodeName: "Mozilla",
appMinorVersion: "0",
appName: "Netscape",
browserLanguage: "zh-CN",
cookieEnabled: true,
cpuClass: "x86",
language: "zh-CN",
maxTouchPoints: 0,
msManipulationViewsEnabled: true,
msMaxTouchPoints: 0,
msPointerEnabled: true,
onLine: true,
platform: "Win32",
pointerEnabled: true,
product: "Gecko",
systemLanguage: "zh-CN",
userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
userLanguage: "zh-CN",
vendor: "Google Inc.",
vendorSub: "",
webdriver: false
},
window = this,
window.navigator = navigator;
this.document = {}
var r = (function() {
function e(e, a, r) {
    return (b[e] || (b[e] = t("x,y", "return x " + e + " y")))(r, a)
}
function a(e, a, r) {
    return (k[r] || (k[r] = t("x,y", "return new x[y](" + Array(r + 1).join(",x[++y]").substr(1) + ")")))(e, a)
}
function r(e, a, r) {
    var n, t, s = {},
    b = s.d = r ? r.d + 1 : 0;
    for (s["$" + b] = s, t = 0; t < b; t++) s[n = "$" + t] = r[n];
    for (t = 0, b = s.length = a.length; t < b; t++) s[t] = a[t];
    return c(e, 0, s)
}
function c(t, b, k) {
    function u(e) {
        v[x++] = e
    }
    function f() {
        return g = t.charCodeAt(b++) - 32,
        t.substring(b, b += g)
    }
    function l() {
        try {
            y = c(t, b, k)
        } catch(e) {
            h = e,
            y = l
        }
    }
    for (var h, y, d, g, v = [], x = 0;;) switch (g = t.charCodeAt(b++) - 32) {
    case 1:
        u(!v[--x]);
        break;
    case 4:
        v[x++] = f();
        break;
    case 5:
        u(function(e) {
            var a = 0,
            r = e.length;
            return function() {
                var c = a < r;
                return c && u(e[a++]),
                c
            }
        } (v[--x]));
        break;
    case 6:
        y = v[--x],
        u(v[--x](y));
        break;
    case 8:
        if (g = t.charCodeAt(b++) - 32, l(), b += g, g = t.charCodeAt(b++) - 32, y === c) b += g;
        else if (y !== l) return y;
        break;
    case 9:
        v[x++] = c;
        break;
    case 10:
        u(s(v[--x]));
        break;
    case 11:
        y = v[--x],
        u(v[--x] + y);
        break;
    case 12:
        for (y = f(), d = [], g = 0; g < y.length; g++) d[g] = y.charCodeAt(g) ^ g + y.length;
        u(String.fromCharCode.apply(null, d));
        break;
    case 13:
        y = v[--x],
        h = delete v[--x][y];
        break;
    case 14:
        v[x++] = t.charCodeAt(b++) - 32;
        break;
    case 59:
        u((g = t.charCodeAt(b++) - 32) ? (y = x, v.slice(x -= g, y)) : []);
        break;
    case 61:
        u(v[--x][t.charCodeAt(b++) - 32]);
        break;
    case 62:
        g = v[--x],
        k[0] = 65599 * k[0] + k[1].charCodeAt(g) >>> 0;
        break;
    case 65:
        h = v[--x],
        y = v[--x],
        v[--x][y] = h;
        break;
    case 66:
        u(e(t.substr(b++, 1), v[--x], v[--x]));
        break;
    case 67:
        y = v[--x];
        d = v[--x];
        g = v[--x];
        u(g.x === c ? r(g.y, y, k) : g.apply(d, y));
        break;
    case 68:
        u(e((g = t.substr(b++, 1)) < "<" ? (b--, f()) : g + g, v[--x], v[--x]));
        break;
    case 70:
        u(!1);
        break;
    case 71:
        v[x++] = n;
        break;
    case 72:
        v[x++] = +f();
        break;
    case 73:
        u(parseInt(f(), 36));
        break;
    case 75:
        if (v[--x]) {
            b++;
            break
        }
    case 74:
        g = t.charCodeAt(b++) - 32 << 16 >> 16,
        b += g;
        break;
    case 76:
        u(k[t.charCodeAt(b++) - 32]);
        break;
    case 77:
        y = v[--x],
        u(v[--x][y]);
        break;
    case 78:
        g = t.charCodeAt(b++) - 32,
        u(a(v, x -= g + 1, g));
        break;
    case 79:
        g = t.charCodeAt(b++) - 32,
        u(k["$" + g]);
        break;
    case 81:
        h = v[--x],
        v[--x][f()] = h;
        break;
    case 82:
        u(v[--x][f()]);
        break;
    case 83:
        h = v[--x],
        k[t.charCodeAt(b++) - 32] = h;
        break;
    case 84:
        v[x++] = !0;
        break;
    case 85:
        v[x++] = void 0;
        break;
    case 86:
        u(v[x - 1]);
        break;
    case 88:
        h = v[--x],
        y = v[--x],
        v[x++] = h,
        v[x++] = y;
        break;
    case 89:
        u(function() {
            function e() {
                return r(e.y, arguments, k)
            }
            return e.y = f(),
            e.x = c,
            e
        } ());
        break;
    case 90:
        v[x++] = null;
        break;
    case 91:
        v[x++] = h;
        break;
    case 93:
        h = v[--x];
        break;
    case 0:
        return v[--x];
    default:
        u((g << 16 >> 16) - 16)
    }
}


var n = window;
var t = n.Function,
s = Object.keys ||
function(e) {
    var a = {},
    r = 0;
    for (var c in e) a[r++] = c;
    return a.length = r,
    a
},
b = {},
k = {};
return r;
})()
(decodeURI("gr$Daten%20%D0%98b/s!l%20y%CD%92y%C4%B9g,(lfi~ah%60%7Bmv,-n%7CjqewVxp%7Brvmmx,&eff%7Fkx%5B!cs%22l%22.Pq%25widthl%22@q&heightl%22vr*getContextx$%222d%5B!cs#l#,*;?%7Cu.%7Cuc%7Buq$fontl#vr(fillTextx$$%E9%BE%98%E0%B8%91%E0%B8%A0%EA%B2%BD2%3C%5B#c%7Dl#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802%5B%25c%7Dl#vr&strokex%5B%20c%7Dl%22v,)%7DeOmyoZB%5Dmx%5B%20cs!0s$l$Pb%3Ck7l%20l!r&lengthb%25%5El$1+s$j%02l%20%20s#i$1ek1s$gr#tack4)zgr#tac$!%20+0o!%5B#cj?o%20%5D!l$b%25s%22o%20%5D!l%22l$b*b%5E0d#%3E%3E%3Es!0s%25yA0s%22l%22l!r&lengthb%3Ck+l%22%5El%221+s%22j%05l%20%20s&l&z0l!$%20+%5B%22cs'(0l#i'1ps9wxb&s()%20&%7Bs)/s(gr&Stringr,fromCharCodes)0s*yWl%20._b&s%20o!%5D)l%20l%20Jb%3Ck$.aj;l%20.Tb%3Ck$.gj/l%20.%5Eb%3Ck&i%22-4j!%1F+&%20s+yPo!%5D+s!l!l%20Hd%3E&l!l%20Bd%3E&+l!l%20%3Cd%3E&+l!l%206d%3E&+l!l%20&+%20s,y=o!o!%5D/q%2213o!l%20q%2210o!%5D,l%202d%3E&%20s.%7Bs-yMo!o!%5D0q%2213o!%5D*Ld%3Cl%204d#%3E%3E%3Eb%7Cs!o!l%20q%2210o!%5D,l!&%20s/yIo!o!%5D.q%2213o!%5D,o!%5D*Jd%3Cl%206d#%3E%3E%3Eb%7C&o!%5D+l%20&+%20s0l-l!&l-l!i'1z141z4b/@d%3Cl%22b%7C&+l-l(l!b%5E&+l-l&zl'g,)gk%7Dejo%7B%7Fcm,)%7Cyn~Lij~em%5B%22cl$b%25@d%3Cl&zl'l%20$%20+%5B%22cl$b%25b%7C&+l-l%258d%3C@b%7Cl!b%5E&+%20q$sign%20"), [TAC={}]);
return TAC.sign(userId);
}
"""
    # keyword = 'https://www.iesdouyin.com/share/user/68793469235?sec_uid=MS4wLjABAAAAAnjLfa6tDSVxSTPnBPfpOkl9PL8X4kMhnCS_ER8PHcA&timestamp=1565859993https://www.iesdouyin.com/share/user/68793469235?sec_uid=MS4wLjABAAAAAnjLfa6tDSVxSTPnBPfpOkl9PL8X4kMhnCS_ER8PHcA&timestamp=1565859993'
    _signature = execjs.compile(js1+'\n'+js2).call("generateSignature",url)
    print(_signature)
    return _signature,dytk,uid


def get_dy(url):
    dytk,tac,uid = get_data(url)
    _signature, dytk, uid = get_dyList(dytk,tac,uid,url)
    print(_signature, dytk, uid)
    return _signature, dytk, uid

url = 'https://www.iesdouyin.com/share/user/68793469235?sec_uid=MS4wLjABAAAAAnjLfa6tDSVxSTPnBPfpOkl9PL8X4kMhnCS_ER8PHcA&timestamp=1565859993https://www.iesdouyin.com/share/user/68793469235?sec_uid=MS4wLjABAAAAAnjLfa6tDSVxSTPnBPfpOkl9PL8X4kMhnCS_ER8PHcA&timestamp=1565859993'
#
get_dy(url)
