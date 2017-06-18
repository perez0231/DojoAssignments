import { Component } from '@angular/core';
import { HttpService } from './http.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Weather';
  city= ""
  weather= [];
  constructor(private _httpService: HttpService){}

  OnSubmit(city){
      this.city = city.city
      this._httpService.getWeather(this.city)
      .then(weather =>{this.weather = weather
      console.log(this.weather)
      console.log("here")
      })
      .catch(err => {console.log(err) })


  }

}
