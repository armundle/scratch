var express = require('express')
var router = express.Router();

router.use(function timeLog(req, res, next){
   console.log('Time: ', Date.now());
   next();
});

router.get('/', function(req, res){
   res.send('Birds Home Page');
});

router.get('/about', function(req, res){
   res.send('Birds About Page');
})

module.exports = router;
