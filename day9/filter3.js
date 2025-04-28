function hasQueryString(url){
    try{
        let parsedUrl = new URL(url);
        return parsedUrl.search ? true: false;
    }
    catch (e){
        return false;
    }
}

let url = "https://www.w3schools.com";

if(hasQueryString(url)){
    console.log(`${url} is a valid URL with a query string`);
} else{
    console.log(`${url} is not a valid URL with a query string`);
}