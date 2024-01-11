#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return constructor.name + '{}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const width = this.height;
    const height = this.width;
    this.height = height;
    this.width = width;
  }

  double () {
    const width = this.width;
    const height = this.height;
    this.height = height * 2;
    this.width = width * 2;
  }
}
module.exports = Rectangle;
