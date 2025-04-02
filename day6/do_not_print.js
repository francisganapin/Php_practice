const fruits = ["apple","banana","cherry"];

for (const x of fruits){
    if (x === "banana"){
        continue
    }
    console.log(x);
}