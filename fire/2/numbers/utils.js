let notifyPriority = 0;

let times = [['second', 60], ['minute', 60], ['hour', 24], ['day', 30], ['month', 12], ['year', 1000]];

let processPhrase = function (num, places, what, plural) {
  let m = (typeof num === 'number') ? 'toFixed' : 'toStr';
  return (num === Math.round(num) ? num : num[m](places)) + ' ' + (num === 1 ? what : (plural || what + 's'));
}

let formatTime = function (x) {
  x = x / 1000;
  let r = [];
  for (let [i, num] of times) {
    let v = x % num;
    x -= v;
    x /= num;
    r.push([v, 3, i]);
  }
  let s = [processPhrase(...r[0]), ', and '];
  for (let i of r.slice(1)) {
    s.push(processPhrase(...i));
    s.push(', ');
  }
  s.pop();
  return s.reverse().join('');
}

let get = function (d, k, def) {
  return (k in d) ? d[k] : def;
}

let notify = function (text, color, priority) {
  if (notifyPriority > priority) {
    return;
  }
  let n = document.getElementById('notify');
  n.style.color = color;
  n.innerHTML = text;
  setTimeout(function () {
    if (n.innerHTML === text) {
      n.innerHTML = '';
      notifyPriority = 0;
    }
  }, 3000);
}

let title = function (x) {
  return x[0].toUpperCase() + x.slice(1).toLowerCase();
}

export {title, get, processPhrase, formatTime, notify};
