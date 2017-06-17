import { Component, Input, EventEmitter, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  //@Output() updatePower= new EventEmitter

  constructor() { }
  @Input() power;
  powers = [];
  onSubmit() {
    event.preventDefault();
    this.powers.push(this.power);
  }

  ngOnInit() {
  }

}
