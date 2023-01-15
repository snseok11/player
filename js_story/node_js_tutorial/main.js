const mysql = require('mysql');

var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
function template_HTML(title, list, body, control){
    return `<!doctype html>
    <html>
    <head>
    <title>WEB1 - ${title}</title>
    <meta charset="utf-8">
    </head>
    <body>
    <h1><a href="/">WEB</a></h1>
    <ol>
        ${list}
    </ol>
    ${control}
    <h2>${title}</h2>
    ${body}
    </p>
    </body>
    </html>`
}

function template_List(file_list){
    var list = '<ul>';
    var i = 0;
    while(i < file_list.length){
        list = list + `<li><a href="/?id=${file_list[i]}">${file_list[i]}</a></li>`
        i = i + 1;
    }
    list = list+'</ul>'
    return list
}
function create_update(update){
    if(update == undefined){
        return `<h1><a href = "/create">create</a></h1>`
    }
    else {
        return `<p><h1><a href = "/create">create</a></h1></p>
        <p><h1><a href="/update?id=${update}">update</a></h1></p>`
    }
}

var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;
    var title = queryData.id;
    if(pathname == '/'){ /// 이 pathname 은 parameter 는 포함이 되질 않아
        if(queryData.id === undefined){
            fs.readdir('./data', function(err, filelist){
                var list = template_List(filelist);
                var title = 'Welcome';
                var data = 'Hello, node js root directory';
                var template = template_HTML(title, list, data, create_update());
                response.writeHead(200);
                response.end(template);
            })
        } else {
            fs.readdir('./data', function(err, filelist){
                fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, data){
                    var list = template_List(filelist);
                    var title = queryData.id;
                    var template = template_HTML(title, list, data, create_update(title));
                    response.writeHead(200);
                    response.end(template);
                })
            })
        }   
    }
    else if (pathname === '/create'){
        fs.readdir('./data', function(err, filelist){
            var list = template_List(filelist);
            var title = 'WEB-create';
            var template = template_HTML(title, list, `
            <form action="create_process" method="post">
                <p><input type="text" name="title_name"></p>
                <p><textarea name="description" id="" cols="30" rows="10">
                </textarea></p>
                <p><input type="submit"></p>
            </form>
            `, create_update(queryData.id));
            response.writeHead(200);
            response.end(template);});
    }
    else if (pathname === '/create_process'){
        response.writeHead(200);
        var body = '';
        request.on('data', function(data){
            body = body+data;
        });
        request.on('end', function(){
            var post = qs.parse(body);
            fs.writeFile(`data/${post.title_name}`, post.description, 'utf-8', function(err){
                response.writeHead(302, {location : `/?id = ${post.title_name}`});
                response.end('success');
            });
        });
    }
    else if (pathname ==='/update'){
        
        fs.readdir('./data', function(err, filelist){
            fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, data){
                var list = template_List(filelist);
                var title = queryData.id;
                var template = template_HTML(title, list, data, create_update(title));
                response.writeHead(200);
                response.end(template);
            })
        })
    }
    else {
        response.writeHead(200);
        response.end('not found');
    }
});
app.listen(3000);

// response.end(fs.readFileSync(__dirname + _url)); ///얘네가 읽어줌
