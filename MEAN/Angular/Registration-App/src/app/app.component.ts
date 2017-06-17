import { Component } from '@angular/core';
import { User } from './Users';
import {NgForm} from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
  export class AppComponent {
  usersinfo = Array<User>();
  user= new User();
  onSubmit(){
    this.usersinfo.push(this.user);
    this.user = new User();
    console.log(this.usersinfo)

  }


}
