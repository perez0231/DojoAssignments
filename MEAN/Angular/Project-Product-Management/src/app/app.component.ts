import { Component } from '@angular/core';
import { ProductsService } from './products.service'
import { Product } from './product';
import { NgForm } from '@angular/forms';
import { Injectable } from '@angular/core';
import { BehaviorSubject} from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  title = 'Project Product Managment';
  products= [ ]


 constructor(private _productsService: ProductsService){
    this._productsService.updateProducts(this.products);
    this._productsService.productsObservable.subscribe((products) => {
      this.products = products
    });
 }


}
