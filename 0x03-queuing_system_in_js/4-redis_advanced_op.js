import { createClient } from 'redis';
const redis = require("redis");

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));

const keyValue = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
}

for (let key in keyValue) {
  client.HMSET("HolbertonSchools", key, keyValue[key], redis.print);
}

client.hgetall("Holbertonschools", (err, res) => console.log(res));

