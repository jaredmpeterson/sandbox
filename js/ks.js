const spendingLimit = 1000;
var accountBalance = 1000;
const taxRate = 0.075;
const phonePrice = 949.0;
const accessoryPrice = 29.99;
var amount = 0;

function withTax(itemPrice) {
  return itemPrice + itemPrice * taxRate;
}

function formatPrice(amount) {
  return "$" + amount.toFixed(2);
}

while (amount < accountBalance) {
  amount += withTax(phonePrice);

  if (amount < spendingLimit) {
    amount += withTax(accessoryPrice);
  }
}

if (amount > accountBalance) {
  console.log("You cannot afford this phone. :(");
}
