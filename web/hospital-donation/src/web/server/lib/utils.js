const PRODUCTS = [
    {'name': 'Oxygen Tank', 'price': 6000000},
    {'name': 'Hospital Bed', 'price': 10000000},
    {'name': 'Ventilator', 'price': 37000000},
    {'name': 'ECG Machine', 'price': 52000000},
    {'name': 'Transport Ventilator', 'price': 326000000},
    {'name': 'Rontgen Machine', 'price': 1500000000}
]

function accessProducts(id, key) {
    if (id < 0) throw new Error(`Cannot find product with id=${id}.`)
    if (PRODUCTS.length <= id) throw new Error(`Cannot find product with id=${id}.`)
    return PRODUCTS[id][key]
}
exports.getProductList = () => {
    return PRODUCTS
}
exports.getProductName = (id) => {
    return accessProducts(id, 'name')
}
exports.getProductPrice = (id) => {
    return accessProducts(id, 'price')
}