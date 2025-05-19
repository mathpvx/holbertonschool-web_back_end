const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when passed (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when passed (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when passed (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return Error when dividing by 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });

  describe('Edge cases', function () {
    it('should round a = 1.5 up and b = 3.4 down', function () {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.4), 5);
    });
  });
});
