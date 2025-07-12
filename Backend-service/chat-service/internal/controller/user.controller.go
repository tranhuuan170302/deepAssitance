package controller

import (
	"github.com/TranHuuAn/chat-service/internal/service"
	"github.com/TranHuuAn/chat-service/pkg/response"
	"github.com/gin-gonic/gin"
)

// create structure user controller
type UserController struct {
	userService *service.UserService
}

// create function new user controller
func NewUserController() *UserController {
	return &UserController{
		userService: service.NewUserService(),
	}
}

// create function get user by id
func (uc *UserController) GetUserByID(c *gin.Context) {
	response.SuccessResponse(c, 200, []string{"tipsjs"})
}
