package main

import "fmt"

func main() {
	a := 33
	b := 33

	if b > a {
		fmt.Println("b is greater than a")
	} else if a == b {
		fmt.Println("a and b are equal")
	} else {
		fmt.Println("a is greater than b")
	}
}
