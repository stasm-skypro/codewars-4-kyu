function countSmileys(arr) {
    const regex = /^[:;][-~]?[)D]$/;
    return arr.filter((face) => regex.test(face)).lenth;
}


// testing case
assert.strictEqual(countSmileys([]                             ), 0);
assert.strictEqual(countSmileys([':D',':~)',';~D',':)']        ), 4);
assert.strictEqual(countSmileys([':)',':(',':D',':O',':;']     ), 2);
assert.strictEqual(countSmileys([';]', ':[', ';*', ':$', ';-D']), 1);