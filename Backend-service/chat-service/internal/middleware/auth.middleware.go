package middleware

import (
	"github.com/TranHuuAn/chat-service/pkg/response"
	"github.com/gin-gonic/gin"
)

func AuthMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		token := c.GetHeader("Authorization")
		if token == "" {
			response.Errorresponse(c, response.ErrorCodeUnauthorized, "Unauthorized")
			c.Abort()
			return
		}
		c.Next()
	}

}
