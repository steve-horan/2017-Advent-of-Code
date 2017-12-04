package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := os.Args[1]
	l := func() []int { //Anon Func like the Python Solution
		s := []int{}
		for _, i := range input {
			r, _ := strconv.Atoi(string(i)) // Pretty sure this is bad.. rune -> string -> int conversion
			s = append(s, r)
		}
		return s
	}()
	s := 0
	for c, i := range l {
		if (c == len(l)-1) && (i == l[0]) {
			s += i
		} else if i == l[c+1] {
			s += i
		}
	}
	fmt.Println(s)
}
