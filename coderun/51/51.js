const findMaxEl = (textArr) => {
    const dict = {};
    let result = [];

    for (let word of textArr) {
        if (dict[word] !== undefined) {
            dict[word] += 1;
        } else {
            dict[word] = 0;
        }

        result.push(dict[word]);
    }

    return result.join(' ');
}

const fs = require('fs');
const text = fs.readFileSync('input.txt', 'utf-8').trim().split(/\s+/);

if (text[0] === '') return [];

console.log(findMaxEl(text));