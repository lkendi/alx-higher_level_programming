#!/usr/bin/node
global.callMeMoby = function (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
};
