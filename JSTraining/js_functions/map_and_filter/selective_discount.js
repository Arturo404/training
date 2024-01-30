array_products = [
    {
        name: "pan",
        price:20.1
    },
    {
        name: "bench",
        price:50
    },
    {
        name: "chair",
        price:52
    },
    {
        name: "ps4",
        price:345
    },
    {
        name: "book",
        price:21
    },
    {
        name: "couch",
        price:2456.45
    }
];

function discount(product) {
    product.price*=0.85;
    return product;
}

function SelectAndMapWithDiscount(array_products) {
    const array_mapped = array_products.filter((product)=>{return product.price>50;}).map(discount);
    return array_mapped;
}

console.log(SelectAndMapWithDiscount(array_products));