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
    {'name': 'Sevens add and multiply', 'desc': 'Get sevens multiplier to at least 1000. Reward: Sevens are again 7/6x stronger.'},
    {'name': 'You need a boost', 'desc': 'Boost.'}
  ], [
    {'name': 'All at once', 'desc': 'Buy at least 343 ones at once.'},
    {'name': "That's a lot of boosts", 'desc': 'Boost 10 times.'},
    {'name': "What's the point of doing that?", 'desc': "Buy a single one when you've bought at least 2401. Reward: each one bought gives a 2401/2400 boost to one production."},
    {'name': 'Halfway there', 'desc': 'Get over 1.34e154 zeros. Reward: All production is doubled.'},
    {'name': 'Some one needs to nerf that', 'desc': 'Produce 1e6 zeros per second with a single one and nothing else.'},
    {'name': '2747', 'desc': 'Get 274 sevens. Reward: each seven bought gives a 343/342 boost to seven production.'},
    {'name': 'Not quite eight', 'desc': 'Go infinite. Reward: Start with 7 zeros.'}
  ], [
    {'name': 'Daredevil', 'desc': 'Complete a challenge.'},
    {'name': "That's fast", 'desc': 'Go infinite in 1 hour. Reward: Start with 7^3 zeros.'},
    {'name': "One's even enough", 'desc': 'Go infinite with only one seven. Reward: All numbers but sevens are 7/6x stronger.'},
    {'name': 'Why were boosts afraid of seven?', 'desc': 'Boost sevens.'},
    {'name': 'Some one needs to nerf that II', 'desc': 'Produce 1e6 zeros per second with a single one and nothing else without any shifts or boosts.'},
    {'name': 'Anti-invasion from the eighth dimension!', 'desc': 'Get the production multipliers in reversed order (that is, get one production multiplier to be less than two production multiplier, two production multiplier to be less than three production multiplier, etc.). Reward: number n gets nx production multiplier (that is, ones get 1x, twos get 2x, etc.).'},
    {'name': "That's a lot of infinities", 'desc': 'Go infinite 10 times.'}
  ], [
    {'name': 'Anti-challenged', 'desc': 'Complete all the challenges.'},
    {'name': "That's faster", 'desc': 'Go infinite in 1 minute. Reward: Start with 7^9 zeros.'},
    {'name': 'How did you do that?', 'desc': 'Go infinite having shifted no more than 5 times and not boosted at all.'},
    {'name': "We ain't ever getting over", 'desc': 'Infinity without your zeros ever getting over your zeros per second. Reward: Ones get 2x multiplier.'},
    {'name': 'Many stoppages', 'desc': 'Complete Challenge 2 in 2 minutes. Reward: Boost to production over first two minutes of infinity.'},
    {'name': "Exponential doesn't mean fast", 'desc': 'Complete Challenge 3 in 3 minutes. Reward: exponential boost to all production over first 21 minutes, vanishing over next 21.'},
    {'name': 'Everything is done for you', 'desc': 'Go infinite without at all manually clicking, buying, or resetting.'}
  ], [
    {'name': 'Limit break', 'desc': 'Break infinity.'},
    {'name': 'Much upgrade. Such power. So wow.', 'desc': 'Max all the top 4 rows of infinity upgrades.'},
    {'name': 'No one needs that many boosts', 'desc': 'Get 100 total boosts. Reward: Boost power is boost power^(7/6).'},
    {'name': 'This is hell', 'desc': 'Get sum of challenge times under 6.66 minutes. Reward: Boost to production based of sum of challenge times.'},
    {'name': "You're a star", 'desc': 'Get a star.'},
    {'name': 'Luminosity', 'desc': 'Get 1000 star power. Reward: Star power generation doubled.'},
    {'name': 'That many at once?', 'desc': 'Get over 1000 infinity points by going infinite once. Reward: Infinity points from going infinity are raised to the 7/6 power.'}
  ], [
    {'name': "It's night now", 'desc': 'Get 3 stars. Reward: Star power generation tripled.'},
    {'name': 'Maximum speed', 'desc': 'Max all the autobuyers.'},
    {'name': 'Moar anafabula', 'desc': 'Get the multiplier from achievement 2747 to be at least 2747. Reward: The multiplier from achievement 2747 is squared.'},
    {'name': 'My eyes hurt', 'desc': 'Get 1e6 star power.'},
    {'name': "2 million infinities? Nah, that's too hard.", 'desc': 'Get 2 million infinity points. Reward: Infinities at least 5 seconds give double the infinity points.'},
    {'name': 'You broke the upgrades', 'desc': 'Max all the break infinity upgrades.'},
    {'name': "But I didn't want another prestige layer...", 'desc': 'Go extragalactic.'}
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
