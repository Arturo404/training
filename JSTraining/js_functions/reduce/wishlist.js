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


const addItem = (total_price, item) => {
    return total_price+item.price;
}

const computeBudget = (wishlist) => {
    return wishlist.reduce(addItem, 0);
}