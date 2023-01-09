const assert = require('assert');

const firstArray = [1, 2, 3]
const secondArray = firstArray

// assert.equal
// assert.strictEqual
// assert.deepEqual
assert.deepStrictEqual(firstArray, secondArray)