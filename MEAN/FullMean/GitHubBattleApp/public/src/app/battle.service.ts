import { Injectable } from '@angular/core';

import { Http } from '@angular/http'
import 'rxjs'

@Injectable()

export class BattleService {
  users = [];
  constructor(private _http: Http) { }
  gitScore(username){
    console.log("hereat my service")
          return this._http.get('https://api.github.com/users/'+ username).map(data=>data.json()).toPromise();
  }

  create(user){
    console.log("here at service ");
    return this._http.post('/users', user)
    .map((data)=>{ console.log(data)
      this.users.push(data.json())
      console.log("pppopooop")
      console.log(this.users)
      return data.json()
    })
    .toPromise();

  }

  new(){
    this.users= []
  }

  battle(){
    console.log(this.users)
    return this.users
  }

  rankings(){
    return this._http.get('/users').map(data => data.json()).toPromise()}

  }
