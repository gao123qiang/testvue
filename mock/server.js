let http = require('http');
let fs = require('fs');
let url = require('url');

let sliders = require('./sliders.js');
function read(cb){
  fs.readFile('./book.json','utf8',function (err,data) {
    if(err || data.length === 0){
      cb([]);
    }else{
      cb(JSON.parse(data))
    }
  })
}
http.createServer((req,res) => {//解决跨域的问题，在后端加一个跨域头
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type,Content-Length, Authorization, Accept,X-Requested-With");
  res.setHeader("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
  res.setHeader("X-Powered-By",' 3.2.1');
  if(req.method==="OPTIONS") return res.end();
  let{pathname,query} = url.parse(req.url);
  if(pathname === "/sliders"){
    res.setHeader('Content-Type','aplication/json;charset=utf8');
    return res.end(JSON.stringify(sliders))
  }
  if(pathname === '/hot'){
    read(function (books) {
      let hot = books.reverse().slice(0,3);
      res.setHeader('Content-Type','aplication/json;charset=utf8');
      res.end(JSON.stringify(hot));
    });
    return
  }
}).listen(3000);



