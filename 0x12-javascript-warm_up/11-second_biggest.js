#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

function findSecondBiggest (list) {
  if (list.length < 2) {
    return 0;
  }
  const max = Math.max(...list);
  list = list.filter(num => num !== max);
  return Math.max(...list);
}

console.log(findSecondBiggest(args));
