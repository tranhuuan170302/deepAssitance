package main

// import (
// 	"fmt"

// 	"github.com/spf13/viper"
// )

// type Config struct {
// 	Server struct {
// 		Port int `mapstructure:"port"`
// 	} `mapstructure:"server"`

// 	Database []struct {
// 		User     string `mapstructure:"user"`
// 		Password string `mapstructure:"password"`
// 		Host     string `mapstructure:"host"`
// 	} `mapstructure:"databases"`
// }

// func main() {

// 	fmt.Println("Config Port::", config.Server.Port)

// 	for _, db := range config.Database {
// 		fmt.Printf("database User: %s, password: %s, host: %s\n", db.User, db.Password, db.Host)
// 	}
// }
