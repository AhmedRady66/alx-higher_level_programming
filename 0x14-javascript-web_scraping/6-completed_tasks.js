#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, _response, body) => {
  if (err) {
    console.error(err);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUsers = {};

  for (let i = 0; i < tasks.length; i++) {
    const userId = tasks[i].userId;
    const completed = tasks[i].completed;

    if (completed) {
      if (!completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }
      completedTasksByUsers[userId]++;
    }
  }

  console.log(completedTasksByUsers);
});
