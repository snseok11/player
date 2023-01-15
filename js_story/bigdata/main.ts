import {basic, db} from "./lib/basic";

const mysql = db.conn('949551', undefined);
var app = basic.http.createServer(function(request,response){
    var _url = request.url;
    var queryData = basic.url.parse(_url, true).query;
    var pathname = basic.url.parse(_url, true).pathname;
    if(pathname === '/'){
        if(queryData.id=== undefined){
            
        }
    }

});

app.listen(3000);
