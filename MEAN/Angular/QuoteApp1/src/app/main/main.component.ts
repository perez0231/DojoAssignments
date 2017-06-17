import { Component, Input, OnInit } from '@angular/core';
import {Quote} from '../Quote';
import {NgForm} from '@angular/forms'


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor() { }
  @Input() quotes;


  ngOnInit() {
  }
  count: number = 0
  Like(quote){
    quote.likes++
  }
  unlike(quote){
    quote.likes --
  }

  delete(i){
    this.quotes.splice(i, 1);

  }




}
