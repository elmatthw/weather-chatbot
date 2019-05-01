var request = require('request');
var express = require('express');
var bodyParser = require('body-parser');
var app = express();


app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(express.static(__dirname));

app.post('/conversations/default/parse', function (req, res) {
    var messageToRasa = req.body.user_query;
    console.log(messageToRasa);
    request.post(
      'http://localhost:5005/conversations/default/respond',
      { json: { 'query': messageToRasa} },
      function (error, response, body) {
          if (!error && response.statusCode == 200) {
              //body[0].text is the reply from Rasa

              console.log(body[0].text)
              }
          else{
            console.log(`Error: \n${error}`);
          }
      }
  );
    res.redirect('/index.html')
});

/*
app.post('http://localhost:5005/conversations/default/respond', { json: {'query': messageToRasa},
    function (req, res) {
            if (res.statusCode === 200){
                console.log(req.body);
                console.log(body[0].text)
            }
            else {
                console.log('error')
            }
        }
    });
*/

app.get('/', function (req, res) {
    res.sendFile('/index.html')
});


// var messageToRasa = 'Tell me the weather in Warsaw';


var server = app.listen(5005);