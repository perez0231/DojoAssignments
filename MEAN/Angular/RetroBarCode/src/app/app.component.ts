import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Retro Barcode Generator';

  colors = [ 'YellowGreen', "Wheat", "Tomato", "Thistle", "RoyalBlue", "RosyBrown", "SeaShell", "Plum", "PowderBlue", "SaddleBrown"]
  a: number =(Math.floor(Math.random() * 9)) +1;
  b: number =(Math.floor(Math.random() * 9)) +1;
  c: number =(Math.floor(Math.random() * 9)) +1;
  d: number =(Math.floor(Math.random() * 9)) +1;
  e: number =(Math.floor(Math.random() * 9)) +1;
  f: number =(Math.floor(Math.random() * 9)) +1;
  g: number =(Math.floor(Math.random() * 9)) +1;
  h: number =(Math.floor(Math.random() * 9)) +1;
  i: number =(Math.floor(Math.random() * 9)) +1;
}
