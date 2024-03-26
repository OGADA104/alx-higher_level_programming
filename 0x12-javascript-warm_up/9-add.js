#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  const sum = Number(a) + Number(b);
  return sum;
}
const result = add(a, b);
console.log(result);
