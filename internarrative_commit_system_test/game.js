let strengths = {};

for (let i = 0; i <= 7; i++) {
  strengths[i] = 200;
}

strengths[7] = 0;

let step = 0;

setInterval(function () {
  for (let i = 1; i <= 7; i++) {
    strengths[i - 1] += strengths[i] *
    2 ** Math.floor(Math.log(strengths[0]) / Math.log(7) / i) *
    2 ** Math.floor(Math.log(strengths[i - 1]) / Math.log(7 / 6) / 343);
  }
  if (step % 10 === 0) {
    console.log(step, strengths);
  }
  step++;
}, 100);
