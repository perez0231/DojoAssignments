import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'DojoMail';

  emails = [
    {email: "perez0324@gmail.com", importance: true, subject: "Beer Garden", content:"lets go to the beer garden"},
    {email: "jillybean@gmail.com", importance: false, subject: "Beer Garden RE:", content:"Im always down to drink"},
    {email: "marco@gmail.com", importance: true, subject: "Beer Garden RE: RE:", content:"Jill is  a dick"},
    {email: "Tim@gmail.com", importance: true, subject: "Beer Garden RE: RE:", content:"Jill is  a dick"},

  ]
}
