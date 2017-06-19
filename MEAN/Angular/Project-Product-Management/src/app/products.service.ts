import { Injectable } from '@angular/core';
import {Product} from './product';
import { BehaviorSubject } from 'rxjs';

@Injectable()
export class ProductsService {


  productsObservable = new BehaviorSubject(null)

  constructor() { }
  products=[];
  updateProducts(products: Array<Product>){
    this.productsObservable.next(products);
  }

  // create(newProduct){
  //   this.products.push(newProduct)
  // }

  getOneProduct(idx){
  return this.products[idx];
}

}
