const fs = require('fs');
const path = require('path');
function delDir(path){
    let files = [];
    if(fs.existsSync(path)){
        files = fs.readdirSync(path);
        files.forEach((file, index) => {
            let curPath = path + "/" + file;
            if(fs.statSync(curPath).isDirectory()){
                delDir(curPath); //递归删除文件夹
            } else {
                fs.unlinkSync(curPath); //删除文件
            }
        });
        fs.rmdirSync(path);  // 删除文件夹自身
    }
}
// 获取web 目录
let webPath = path.resolve(__dirname, '../gateway-server/web');
console.log(webPath);
// 清除开始
delDir(webPath)
console.log("清除完成")