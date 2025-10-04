// main.go
package main

import (
    "fmt"
    "net"
    "time"
)

func scanPort(host string, port int) bool {
    address := fmt.Sprintf("%s:%d", host, port)
    conn, err := net.DialTimeout("tcp", address, 1*time.Second)
    if err != nil {
        return false
    }
    conn.Close()
    return true
}

func main() {
    hosts := []string{"127.0.0.1", "8.8.8.8"}
    ports := []int{22, 80, 443}

    for _, host := range hosts {
        fmt.Printf("Scanning host: %s\n", host)
        for _, port := range ports {
            if scanPort(host, port) {
                fmt.Printf("Port %d: open ✅\n", port)
            } else {
                fmt.Printf("Port %d: closed ❌\n", port)
            }
        }
        fmt.Println("----")
    }
}
