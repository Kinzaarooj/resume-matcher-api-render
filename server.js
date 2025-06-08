const express = require('express');
    const app = express();
    app.use(express.json());

    app.post('/webhook', (req, res) => {
      console.log('Webhook received:', req.body);
      res.status(200).json({ message: 'Webhook received successfully' });
    });

    const port = process.env.PORT || 3000;
    app.listen(port, () => console.log(`Server running on port ${port}`));