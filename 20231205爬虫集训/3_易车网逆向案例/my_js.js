
const crypto = require('crypto');

//1. 把这个函数补齐了
//2. 把调用函数用的e和t补齐了. 就可以了
function r(e, t) {
    if (!e.headers || !e.headers["x-platform"])
        return t.cid;
    var n = t.headerEncryptKeys.find(function(t) {
        return t.name == e.headers["x-platform"]
    });
    return n ? n.value : "DB2560A6EBC65F37A0484295CD4EDD25"
}

function my_md5(message){
    const hash = crypto.createHash('md5').update(message).digest('hex');
    return hash;
}

function s(e, t){
    var n = "";
    if ("headers" == e.encryptType) {
        var i = e.data ? JSON.stringify(e.data) : "{}"
          , o = r(e, t);
        n = "cid=" + t.cid + "&param=" + i + o + t.timestamp;

    } else {
        var a = [];  // js原生语法
        a.push("cid=" + t.cid),
        a.push("uid=" + t.uid),
        a.push("ver=" + t.ver),
        a.push("devid=" + (e.deviceId || "")),
        a.push("t=" + t.timestamp),
        a.push("key=" + t.paramsKey),
        n = a.join(";")
    }
    // 世界第一坑.
    // 看到是MD5的时候. 你应该高兴.
    // 你要注意. 现在很多网站为了反爬. 魔改md5.
    // 你需要去验证. 是否是标准的md5
    // https://1024tools.com/hash
    // 经过测试. 标准的md5
    console.log(n)
    var s = my_md5(n); // 貌似是一个md5
    return s
}

var e = {
    "url": "https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param",
    "data": {  // 思考. 这个东西真的是固定的么?? 留给你们...
        "cityId": "201",
        "serialId": "1661"
    },
    "headers": {
        "x-platform": "pc"
    },
    "method": "GET",
    "withCredentials": "true",
    "async": "true",
    "isParam": "true",
    "dataType": "json",
    "defaultContentType": "true",
    "encryptType": "headers",
    "isEncrypt": "false",
    "isBrush": "false",
    "proxy": "false",
    "timeout": 5000
}
var t = {
    "cid": "508", // 固定的
    "ver": "v10.80.0",  // 固定的
    "gradeParam": {},  // 固定的
    "uid": "",  // 固定的
    "headerEncryptKeys": [
        {
            "name": "pc",
            "value": "19DDD1FBDFF065D3A4DA777D2D7A81EC",
            "cid": "508"
        },
        {
            "name": "phone",
            "value": "DB2560A6EBC65F37A0484295CD4EDD25",
            "cid": "601"
        },
        {
            "name": "h5",
            "value": "745DFB2027E8418384A1F2EF1B54C9F5",
            "cid": "601"
        },
        {
            "name": "business_applet",
            "value": "64A1071F6C3C3CC68DABBF5A90669C0A",
            "cid": "601"
        },
        {
            "name": "wechat",
            "value": "AF23B0A6EBC65F37A0484395CE4EDD2K",
            "cid": "601"
        },
        {
            "name": "tencent",
            "value": "1615A9BDB0374D16AE9EBB3BBEE5353C",
            "cid": "750"
        }
    ],  // 固定的
    "paramsKey": "f48aa2d0-31e0-42a6-a7a0-64ba148262f0" // 固定的
}

function fn(){
    var headers = {}
    var tm = new Date().getTime()+"";
    t.timestamp = tm;
    headers['x-timestamp'] = tm;
    headers['x-sign'] = s(e, t);
    headers['x-city-id'] = "201";
    headers['x-ip-address'] = '120.244.62.183';
    headers['x-user-guid'] = '3b0fec58-e8fc-4a83-b1b6-672adbe11c76';
    headers['cid'] = "508";
    headers['x-platform'] = 'pc';  // 樵夫该死..
    return headers;
}

// 调试...
// sign = fn(e, t)
// console.log(sign)
