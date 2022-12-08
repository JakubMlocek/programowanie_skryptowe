"use strict";

var expect = chai.expect;

"use strict";
var gsum = 0;

function isNumber(char) {
    if (typeof char !== 'string') {
      return false;
    }
    if (char.trim() === '') {
      return false;
    }
    return !isNaN(char);
}

function cyfry(napis){
    var sum = 0;
    for(var i = 0; i < napis.length; i++){
        if(isNumber(napis[i])){
            sum += parseInt(napis[i],10);
        }
    }
    return sum;
}

function litery(napis){
    var counter = 0;
    for(var i = 0; i < napis.length; i++){
        if(!isNumber(napis[i])){
            counter += 1;
        }
    }
    return counter;
}

function suma(napis){
    if(isNumber(napis[0])){
        gsum += cyfry(napis);
    }
    return gsum;
}

describe('Test functions for lab8 preparation', function(){
  describe('The cyfry() function', function() {
    it('returns sum of nums in line (Same cyfry)', function() {
      expect(cyfry("1111")).to.equal(4);
    });
    it('returns sum of nums in line (Same litery)', function() {
      expect(cyfry("abcd")).to.equal(0);
    });
    it('returns sum of nums in line (Litery, a po nich cyfry)', function() {
      expect(cyfry("abcd1234")).to.equal(10);
    });
    it('returns sum of nums in line (Cyfry, a po nich litery)', function() {
      expect(cyfry("1234abcd")).to.equal(10);
    });
    it('returns sum of nums in line (Pusty napis)', function() {
      expect(cyfry("")).to.equal(0);
    }); 
  });

  describe('The litery() function', function() {
    it('returns num of letters in line (Same cyfry)', function() {
      expect(litery("1111")).to.equal(0);
    });
    it('returns num of letters in line (Same litery)', function() {
    expect(litery("abcd")).to.equal(4);
    });
    it('returns num of letters in line (Litery, a po nich cyfry)', function() {
    expect(litery("abcd1234")).to.equal(4);
    });
    it('returns num of letters in line (Cyfry, a po nich litery)', function() {
    expect(litery("1234abcd")).to.equal(4);
    });
    it('returns num of letters in line (Pusty napis)', function() {
    expect(litery("")).to.equal(0);
    });
  });


  describe('The suma() function', function() {
    gsum = 0;
    it('returns sum of all nums in all lines (Same cyfry)', function() {
      expect(suma("1111")).to.equal(4);
    });
    it('returns sum of all nums in all lines (Same litery)', function() {
      expect(suma("abcd")).to.equal(4);
    });
    it('returns sum of all nums in all lines (Litery, a po nich cyfry)', function() {
      expect(suma("abcd1234")).to.equal(4);
    });
    it('returns sum of all nums in all lines (Cyfry, a po nich litery)', function() {
      expect(suma("1234abcd")).to.equal(14);
    });
    it('returns sum of all nums in all lines (Pusty napis)', function() {
      expect(suma("")).to.equal(14);
    });
  });
});