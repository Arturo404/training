wishlist = [
    {
        title: "Tesla Model 5",
        price: 90000
    },
    {
        title: "4 carat diamond ring",
        price: 45000
    },
    {
        title: "Fancy hacky Sack",
        price: 5
    },
    {
        title: "Gold fidgit spinner",
        price: 2000
    }
    
];


function addItem(total_price, item) {
    return total_price+item.price;
}

function computeBudget(wishlist) {
    const budget = wishlist.reduce(addItem, 0);
    return budget;
}

console.log(computeBudget(wishlist));