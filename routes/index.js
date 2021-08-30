var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.send("Hello There or 안녕하세요, welcome to the root route for the backend of this application, Talk To Me In Korean-React. If you require more information please visit `github repo link` ");
});

module.exports = router;
