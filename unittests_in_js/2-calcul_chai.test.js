const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when passed (1.4, 4.5)', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when passed (1.4, 4.5)', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when passed (1.4, 4.5)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return Error when dividing by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });

  describe('Edge cases', function () {
    it('should round a = 1.5 up and b = 3.4 down', function () {
      expect(calculateNumber('SUM', 1.5, 3.4)).to.equal(5);
    });
  });
});
