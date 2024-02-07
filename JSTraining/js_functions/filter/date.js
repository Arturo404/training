array_dates = ["2000-10-28", "2023-11-18", "2034-10-08", "1998-02-16", "3490-07-06", "1967-07-06", "1970-11-06"];

const isInPast = (date_string) => {
    const date = new Date(date_string + "T00:00:00");
    const current_date = new Date()
    return date < current_date;
}

const filterDateInPast = (array_dates) => {
    const array_filtered = array_dates.filter(isInPast);
    return array_filtered;
}

console.log(filterDateInPast(array_dates));