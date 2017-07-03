import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { Cookie } from 'ng2-cookies';
import { AppointmentService} from '../appointment.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user: any ={}
  constructor(private _http:Http, private _appointmentService: AppointmentService, private _router: Router) { }

  ngOnInit() {
  }
  login(){
  this._appointmentService.login(this.user)
  .then(data =>{
    console.log(data)
    Cookie.set("name", data.name)
    Cookie.set("id", data._id)
    console.log("cl id")
    console.log(data._id)

    this._router.navigateByUrl("appointments")
  })
}
}
