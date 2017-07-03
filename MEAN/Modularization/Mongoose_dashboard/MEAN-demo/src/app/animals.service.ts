import { Injectable } from '@angular/core';
import {Http} from '@angular/http'
import 'rxjs'

@Injectable()
export class AnimalsService {

  constructor(private _http:Http) {
  }


  get(){
    return this._http.get('/animals').map(res=>res.json()).toPromise();
    return this._http.post('/animals').map(res=>res.json()).toPromise();
  }
}
