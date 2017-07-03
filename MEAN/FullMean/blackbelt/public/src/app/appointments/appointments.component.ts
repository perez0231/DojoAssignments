import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { Cookie } from 'ng2-cookies';
import { AppointmentService} from '../appointment.service'

@Component({
  selector: 'app-appointments',
  templateUrl: './appointments.component.html',
  styleUrls: ['./appointments.component.css']
})
export class AppointmentsComponent implements OnInit {
  name =Cookie.get("name")
  id =Cookie.get("id")
  appointments: any = []

  constructor(private _http:Http, private _appointmentService: AppointmentService, private _router: Router) { }

  ngOnInit() {
    this._appointmentService.appointments()
    .then(data => {
    console.log(data)
    console.log(this.appointments)
    this.appointments = data

    })
    .catch(err => console.log(err))
  }



  logOut(){
    Cookie.deleteAll()
    this._router.navigateByUrl('')
  }


}
