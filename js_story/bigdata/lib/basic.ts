

const basic = {
    http : require('http'),
    fs : require('fs'),
    url : require('url'),
    qs : require('querystring'),
}

const create_db  =  function(db_name : string){this.conn.connect(function(err){
        if (err) throw err;
        console.log("connected!");
        db_name = `CREATE DATABASE ${db_name}`;
        this.conn(this.password_is).query(db_name, function(err,result){
            if (err) throw err;
            console.log('create database!');
        });
    })}

const db  = {
    password_is : Number,
    db_is : String,
    mysql : require('mysql'),
    conn : function(pass_word : string, db_name : string | undefined){
        if(db_name === undefined){
            this.mysql.createConnection({
                host : 'localhost',
                user : 'node_js',
                password : `${pass_word}`});
            this.password_is = pass_word;
        }
        else{
            this.mysql.createConnection({
                host : 'localhost',
                user : 'node_js',
                password : `${pass_word}`,
                database : `${db_name}`});
            this.password_is = pass_word;
            this.db_is = db_name;
        }},
    create_tb : function(table_name : string, row : any[]){
        var row_list = '\t(';
        for(var i = 0; i++; i < row.length){
            if(row[i] === String){
                row_list = row_list + row[i] + '\t VARCHAR(255),';
            }
            else{
                row_list = row_list + row[i] + '\t INT(20) NOT NULL';
            }
        }
        row_list = row_list + ')';
        this.conn(this.password_is, this.db_is).connect(function(err){
            if (err) throw err;
            var sql = `CREATE TABLE ${table_name} ${row_list}`;
            this.conn.query(sql, function (err, result) {
            if (err) throw err;
            console.log("Table created");})});
    },
}


export {basic, create_db, db}