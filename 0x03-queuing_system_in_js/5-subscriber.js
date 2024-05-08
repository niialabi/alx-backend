import { createClient } from 'redis';
const redis = require("redis");

const subscriberClient = createClient().on("error", (err) =>
  console.log("Redis client not connected to the server:", err.message)
);
console.log("Redis client connected to the server");

subscriberClient.subscribe("holberton school channel");
subscriberClient.on("message", (ch, message) => {
  console.log(message)
  if (message == "KILL_SERVER") {
    subscriberClient.unsubscribe(ch);
    subscriberClient.quit();
  }
});

