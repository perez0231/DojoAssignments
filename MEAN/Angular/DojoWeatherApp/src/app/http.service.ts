import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/Rx'; //Injectable


  @Injectable()

  export class HttpService {
      constructor(private _http: Http) { }
      getWeather(city){
          return this._http.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=7c0089a51d3a0058b9370a6f54a82ce1').map(data=>data.json()).toPromise();
  }
  }
