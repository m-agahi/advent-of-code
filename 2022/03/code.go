package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		fmt.Println("fucking error man")
		panic(e)
	}
}

func main() {

	readFile, err := os.Open("./puzzle.txt")
	check(err)

	var word, rs1l, rs1r string = "", "", ""
	var sum1, sum2, index, badge int = 0, 0, 0, 0
	var forbreak, forbreak1 bool = false, false
	var sax = [3]string{}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			if index == 0 {
				sax[0] = word
			} else if index == 1 {
				sax[1] = word
			} else {
				sax[2] = word
				index = -1
			}
			rs1l = string([]rune(word)[0 : len(word)/2])
			rs1r = string([]rune(word)[len(word)/2 : len(word)])
			forbreak = false
			for i := 0; i < len(rs1l); i++ {
				left := int([]rune(rs1l)[i]) - 64
				for j := 0; j < len(rs1r); j++ {
					right := int([]rune(rs1r)[j]) - 64
					if left == right {
						// fmt.Printf("%s ", string([]rune(rs1l)[i]))
						if left > 26 {
							left -= 32
						} else {
							left += 26
						}
						if right > 26 {
							right -= 32
						} else {
							right += 26
						}
						sum1 += left
						// fmt.Printf("%d\n ", left)
						forbreak = true
						break
					}
				}
				if forbreak {
					break
				}
			}
			if index == -1 {
				for r := 0; r < len(sax[0]); r++ {
					for s := 0; s < len(sax[1]); s++ {
						if sax[0][r] == sax[1][s] {
							for t := 0; t < len(sax[2]); t++ {
								if sax[0][r] == sax[2][t] {
									// fmt.Printf("badge is %s ", string([]rune(sax[0])[r]))
									badge = int([]rune(sax[0])[r]) - 64
									if badge > 26 {
										badge -= 32
									} else {
										badge += 26
									}
									sum2 += badge
									forbreak1 = true
									break
								}
							}
						}
						if forbreak1 {
							break
						}
					}
					if forbreak1 {
						break
					}

				}
				// fmt.Println("")
			}
			index++
			forbreak1 = false
		} else {
			fmt.Println("nothing")
		}
	}
	// for i := 0; i < len(sax)/3; i++ {
	// 	fmt.Printf("%s\n%s\n%s\n\n", sax[i], sax[i+1], sax[i+2])
	// }
	fmt.Printf("part one answer is = %d\npart two answer is = %d\n", sum1, sum2)

	readFile.Close()
}
