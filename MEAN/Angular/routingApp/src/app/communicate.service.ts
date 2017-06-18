import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
@Injectable()
export class CommunicateService {

  constructor() { }
  observedUsers = new BehaviorSubject(null);
  updateUsers(users: Array) {
    this.observedUsers.next(users);
  }
}
