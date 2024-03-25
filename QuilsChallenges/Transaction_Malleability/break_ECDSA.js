const EC = require('elliptic').ec;
const ec = new EC('secp256k1');

const ecparams = ec.curve;
const BN = require('bn.js');
const n = new BN(ecparams.n);
const private_key = BigInt("123627363487254893530457035545151564891328978956221587879562115");
const public_key = ec.keyFromPrivate(private_key).getPublic();

// console.log(public_key);

const msg = 1n;
const sig = ec.keyFromPrivate(private_key).sign(msg);

console.log(ec.verify(msg, sig, public_key));

// Transaction Malleability

const s = new BN(sig.s);

const sig2 = { r: sig.r, s: n.sub(s) };

console.log(ec.verify(msg, sig2, public_key));


