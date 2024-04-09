#!/usr/bin/node
let secondBiggest = 0;

if (process.argv.length <= 2) {
  console.log(0);
} else {
  let biggest = parseInt(process.argv[2]);
  let i = 3;
  while (i < process.argv.length) {
    const current = parseInt(process.argv[i]);
    if (current > biggest) {
      secondBiggest = biggest;
      biggest = current;
    } else if (current > secondBiggest && current !== biggest) {
      secondBiggest = current;
    }
    i++;
  }
  console.log(secondBiggest);
}
