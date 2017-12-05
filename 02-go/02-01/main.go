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
		l := func() int {
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
		h := func() int {
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
