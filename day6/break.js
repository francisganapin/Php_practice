const fruits = ["apple", "banana", "cherry"]; // Array declaration

for (const x of fruits) {
    console.log(x);
    if (x === "banana") {
        break; // Stops the loop when "banana" is encountered
    }
}