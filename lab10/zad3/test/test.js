//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8000");

// UNIT test begin
describe('lab10', function () {
  describe('Zad3', function () {
    describe('GET /submit?filepath=pliczek.txt', function () {
      it('respond with contents of pliczek.txt', function (done) {
        server
          .get('/submit?filepath=pliczek.txt')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "tojestzawartosc", done);
      });
    });

    describe('GET /submit?filepath=test', function () {
      it('respond with "test is a directory!"', function (done) {
        server
          .get('/submit?filepath=test')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "test is a directory!", done);
      });
    });

    describe('GET /submit?filepath=no_such_file', function () {
      it('respond with "no_such_file does not exist!"', function (done) {
        server
          .get('/submit?filepath=no_such_file')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "no_such_file does not exist!", done);
      });
    });
  });
});