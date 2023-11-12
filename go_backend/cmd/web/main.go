package main

import (
	"log"
	"net/http"
	"time"
)

type Applicagtion struct {

}

func main() {

	srv := &http.Server{
		Addr:         ":8080",
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	err := srv.ListenAndServe()
	if err != nil {
		log.Println(err)
	}
}
