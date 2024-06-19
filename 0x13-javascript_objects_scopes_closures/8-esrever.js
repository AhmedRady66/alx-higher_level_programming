#!/usr/bin/node

exports.esrever = function (list) {
  let out = [];
  for (let index = 0; index < list.length; index++) {
    out.unshift(list[index]);
  }
  return out;
};
