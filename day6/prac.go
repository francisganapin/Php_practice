package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	x := `{"name":"lakes","age":30,"city":"Manila"}`

	var y map[string]interface{}

	err := json.Unmarshal([]byte(x), &y)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(y["age"])
}
