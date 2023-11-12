package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func (app *Applicagtion) routes() http.Handler {

	router := gin.Default()

	router.GET("/", app.home())


}