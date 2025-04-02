package main

import "fmt"

func main() {
	fruits := []string{"apple", "banana", "cherry"}

	for _, x := range fruits {
		fmt.Println(x)
		if x == "banana" {
			break
		}
	}
}
