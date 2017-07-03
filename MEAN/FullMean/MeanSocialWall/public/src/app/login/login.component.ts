import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { MessageService} from '../message.service'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user: any ={}
  constructor(private _http:Http, private _messageService: MessageService) { }

  ngOnInit() {
  }

  login(){
    this._messageService.login(this.user)
  }

}
