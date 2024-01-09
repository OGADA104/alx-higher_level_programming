#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const fact = num > 0 ? factorial(num) : undefined;
console.log(`${fact}`);
