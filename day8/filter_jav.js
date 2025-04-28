const fruits = ["apple",'banana','cherry','mango','blueberry'];


const filteredFruits = fruits.filter(fruits => /berry$/.test(fruits));

console.log(filteredFruits);