// No use of any template system
var express = require('express'),
  logger = require('morgan');
var app = express();
var x = 1;
var y = 2;

function checkExists(fpath) {
  try {
      if (fs.existsSync(fpath)) {
          return true
      }
      return false
  }
  catch (err) {
      return false
  }
}

function checkIsFile(fpath) {
  if (checkExists(fpath)) {
      if (fs.statSync(fpath).isFile()) {
          return true
      } else {
          return false
      }
  } else {
      return false
  }
}

function readFile(fpath) {
  if (checkIsFile(fpath)) {
      return fs.readFileSync(fpath, { encoding: 'utf8' })
  }
  else {
      return null
  }
}


// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
  res.send(`
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
        rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
        crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>${x} + ${y} = ${x + y}</h1>
    </main>
    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous">
    </script>
  </body>
</html>
`); // Send a response to the browser
});

app.get('/json/:path', (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  readFile(`operations/${req.params.path}`, 'utf-8', (error, json) => {
    if (error) return;
    const { operations } = JSON.parse(json);
    let end = 0;
    operations.forEach((op) => {
      switch (op.op) {
        case '*':
          res.write(`<p>${op.x} * ${op.y} = ${op.x * op.y}</p><br>`);
          break;
        case '+':
          res.write(`<p>${op.x} + ${op.y} = ${op.x + op.y}</p><br>`);
          break;
        case '-':
          res.write(`<p>${op.x} - ${op.y} = ${op.x - op.y}</p><br>`);
          break;
        case '/':
          res.write(`<p>${op.x} / ${op.y} = ${op.x / op.y}</p><br>`);
          break;
        default:
          res.write('ERROR');
      }
      end += 1;
      if (end == operations.length) res.end();
    });
  });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
  console.log('The application is available on port 3000');
}); 