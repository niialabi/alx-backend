import { createClient } from 'redis';
const redis = require("redis");
import { promisify } from "util";

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  get(schoolName).then((res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

