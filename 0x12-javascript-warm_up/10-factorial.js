#!/usr/bin/node

function fact (num) {
  if ((isNaN(num)) || (num === 1)) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

console.log(fact(parseInt(process.argv[2])));
