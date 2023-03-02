package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

type file struct {
	name      string
	file_type string
	size      int
	children  []*file
	parrent   *file
	id        string
}

var terminal = make([]string, 0)
var fs = make([]*file, 0)
var parrents = make([]*file, 0)
var word string
var parrentsmap = make(map[string]bool)

func check(e error) {
	if e != nil {
		fmt.Println("fucking error man")
		panic(e)
	}
}

func debug(message string) {
	fmt.Println(message)
}

func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	check(err)

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		word = fileScanner.Text()
		terminal = append(terminal, word)
	}

	do(terminal)
	readFile.Close()
}

// parses the input file line by line and detemines what to do based on the input
func do(terminal []string) {
	for l := 0; l < len(terminal); l++ {
		var ftemp file
		line := terminal[l]
		// using uuid to diffrenciate between files and directories with the same name when we search th array
		newUUID, err := exec.Command("uuidgen").Output()
		check(err)
		// if its a command
		if line[0:2] == "$ " {
			if line[2:4] == "ls" {
				// do nothing
				// debug("ls")
			} else if line[2:6] == "cd /" {
				// only once for root directory
				ftemp.name = "/"
				ftemp.file_type = "d"
				ftemp.size = 0
				ftemp.id = string(newUUID)
				fs = append(fs, &ftemp)
				parrents = append(parrents, &ftemp)
			} else if line[2:6] == "cd ." {
				// pop one entry from parrent stack
				parrents = parrents[:len(parrents)-1]
			} else if line[2:5] == "cd " {
				// create tha directory object and add it to the parrent stack
				ftemp.name = line[5:]
				ftemp.file_type = "d"
				ftemp.size = 0
				ftemp.id = string(newUUID)
				ftemp.parrent = parrents[len(parrents)-1]
				fs = append(fs, &ftemp)
				parrents = append(parrents, &ftemp)

			}
		} else if line[0:3] == "dir" {
			// do nothing. we create directory objexts upon traversing to them
			// debug("this is not the message you are looking for")
		} else {
			// create file object, set its parrent and size and such
			temp := strings.Fields(line)
			ftemp.name = temp[1]
			ftemp.size, _ = strconv.Atoi(temp[0])
			ftemp.file_type = "f"
			ftemp.id = string(newUUID)
			ftemp.parrent = parrents[len(parrents)-1]
			fs = append(fs, &ftemp)
		}
	}

	// create a unique map of the non edge nodes aka parrents
	for i := 1; i < len(fs); i++ {
		parrentsmap[fs[i].parrent.id] = true
	}

	// find children that have the same parrent and add that child to the parrent children field
	for k := range parrentsmap {
		for i := 0; i < len(fs); i++ {
			if fs[i].id == k {
				for child := 1; child < len(fs); child++ {
					if fs[child].parrent.id == k {
						fs[i].children = append(fs[i].children, fs[child])
					}
				}
			}
		}
	}

	// create a queue from directories with Breadth-first traverse
	q := make([]*file, 0)
	for k := 0; k < len(fs); k++ {
		if fs[k].file_type == "d" {
			q = append(q, fs[k])
		} else {
			fs[k].parrent.size += fs[k].size
		}
	}

	// picks directories that were queued up in q and adds their size to their parrents size
	for k := len(q) - 1; k > 0; k-- {
		q[k].parrent.size += q[k].size
	}

	// find directories that have less than 100000 in size and adds the up
	sum1 := 0
	for k := 0; k < len(fs); k++ {
		if fs[k].file_type == "d" && fs[k].size < 100000 {
			sum1 += fs[k].size
		}
	}

	disk_size := 70000000
	update_size := 30000000
	available := disk_size - fs[0].size
	needed_space := update_size - available
	least := fs[0].size
	var dir *file
	for k := 0; k < len(fs); k++ {
		if fs[k].file_type == "d" && fs[k].size >= needed_space && fs[k].size < least {
			least = fs[k].size
			dir = fs[k]
		}
	}

	fmt.Println("part 1 results: ", sum1)
	fmt.Println("part 2 results: ", dir.size)
}
