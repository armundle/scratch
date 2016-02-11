var express = require('express');
var app = express();

var birds = require('./birds');

app.get('/', function(req, res){
   res.send('Hello World!');
});

app.use('/birds', birds);

app.listen(3000, function(){
   console.log('Example app listening on port 3000!');
});

