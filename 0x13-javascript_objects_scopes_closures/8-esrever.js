#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];
  for (let index = 0; index < list.length; index++) {
    out.unshift(list[index]);
  }
  return out;
};
