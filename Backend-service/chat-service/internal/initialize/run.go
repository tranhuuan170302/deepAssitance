package initialize

import (
	"fmt"

	"github.com/TranHuuAn/chat-service/global"
)

func Run() {
	InitLoadConfig()
	dbConfig := global.Config.Postgress
	fmt.Println("Loading configuration postgress", dbConfig.Host, dbConfig.Port)
	InitLogger()
	InitPostgress()
	InitRedis()

	r := InitRouter()

	r.Run()
}
