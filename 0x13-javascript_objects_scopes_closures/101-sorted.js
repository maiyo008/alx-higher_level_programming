#!/usr/bin/node
const dict = require('./101-data').dict;
const usersByOccurrence = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (!(occurrence in usersByOccurrence)) {
    usersByOccurrence[occurrence] = [];
  }
  usersByOccurrence[occurrence].push(userId);
}
console.log(usersByOccurrence);
