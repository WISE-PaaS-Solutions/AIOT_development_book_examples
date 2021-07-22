// Blocking - 阻塞處理
function block() {
    var start = new Date().getTime();
    while (new Date().getTime() < start + 3000);

    console.log("done...");
}
// 呼叫 block() 函數
block();
console.log("I hate blocking!");