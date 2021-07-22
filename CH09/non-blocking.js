// Non-blocking 非阻塞處理
function nonblock(done) {
    setTimeout(() => {
        done();
    }, 3000);
}

nonblock(function () {
    console.log("done...");
});
console.log("I like non-blocking!");