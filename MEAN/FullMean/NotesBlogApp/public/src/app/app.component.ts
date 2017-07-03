import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { NotesService} from "./notes.service"
import { FormsModule} from "@angular/forms"

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
notes:any = []

constructor(private _NotesService:NotesService , private _router:Router) {

  this._NotesService.get()
  .then(notes => {this.notes =notes
    console.log(notes[notes.length-1])
  })
  .catch(err => console.log(err))



}

note = {}


create(){
  console.log("create at TS")
  this._NotesService.create( this.note )
  .then( notes => {this.notes= notes
  this.note = {}
  })
  .catch(err => console.log(err))



}
}
