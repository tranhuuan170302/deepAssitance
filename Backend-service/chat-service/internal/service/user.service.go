package service

import "github.com/TranHuuAn/chat-service/internal/repo"

// create user service structure
type UserService struct {
	userRepo *repo.UserRepo
}

func NewUserService() *UserService {
	return &UserService{
		userRepo: repo.NewUserRepo(),
	}
}

// get user by id
func (us *UserService) GetUserByID(uid string) (string, error) {
	return us.userRepo.GetUserByID(uid), nil
}
