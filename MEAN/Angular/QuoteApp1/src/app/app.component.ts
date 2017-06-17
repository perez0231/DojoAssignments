import { Component, Input, Output } from '@angular/core';
import {Quote} from './quote'
import {NgForm} from '@angular/forms'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  quotes= [];
  quote = new Quote();


  onSubmit(){

    console.log('onSUbmit()')
    console.log(this.quote)
    this.quotes.push(this.quote);
    this.quote = new Quote()
    console.log(this.quotes)
  }


}
