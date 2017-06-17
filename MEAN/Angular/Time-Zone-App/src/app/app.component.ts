import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'US Time Zone Display';
  time = new Date();
  color= "yellow"
  timearea= []

  showPST(){
    this.timearea = ["PST time:"]
    this.timearea.push(this.time) }
  showMST(){
      this.timearea = ["MST time:"]
      this.timearea.push(this.time) }
  showCST(){
    this.timearea = ["CST time:"]
    this.timearea.push(this.time) }
  showEST(){
    this.timearea = ["PST time:"]
    this.timearea.push(this.time) }
}
