function maximumToys(prices, k) {
  let toyCount = 0;
  let total = 0;
  prices.sort((a, b) => a - b);
  for (let price of prices) {
    total += price;
    if (total > k) break;
    toyCount += 1;
  }
  return toyCount;
}

console.log(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50));
