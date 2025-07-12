package router

import (
	"net/http"

	"github.com/TranHuuAn/chat-service/internal/controller"
	"github.com/TranHuuAn/chat-service/internal/middleware"
	"github.com/gin-gonic/gin"
)

// create router for chat service
func healthy(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "the system is working....!",
	})
}

func NewRouter() *gin.Engine {

	r := gin.Default()
	r.Use(middleware.AuthMiddleware())
	v1 := r.Group("/v1")
	{
		v1.GET("/health", healthy)
		v1.GET("/user/:uid", controller.NewUserController().GetUserByID)
	}
	return r
}
