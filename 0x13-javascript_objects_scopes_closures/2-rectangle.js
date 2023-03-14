#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w === 'undefined' || typeof h === 'undefined') {
      // Do nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
