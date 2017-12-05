package main

type pos struct {
	x int
	y int
}

type moves struct {
	right struct {
		x string
		y string
	}
	up struct {
		x string
		y string
	}
	left struct {
		x string
		y string
	}
	down struct {
		x string
		y string
	}
}

var Moves = &moves{
	right: struct{
		x: "+", y: ""},
	up:   struct{x: "", y: "+"},
	left: {"-", ""},
	down: {"", "-"}}

func main() {
	// p = position
	// n = number
	// i = index
	// f = factor
	// t = tick
	p := pos{0, 0}
	n := 1
	i := 0
	f := 1
	t := 1
}
