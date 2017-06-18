import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';

@Component({
  selector: 'app-san-jose',
  templateUrl: './san-jose.component.html',
  styleUrls: ['./san-jose.component.css']
})
export class SanJoseComponent implements OnInit {

  title = 'Dojo Weather';
  city= "Palo Alto";
  weather= [];
  hi_temp= 0;
  avg_temp=0;
  min_temp= 0;
  humidity= 0;
  current_forcast=""

  constructor(private _httpService: HttpService){}

  ngOnInit() {


        this._httpService.getWeather(this.city)
        .then(weather =>{this.weather = weather
        console.log(this.weather)

        this.hi_temp= weather.main.temp_max
        console.log(weather.main.temp_max)

        this.min_temp= weather.main.temp_min
        console.log(weather.main.temp_min)

        this.avg_temp= weather.main.temp
        console.log(weather.main.temp)

        this.humidity= weather.main.humidity
        console.log(weather.main.humidity)

        this.current_forcast= weather.weather[0].description
        console.log(weather.weather[0].description)

        console.log("here")
        })
        .catch(err => {console.log(err) })

  }


}
