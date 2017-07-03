import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import {UsersService} from '../users.service'
import { Cookie } from 'ng2-cookies';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor(private _usersService: UsersService, private _router:Router) { }
  user: any= {}
  users = []
  cpassword=""
  ngOnInit() {
  }

  OnSubmit(){
    if(this.user.password != this.cpassword){
      alert("passwords do not match")
    }
    else{
      this._usersService.create(this.user)
      .then((data)=>{
        if(data.error){
          alert(data.messages)
        }
        else{
          Cookie.set("logged_id", data.user._id)
          Cookie.set("fname", data.user.first_name)
          Cookie.set("lname", data.user.last_name)

          this._router.navigateByUrl('success')
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }




}
