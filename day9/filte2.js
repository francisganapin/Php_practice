function isValidIPv6(ip){
    const ipv6Regex = /^(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$/;

}

let ip = "2001:0db8:85a3:08d3:1319:8a2e:0370:7334";


if (isValidIPv6(ip)){
    console.log(`${ip} is valid IPv6 address`);
}else{
    console.log(`${ip} is not a valid IPv6 address`);
}