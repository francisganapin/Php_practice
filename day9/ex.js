function inverse(x){
    if(!x) {
        throw new Error("Division by Zero");
    }
    return 1 / x;
}


try {
    console.log(inverse(5));
    console.log(inverse(0));
} catch(e){
    console.log("Caught exception: " + e.message);
}