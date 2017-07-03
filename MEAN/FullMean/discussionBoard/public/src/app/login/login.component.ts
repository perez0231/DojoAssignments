import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { MessageService} from '../message.service'
import { Cookie } from 'ng2-cookies';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  user: any ={}
  constructor(private _http:Http, private _messageService: MessageService, private _router: Router) { }

  ngOnInit() {
  }

  login(){
    this._messageService.login(this.user)
    .then(data =>{
    console.log("component login")
    console.log(data)
    console.log("setting cookies")
    Cookie.set("name", data.name)
    console.log(Cookie.set("name", data.name))
    this._router.navigateByUrl("allquestions")

  })

  }


}
