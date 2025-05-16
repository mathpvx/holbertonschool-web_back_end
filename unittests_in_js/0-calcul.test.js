const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return 4 when passed (1, 3)', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 when passed (1, 3.7)', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 when passed (1.2, 3.7)', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 when passed (1.5, 3.7)', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });
});