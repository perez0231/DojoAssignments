import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies';
import { Router } from '@angular/router'
import { UsersService} from "../users.service"

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user: any = {}
  constructor(private _usersService: UsersService, private _router :Router) {
    console.log("loginCOMP")
    if(Cookie.check("logged_id")){
      console.log(Cookie.get("logged_id"))
      this._router.navigateByUrl('success')
    }

  }

  ngOnInit() {
  }
login(){
  console.log("login COMP before service call")
  this._usersService.login(this.user)
  .then((data)=>{
    if(data.login){
      alert("success!")
      console.log(data.user._id)
      Cookie.set("logged_id", data.user._id)
      Cookie.set("fname", data.user.first_name)
      Cookie.set("lname", data.user.last_name)


      this._router.navigateByUrl("success")
    }
    else{
      alert(data.error)
    }
  })
}
}
