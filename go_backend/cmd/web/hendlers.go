package main

import "net/http"

func (a *Applicagtion) home(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello World!"))
}