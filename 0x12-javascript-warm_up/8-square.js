#!/usr/bin/node

const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < x; index++) {
    console.log('x'.repeat(x));
  }
}
