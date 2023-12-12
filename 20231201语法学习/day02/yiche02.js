// 注释走起

const crypto = require('crypto');

const e = {
    // "url": "https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param",
    // "data": {
    //     "cityId": "2401",
    //     "serialId": "1661"
    // },
    "headers": {
        "x-platform": "pc"
    },
    // "method": "GET",
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
};

const t = {
    "cid": "508",
    // "ver": "v10.80.0",
    // "timestamp": 1702351498582,
    "gradeParam": {},
    "uid": "",
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
    ],
    "paramsKey": "f48aa2d0-31e0-42a6-a7a0-64ba148262f0"
};


function s(e, t) {
    let n;
    if ("headers" === e.encryptType) {
        let i = e.data ? JSON.stringify(e.data) : "{}"
            , o = r(e, t);
        n = "cid=" + t.cid + "&param=" + i + o + t.timestamp
    } else {
        let a = [];
        a.push("cid=" + t.cid);
        a.push("uid=" + t.uid);
        a.push("ver=" + t.ver);
        a.push("devid=" + (e.deviceId || ""));
        a.push("t=" + t.timestamp);
        a.push("key=" + t.paramsKey);
        n = a.join(";")
    }
    let s = my_md5(n);
    return s
}

function my_md5(message) {
    const hash = crypto.createHash('md5').update(message).digest('hex');
    return hash;
}

function r(e, t) {
    if (!e.headers || !e.headers["x-platform"])
        return t.cid;
    let n = t.headerEncryptKeys.find(function (t) {
        return t.name === e.headers["x-platform"]
    });
    return n ? n.value : "DB2560A6EBC65F37A0484295CD4EDD25"
}

function fn(url,edata,method,ver,cityId) {
    e.url=url;
    e.data= edata;
    e.method=method;
    t.ver=ver;
    let headers = {};
    let timestamp = new Date().getTime() + "";
    t.timestamp = timestamp;
    headers['x-timestamp'] = timestamp;
    headers['x-sign'] = s(e, t);
    headers['x-city-id'] = cityId;
    headers['x-ip-address'] = '116.234.204.97';
    headers['x-user-guid'] = '3dcb90cecba7cc71d726327861b0161fa';
    headers['cid'] = "508";
    headers['x-platform'] = 'pc';

    return headers;
}

function add(a,b){
    return a+b;
}