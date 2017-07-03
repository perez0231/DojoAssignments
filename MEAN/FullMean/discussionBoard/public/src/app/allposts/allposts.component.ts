import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies'
import { MessageService} from '../message.service'
import { Router } from "@angular/router"
import { Http } from "@angular/http"

@Component({
  selector: 'app-allposts',
  templateUrl: './allposts.component.html',
  styleUrls: ['./allposts.component.css']
})
export class AllpostsComponent implements OnInit {
name =Cookie.get("name")
questions: any =[]
  constructor(private _http:Http, private _messageService: MessageService, private _router: Router) { }

  ngOnInit() {

      this._messageService.allQuestions()
      .then(data =>{
        console.log("get all")
        console.log(data)
        this.questions = data
        console.log(this.questions)
        console.log("comp all quest")
      })
      .catch(err => console.log(err))

  }

  logOut(){
  Cookie.deleteAll()
  this._router.navigateByUrl('')
}



}
