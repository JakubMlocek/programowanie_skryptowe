var http = require("http");
var fs = require("fs");


async function CheckExistDirFile(response, filepath){
    fs.exists(filepath, (exists) => {
        if (exists) {
            fs.stat(filepath,  (err, stats) => {
                if (stats.isFile()){
                    fs.readFile(filepath, 'utf-8', (err,data) => {
                        response.write(`${data}`);
                        response.end();
                    })
                }
                else if (stats.isDirectory()) {
                    response.write(`${filepath} is a directory!`);
                    response.end();
                }
                else{
                    response.write(`${filepath} is neither file or directory!`);
                    response.end();
                }
            })
        } else {
            response.write(`${filepath} does not exist!`);
            response.end();
        }
    })
}



/**
	 * Handles incoming requests.
	 *
	 * @param {IncomingMessage} request - Input stream — contains data received from the browser, e.g. encoded contents of HTML form fields.
	 * @param {ServerResponse} response - Output stream — put in it data that you want to send back to the browser.
	 * The answer sent by this stream must consist of two parts: the header and the body.
	 * <ul>
	 *  <li>The header contains, among others, information about the type (MIME) of data contained in the body.
	 *  <li>The body contains the correct data, e.g. a form definition.
	 * </ul>
	*/
    function requestListener(request, response) {
        console.log("--------------------------------------");
        console.log("The relative URL of the current request: " + request.url + "\n");
        var url = new URL(request.url, `http://${request.headers.host}`); // Create the URL object
        if (url.pathname == '/submit') { // Processing the form content, if the relative URL is '/submit'
            /* ************************************************** */
            response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
            /* ************************************************** */
            console.log("Creating a response body");
            if (request.method == 'GET'){ // If the GET method was used to send data to the server
                CheckExistDirFile(response, url.searchParams.get('filepath'));
            } else { // If other method was used to send data to the server
                response.write(`This application does not support the ${request.method} method`);
                response.end();
            }
        }
        else { // Generating the form
            /* ************************************************** */
            console.log("Creating a response header")
            // Creating a response header — we inform the browser that the body of the response will be HTML text
            response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
            /* ************************************************** */
            console.log("Creating a response body");
            // and now we put an HTML form in the body of the answer
            response.write(`<form method="GET" action="/submit">
                                <label for="filepath">Give path for a file</label>
                                <input name="filepath">
                                <br>
                                <input type="submit">
                                <input type="reset">
                            </form>`);
            /* ************************************************** */
            console.log("Sending the response");
            response.end();  // The end of the response — send it to the browser
        }
    }
    
    /* ************************************************** */
    /* Main block
    /* ************************************************** */
    
    var server = http.createServer(requestListener); // The 'requestListener' function is defined above
    server.listen(8000);
    console.log("The server was started on port 8000");
    console.log("To stop the server, press 'CTRL + C'");