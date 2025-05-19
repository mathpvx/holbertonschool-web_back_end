const request = require('request');
const { expect } = require('chai');

describe('POST /login', () => {
  it('should return Welcome Betty', (done) => {
    request.post({
      url: 'http://localhost:7865/login',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ userName: 'Betty' })
    }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});

describe('GET /available_payments', () => {
  it('should return correct payment methods', (done) => {
    request.get('http://localhost:7865/available_payments', { json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});
