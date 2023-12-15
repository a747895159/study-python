var crypto = require("crypto");
// 1. sha1计算, 使用nodejs完成该算法
function sha1(big_str){
    var x = crypto.createHash("sha1").update(big_str).digest("hex");
    return x;
}

// 2. 参数的拼接过程, 计算sha1 , token也就算出来了
function fn(t) {
    function e(t) {
        if (!t)
            return "";
        var e = [];
        return Object.keys(t).sort().map((function(n) {
            void 0 !== t[n] && e.push("".concat(n, "=").concat(t[n]))
        }
        )),
        e.join("&")
    }
    //   e(t) 把参数进行处理. 处理成另外一种格式的字符串.
    return sha1(e(t))  // p["a"]("大号字符串")
}
