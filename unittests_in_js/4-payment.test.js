const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', function () {
  it('should stub Utils.calculateNumber and spy on console.log', function () {
    // Stub de la méthode
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy sur console.log
    const logSpy = sinon.spy(console, 'log');

    // Appel réel
    sendPaymentRequestToApi(100, 20);

    // Assertions
    sinon.assert.calledOnce(stub);
    sinon.assert.calledWith(stub, 'SUM', 100, 20);

    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 10');

    // Nettoyage
    stub.restore();
    logSpy.restore();
  });
});
