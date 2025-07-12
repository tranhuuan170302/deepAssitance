package initialize

import (
	"fmt"

	"github.com/TranHuuAn/chat-service/global"
	"github.com/spf13/viper"
)

func InitLoadConfig() {
	viper := viper.New()
	viper.AddConfigPath("./config/")
	viper.SetConfigName("local")
	viper.SetConfigType("yaml")

	// Read file configuration
	err := viper.ReadInConfig()

	if err != nil {
		panic(fmt.Errorf("Failed to read configuration %w \n", err))
	}

	fmt.Println("Server Port::", viper.GetInt("server.port"))
	fmt.Println("Database User::", viper.GetString("databases.user"))

	//configure structure
	if err := viper.Unmarshal(&global.Config); err != nil {
		fmt.Printf("Unable to decode configuration %v", err)
	}
}
