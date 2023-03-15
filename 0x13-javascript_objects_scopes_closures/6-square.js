#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    super.print(c);
  }
}
module.exports = Square;
