package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, _ := os.Open("work.txt")
	b := bufio.NewScanner(f)
	var s int
	for b.Scan() {
		line := strings.Split(b.Text(), "\t")
		a := func() []int {
			s := []int{}
			for _, i := range line {
				newint, _ := strconv.Atoi(i)
				s = append(s, newint)
			}
			return s
		}()
		for _, i := range a {
			for _, x := range a {
				if i%x == 0 {
					if i > x {
						s += i / x
					}
				}
			}
		}
	}
	fmt.Println(s)
}
