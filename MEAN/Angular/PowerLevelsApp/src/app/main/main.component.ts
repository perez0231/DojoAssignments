import { Component, Input, OnInit } from '@angular/core';
import { Power } from '../power';
import {NgForm} from '@angular/forms'

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor() { }
  @Input() PowerExp;



  ngOnInit() {
  }
  ngOnDestroy() {
  }

}
