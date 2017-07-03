import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Http } from '@angular/http'
import { Cookie } from 'ng2-cookies';
import { AppointmentService} from '../appointment.service'
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements OnInit {

  constructor(private _http:Http, private _appointmentService: AppointmentService, private _activatedRoute: ActivatedRoute, private _router: Router) { }

  ngOnInit() {
    this._appointmentService.delete(this._activatedRoute.snapshot.params['id'])
   .then(data =>{
     this._router.navigateByUrl('appointments')
   })
   .catch(err=> console.log(err))


  }

}
