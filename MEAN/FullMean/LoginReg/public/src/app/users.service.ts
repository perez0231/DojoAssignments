import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs'

@Injectable()
export class UsersService {

  constructor(private _http: Http) { }

  create(user){
    console.log("services")
    return this._http.post('/user', user)
    .map((data) => {
      console.log(data)
      console.log("users service return")
      return data.json()
  })
    .toPromise();
  }


  success(){
    return this._http.get('/success')
    .map(data => data.json())
    .toPromise();
  }


login(user){
return this._http.post('/login', user)
.map((data)=>{
  return data.json()
})
.toPromise()
}



}
