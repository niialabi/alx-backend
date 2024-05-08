const kue = require("kue");
const queue = kue.createQueue();

const dtObject = {
  phoneNumber: "0244444444",
  message: "Welcome to Africa",
}


const job = queue.create('push_notification_code', dtObject).save((err) => {
  if (!err) console.log("Notification job created", job.id);
  })
  .on('complete', ()=> console.log("Notification job completed"))
  .on('failed', ()=> console.log("Notification job failed"));
