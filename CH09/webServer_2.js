const http = require('http');
const config = require('./config').config;

const server = http.createServer((req, res) => {
	res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
	res.end('<h1><center> I Love Node.js! </center></h1>');
});

server.listen(config.port, config.hostname, () => {
    console.log(`Server running at http://${config.hostname}:${config.port}/`);
});
