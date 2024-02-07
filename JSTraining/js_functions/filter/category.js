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
    const array_filtered = array_objects.filter((object) => {
        return object.category == category;
    });
    return array_filtered;
}

console.log(filterCategory(array_objects, "kitchen"));
