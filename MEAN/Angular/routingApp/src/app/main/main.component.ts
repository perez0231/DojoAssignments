import { Component } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { CommunicateService } from './communicate.service';
import { Subscription } from "rxjs/Subscription";
import { OnDestroy } from "@angular/core";


@Component({
  selector: 'app-child',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnDestroy {

  users = [];
  subscription: Subscription;
	constructor(private _communicateService: CommunicateService) {
		this.subscription = _communicateService.observedUsers.subscribe(
			(updatedUsers) => {  this.users = updatedUsers; },
			(err) => { },
			() => { }
		)
	}
  updateUsers(){
    this._communicateService.updateUsers(this.users);
  }
}
