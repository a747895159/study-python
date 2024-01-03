var crypto = require("crypto");


function fn(t) {
    function e(t) {
        if (!t)
            return "";
        let e = [];
        return Object.keys(t).sort().map((function (n) {
                void 0 !== t[n] && e.push("".concat(n, "=").concat(t[n]))
            }
        )),
            e.join("&")
    }

    return sha1(e(t))
}

function sha1(t) {
    console.log(t);
    //last_update_time=1702637362&platform=web&roll=gt&type=all
    let s = 'platform=web&roll=gt&type=all&last_update_time=1702637362'
    var x = crypto.createHash("sha1").update(s).digest("hex");
    return x;

}

param = {
    "type": "all",
    "last_update_time": "1702554924",
    "platform": "web"
}

let s = fn(param)
console.log(s)
