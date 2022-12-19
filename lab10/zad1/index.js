const op = require('./module');

/** Getting input from user */
const args = process.argv.slice(2);
const o = new op.Operation(Number(args[0]), Number(args[1]));

/** Printing sum of arguments */
console.log(o.sum());
