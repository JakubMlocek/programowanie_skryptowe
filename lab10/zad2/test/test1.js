var assert = require('assert'); 
var fs_script = require('../fsscript.js');

describe('Zaj10', function () {
  describe('Zad2', function () {
    describe('The checkExists() function', function () {
      it('Returns true for existing file', function () {
        assert.strictEqual(fs_script.checkExists('pliczek.txt'), true)
      });
      it('Returns true for existing dir', function () {
        assert.strictEqual(fs_script.checkExists('./test'), true)
      });
      it('Returns false for nonexistent dir/file', function () {
        assert.strictEqual(fs_script.checkExists('no_such_file.rnd'), false)
      });
    });

    describe('The checkIsDir() function', function () {
      it('Returns true for existing dir', function () {
        assert.strictEqual(fs_script.checkIsDir('./test'), true)
      });
      it('Returns false for existing file', function () {
        assert.strictEqual(fs_script.checkIsDir('pliczek.txt'), false)
      });
      it('Returns false for nonexistent dir/file', function () {
        assert.strictEqual(fs_script.checkIsDir('no_such_file'), false)
      });
    });

    describe('The checkIsFile() function', function () {
      it('Returns true for existing file', function () {
        assert.strictEqual(fs_script.checkIsFile('pliczek.txt'), true)
      });
      it('Returns false for existing dir', function () {
        assert.strictEqual(fs_script.checkIsFile('./test'), false)
      });
      it('Returns false for nonexistent dir/file', function () {
        assert.strictEqual(fs_script.checkIsFile('no_such_file'), false)
      });
    });

    describe('The readFile() function', function () {
      it('Returns file contents for existing file', function () {
        assert.strictEqual(fs_script.readFile('pliczek.txt'), 'test')
      });
      it('Returns null for existing dir', function () {
        assert.strictEqual(fs_script.readFile('./test'), null)
      });
      it('Returns null for nonexistent dir/file', function () {
        assert.strictEqual(fs_script.readFile('no_such_file'), null)
      });
    });
  });
});