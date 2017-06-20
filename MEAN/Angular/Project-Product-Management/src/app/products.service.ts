import { Injectable } from '@angular/core';
import {Product} from './product';
import { BehaviorSubject } from 'rxjs';

@Injectable()
export class ProductsService {

//creating an observable object of BehaviorSubject
  productsObservable = new BehaviorSubject(null)

  constructor() { }
  //creating blank array, Creating update products function with array as a param, telling obserable object to push changes to the products array
  products=[];
  updateProducts(products: Array<Product>){
    this.productsObservable.next(products);
  }

}
