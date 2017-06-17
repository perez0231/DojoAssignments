import { Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-bottom',
  templateUrl: './bottom.component.html',
  styleUrls: ['./bottom.component.css']
})
export class BottomComponent implements OnInit {

  constructor() { }
  @Input() PowerExp;


  ngOnInit() {
  }

}
