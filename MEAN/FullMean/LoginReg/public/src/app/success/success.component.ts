import { Component, OnInit } from '@angular/core';
import {UsersService} from '../users.service'
import { Router } from "@angular/router";
import { Cookie } from "ng2-cookies"

@Component({
  selector: 'app-success',
  templateUrl: './success.component.html',
  styleUrls: ['./success.component.css']
})
export class SuccessComponent implements OnInit {
id = Cookie.get("logged_id")
fname= Cookie.get("fname")
lname= Cookie.get("lname")
users= []

  constructor(private _usersService: UsersService, private _router: Router) { }

  ngOnInit() {
    this._usersService.success()
    .then(data=>{
      this.users= data
    })
    .catch(err => console.log(err))
  }

  logout(){
    Cookie.deleteAll()
    this._router.navigateByUrl('login')
  }

}
