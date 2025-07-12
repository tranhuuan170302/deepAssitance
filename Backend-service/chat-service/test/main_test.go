package test

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func AddOne(num int) int {
	return num + 1
}
func TestAddOneTestAddOne(t *testing.T) {
	assert.Equal(t, AddOne(1), 2, "Addone(1) should be 2")
}
