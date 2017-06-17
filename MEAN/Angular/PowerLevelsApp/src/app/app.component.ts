import { Component, Input, Output } from '@angular/core';
import { Power } from './power';
import {NgForm} from '@angular/forms'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'SupSayan Power Calculator';
  powers=[]
  power= new Power()
  constructor(){
    this.power= new Power();
  }

  logNum(){
    this.powers.push(this.power)
  }

}
