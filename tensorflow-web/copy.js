/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: http://gitlab.yzf.net/wuwenzhou
 * @Date: 2020-11-26 08:52:46
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-27 09:21:37
 */
var fs=require('fs');
// var stat=fs.stat;
// var copy=function(src,dst){
//     //读取目录
//     fs.readdir(src,function(err,paths){
//         console.log(paths)
//         if(err){
//             throw err;
//         }
//         paths.forEach(function(path){
//             var _src=src+'/'+path;
//             var _dst=dst+'/'+path;
//             var readable;
//             var writable;
//             stat(_src,function(err,st){
//                 if(err){
//                     throw err;
//                 }
//                 if(st.isFile()){
//                     readable=fs.createReadStream(_src);//创建读取流
//                     writable=fs.createWriteStream(_dst);//创建写入流
//                     readable.pipe(writable);
//                 }else if(st.isDirectory()){
//                     exists(_src,_dst,copy);
//                 }
//             });
//         });
//     });
// }
// var exists=function(src,dst,callback){
//     //测试某个路径下文件是否存在
//     fs.exists(dst,function(exists){
//         if(exists){//不存在
//             callback(src,dst);
//         }else{//存在
//             fs.mkdir(dst,function(){//创建目录
//                 callback(src,dst)
//             })
//         }
//     })
// }

// exists('./dist','../tensorflow-server/static',copy)

fs.copyFile('./dist/index.html','../tensorflow-server/static/index.html',function(err){
	if(err) {
    console.log('something wrong was happened')
  }else{
    console.log('copy file succeed');
  }
})
