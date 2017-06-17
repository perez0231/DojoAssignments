import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-top',
  templateUrl: './top.component.html',
  styleUrls: ['./top.component.css']
})

export class TopComponent implements OnInit {

  constructor() { }
  @Input() PowerExp;
  powers = [];



  ngOnInit() {
  }

}
