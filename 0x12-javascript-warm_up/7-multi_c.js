#!/usr/bin/node
const x = parseInt(process.argv[2]);
const s = 'C is fun';

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log(s);
  }
} else {
  console.log('Missing number of occurrences');
}
