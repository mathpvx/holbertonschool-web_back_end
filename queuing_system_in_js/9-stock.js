import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// Redis client setup
const client = createClient();
client.on('error', (err) => console.error('Redis client error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Product list
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Helpers
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reserved = await getAsync(`item.${itemId}`);
  return reserved !== null ? parseInt(reserved, 10) : null;
}

// Express server setup
const app = express();
const port = 1245;

// Route: GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route: GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = reservedStock !== null
    ? item.initialAvailableQuantity - reservedStock
    : item.initialAvailableQuantity;

  res.json({ ...item, currentQuantity });
});

// Route: GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId) || 0;
  const available = item.initialAvailableQuantity - reservedStock;

  if (available <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
