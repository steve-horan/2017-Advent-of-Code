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
		line := strings.Split(b.Text(), "\t") // Here we split each line by tabs and create a new slice of strings
		a := func() []int {
			s := []int{}
			for _, i := range line {
				newint, _ := strconv.Atoi(i) // We then convert our []string to []int
				s = append(s, newint)
			}
			return s
		}()
		l := func() int { //Function to get the lowest number in slice
			var m int
			for _, i := range a {
				if m == 0 {
					m = i
				} else if i < m {
					m = i
				}
			}
			return m
		}()
		h := func() int { //Function to get the highest number in a slice
			var m int
			for _, i := range a {
				if m == 0 {
					m = i
				} else if i > m {
					m = i
				}
			}
			return m
		}()
		s += h - l
	}
	fmt.Println(s)
}
