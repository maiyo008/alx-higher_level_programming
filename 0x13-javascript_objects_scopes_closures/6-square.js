#!/sr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let printChar = '';
    if (typeof c === 'undefined') {
      printChar = 'X';
    } else {
      printChar = c;
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += printChar;
      }
      console.log(line);
    }
  }
}
module.exports = Square;
