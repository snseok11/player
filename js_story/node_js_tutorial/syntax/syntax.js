// var args = process.argv;
// console.log(args);

// var arr =['A', 'B', 'C'];
// console.log(arr);
// arr[2] = 3;
// console.log(arr);
// arr.pop();
// console.log(arr);

// const testFolder = '../data';
// var fs = require('fs');

// fs.readdir(testFolder, function(err, filelist){
//     console.log(filelist);
// });


// console.log('A');
// var fs = require('fs');
// var result = fs.readFileSync('./sample.txt', 'utf8');
// console.log(result);
// console.log('B');
// 결과값 : A -> result -> B 동기


// console.log('A');
// var fs = require('fs');
// fs.readFile('./sample.txt', 'utf8', function(err, result){
//     console.log(result);
// });
// console.log('B');
/// 결과 값 : A -> B -> result 비동기


// var a = function(){
//     console.log('A');
// }

// function slowfunc(callback){
//     callback();
// }
// slowfunc(a);
// CallBack 방식