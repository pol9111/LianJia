
var s = 'https://gateway.LianJia.com/wukong/ershoufang/search?city_id=350200&condition=&query=&order=&offset=0&limit=10'
var a = s.split("?")[0].split("://")[1]
var o = a.split("/")[0] // host
var p = a.split(o)[1] // path
// console.log(a ,  o , p ,)
var u = String(Math.random()) // nonce
var c = parseInt((new Date).getTime() / 1e3) // timestamp
console.log(u ,  c ,)
var r = 'get'
var r = (r = r || "GET").toUpperCase(); // method

var n = {
	'city_id': '350200',
	'condition': '',
	'query': '',
	'order': '',
	'offset': '0',
	'limit':  '10',
} // query
var i = ''
n && Object.keys(n).sort().map(function (e) {
			i += e + "=" + n[e] + "&"
		})
// console.log(i)
i = i.substr(0, i.length - 1)

var l = ["accessKeyId=wukong", "nonce=" + u, "timestamp=" + c
, "method=" + r, "path=" + p, "host=" + o.split(":"	)[0].toUpperCase()]
i && "GET" === r && l.push("query=" + i);
// console.log(l)
var m = l.sort().join("&");
// console.log(m)


var CryptoJS = require("crypto-js/index.js");
var rst = CryptoJS.HmacSHA256(m, "lMl0XOUNSExcUYtw").toString(CryptoJS.enc.Base64)
// var rst = CryptoJS.HmacSHA256(m, "lMl0XOUNSExcUYtw")
console.log(rst);


var CryptoJS = require("crypto-js/index.js");
var rst = CryptoJS.HmacSHA256(m, "lMl0XOUNSExcUYtw").toString(CryptoJS.enc.Base64)
// var rst = CryptoJS.HmacSHA256(m, "lMl0XOUNSExcUYtw")
console.log(rst);


