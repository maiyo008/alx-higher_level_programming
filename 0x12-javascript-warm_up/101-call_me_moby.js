#!/usr/bin/node
global.callMeMoby = function (x, theFunction) {
  if (x < 1) return;
  theFunction();
  callMeMoby(x - 1, theFunction);
};
module.exports = { callMeMoby };
