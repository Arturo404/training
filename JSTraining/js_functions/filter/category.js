array_objects = [
    {
        name: "pan",
        category: "kitchen"
    },
    {
        name: "desk",
        category: "office"
    },
    {
        name: "chair",
        category: "office"
    },
    {
        name: "screen",
        category: "office"
    },
    {
        name: "knife",
        category: "kitchen"
    }
];


const filterCategory = (array_objects, category) => {
    return array_objects.filter(object => object.category == category);
}

