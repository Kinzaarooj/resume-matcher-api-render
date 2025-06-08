const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
  console.log('Webhook received:', req.body);
  res.send({ message: 'Webhook received successfully' });
});

app.listen(port, () => {
  console.log(Server running on port ${port});
});
