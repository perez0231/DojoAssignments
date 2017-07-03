import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies'
import { MessageService} from '../message.service'
import { Router } from "@angular/router"
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-answer',
  templateUrl: './answer.component.html',
  styleUrls: ['./answer.component.css']
})
export class AnswerComponent implements OnInit {
name=Cookie.get("name")
question = {}
answer ={
  answer: "",
  details: "",
  user: this.name

}
constructor(private _activatedRoute: ActivatedRoute, private _router: Router, private _messageService: MessageService) { }

  ngOnInit() {
    this._messageService.show(this._activatedRoute.snapshot.params['id'])
    .then (data =>
    this.question = data)
    .catch(err => console.log(err))
  }

  create(){
    console.log("create controller answer")
    this._messageService.createAnswer(this._activatedRoute.snapshot.params['id'], this.answer)
    .then((data)=>{
      this._router.navigateByUrl('allquestions')
    })
    .catch(err => console.log(err))
  }

}
