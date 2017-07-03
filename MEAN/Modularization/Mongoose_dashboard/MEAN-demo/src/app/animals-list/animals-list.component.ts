import { Component, OnInit } from '@angular/core';
import { AnimalsService } from '../animals.service';

@Component({
  selector: 'app-animals-list',
  templateUrl: './animals-list.component.html',
  styleUrls: ['./animals-list.component.css']
})
export class AnimalsListComponent implements OnInit {
  animals:any = []

  constructor(private _animalService: AnimalsService) {
    this._animalService.get()
    .then(res => { this.animals = res})
    .catch(err => console.log(err))
  }

  ngOnInit() {
  }

}
