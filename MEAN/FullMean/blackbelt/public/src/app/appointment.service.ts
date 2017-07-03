import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs'

@Injectable()
export class AppointmentService {

  constructor(private _http: Http) { }

  login(user){
    return this._http.post('/login', user)
    .map((data)=>{
      return data.json()
    })
    .toPromise()
  }


create(appointment){
  console.log("rvices")
  return this._http.post('/appointments', appointment)
  .map((data) =>{
    console.log(data)
    return data.json()
  })
  .toPromise()

}


appointments(){
  return this._http.get('/appointments')
  .map((data)=>{
    console.log(data)
    return data.json()
  })
  .toPromise()
}

delete(id){
  return this._http.get(`/delete/${id}`)
  .map((data)=>{
    console.log(data)
    return data.json()
  })
  .toPromise()
}


}
