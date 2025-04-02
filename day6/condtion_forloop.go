package main

import "fmt"

func main() {
	i := 1

	for i < 6 {
		fmt.Println(i)
		i++
	}
	fmt.Println("I is no longer less than 6")
}
