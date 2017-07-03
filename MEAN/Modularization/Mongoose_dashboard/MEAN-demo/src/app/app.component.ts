import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  animals= [{id:"",name:"", height:0, attack:"", special_ability:""}]
  title = 'app';
}
