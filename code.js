var request = require('request');
var express = require('express');
var bodyParser = require('body-parser');
var app = express();


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(express.static(__dirname + '/static'));
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

app.post('/post', function (req, res) {
    var messageToRasa = req.body.query;
    if(!req.body) return res.sendStatus(400);
    console.log(messageToRasa);
    request.post(
      'http://localhost:5005/conversations/default/respond',
      { json: { query: messageToRasa} },
      function (error, response, body) {
          if (!error && response.statusCode == 200) {
              console.log(body[0].text)
          }
          else{
            console.log(`Error: \n${error}`);
          }
          res.json({user_query: messageToRasa, bot_response: (body[0].text !== undefined) ? body[0].text : "dunno what to say"});
          // res.end();
      }
  );

});


app.get('/', function (req, res) {
    res.render('index.ejs')
});



var server = app.listen(5005);