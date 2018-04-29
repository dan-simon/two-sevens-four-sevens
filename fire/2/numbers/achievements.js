import {notify} from './utils.js';

let achievements = [
  [
    {'name': 'You just one the game!', 'desc': 'Get a one.'},
    {'name': 'This achievement is two hard', 'desc': 'Get a two.'},
    {'name': 'This game was made for you and three', 'desc': 'Get a three.'},
    {'name': 'Four great justice', 'desc': 'Get a four.'},
    {'name': 'Staying afive', 'desc': 'Get a five.'},
    {'name': 'This achievement name makes me six', 'desc': 'Get a six.'},
    {'name': 'Sevenly', 'desc': 'Get a seven.'}
  ], [
    {'name': 'You gotta start somewhere', 'desc': 'Click.'},
    {'name': "That's a lot of clicks", 'desc': 'Click 100 times. Reward: Clicks are 2x stronger.'},
    {'name': 'That sounds a bit shifty', 'desc': 'Shift.'},
    {'name': 'A million is a lot', 'desc': 'Get 1e6 zeros. Reward: Ones are 2x stronger.'},
    {'name': "Where's eight?", 'desc': 'Have exactly 77 sevens. Reward: Sevens are 7/6x stronger.'},
    {'name': 'Sevens add and multiply', 'desc': 'Get sevens multiplier to at least 1000.\nReward: Sevens are again 7/6x stronger.'},
    {'name': 'You need a boost', 'desc': 'Boost.'}
  ], [
    {'name': 'All at once', 'desc': 'Buy at least 343 ones at once.'},
    {'name': "That's a lot of boosts", 'desc': 'Boost 10 times.'},
    {'name': "What's the point of doing that?", 'desc': "Buy a single one when you've bought\nat least 2401. Reward: each one bought gives a 2401/2400 boost to\none production."},
    {'name': 'Halfway there', 'desc': 'Get over 1.34e154 zeros. Reward: All production is doubled.'},
    {'name': 'Some one needs to nerf that', 'desc': 'Produce 1e6 zeros per second with a single one\nand nothing else.'},
    {'name': '2747', 'desc': 'Get 274 sevens. Reward: each seven bought gives a 343/342 boost\nto seven production.'},
    {'name': 'Not quite eight', 'desc': 'Go infinite. Reward: Start with 7 zeros.'}
  ]
];

let populateAchievements = function (player) {
  let table = document.getElementById('achTable');
  for (let i = 0; i < achievements.length; i++) {
    let row = document.createElement('tr');
    row.id = 'achTr' + i;
    for (let j = 0; j < achievements[i].length; j++) {
      let td = document.createElement('td');
      td.id = 'achTd' + i + '-' + j;
      let item = document.createElement('div');
      item.id = 'ach' + i + '-' + j;
      item.innerHTML = achievements[i][j].name;
      item.setAttribute('desc', achievements[i][j].desc);
      item.className = player.achievements.includes(i + '-' + j) ?
      'achievementunlocked' : 'achievementlocked';
      td.appendChild(item);
      row.appendChild(td);
    }
    table.appendChild(row);
  }
}

let reversedAchievements = {};

for (let i = 0; i < achievements.length; i++) {
  for (let j = 0; j < achievements[i].length; j++) {
    reversedAchievements[achievements[i][j].name] = i + '-' + j;
  }
}

let hasAchievement = function (player, x) {
  if (!(x in reversedAchievements)) {
    let str = typeof x === 'object' ? JSON.stringify(x) : x;
    notify('Game bug: no achievement ' + str, 'red', 7);
  }
  return player.achievements.includes(reversedAchievements[x]);
}

let giveAchievement = function (player, x) {
  if (!hasAchievement(player, x)) {
    player.achievements.push(reversedAchievements[x]);
    document.getElementById('ach' + reversedAchievements[x]).className =
    'achievementunlocked';
    notify('Got achievement "' + x + '"!', 'green', 3)
  }
}

export {achievements, populateAchievements, hasAchievement, giveAchievement};
