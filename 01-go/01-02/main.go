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
		h := ((len(l) / 2) + c)
		if c >= (len(l) / 2) {
			break
		} else if i == l[h] {
			s += i * 2
		}
	}
	fmt.Println(s)
}
