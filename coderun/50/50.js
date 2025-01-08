const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const findMaxEl = (textArr) => {
    const dict = {};

    for (let word of textArr) {
        if (dict[word]) {
            dict[word] += 1;
        } else {
            dict[word] = 1;
        }
    }

    return Object.keys(dict).sort((a, b) => a.localeCompare(b)).reduce(
        (a, b) => dict[a] >= dict[b] ? a : b
    );
};


let inputText = [];

rl.on('line', (line) => {
    inputText.push(...line.trim().split(' '));
}).on('close', () => {
    console.log(findMaxEl(inputText));
});