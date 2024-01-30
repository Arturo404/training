array_prices = [20.1,345,21.2,2456.45,12.0,456,23455];

function discount(price) {
    return 0.9*price;
}

function mapWithDiscount(array_prices) {
    const array_mapped = array_prices.map(discount);
    return array_mapped;
}

console.log(mapWithDiscount(array_prices));