#!/usr/bin/node
const fs = require('fs');
let arg = process.argv[2];
fs.readFile(arg, function(err, data){
	if (err) {
		console.log(err);
	}
	console.log(data);
});