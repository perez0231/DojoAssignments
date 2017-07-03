import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { Cookie } from 'ng2-cookies';
import { AppointmentService} from '../appointment.service'

@Component({
  selector: 'app-make-app',
  templateUrl: './make-app.component.html',
  styleUrls: ['./make-app.component.css']
})
export class MakeAppComponent implements OnInit {
  name =Cookie.get("name")
appointment: any ={date: "" , time: "", complaint: "", user: this.name   }
  constructor(private _http:Http, private _appointmentService: AppointmentService, private _router: Router) { }

  ngOnInit() {
  }


  makeAppointment(){
    console.log("making app")
    this._appointmentService.create(this.appointment)
    .then(data => {
      if (data.err){
        alert(data.messages)
      }
      else{
      console.log(data)
      this._router.navigateByUrl("appointments")}
    })
    .catch(err => console.log(err))

  }




}
