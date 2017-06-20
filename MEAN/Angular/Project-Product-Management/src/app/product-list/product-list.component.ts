import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../products.service'
import { Product } from '../product';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products =[];

  constructor(private _productsService: ProductsService) { }




  ngOnInit() {
    this._productsService.productsObservable.subscribe((products) => {
      this.products = products;
    });


  }



}
