import { Component, OnInit } from '@angular/core';
import { ProductsService } from "../products.service"
import { Product } from './../product'
import { Router } from '@angular/router'
import { NgForm } from '@angular/forms';


@Component({
  selector: 'app-product-creation',
  templateUrl: './product-creation.component.html',
  styleUrls: ['./product-creation.component.css']
})

export class ProductCreationComponent implements OnInit {
  newProduct = new Product();
  products: Array<Product>

  constructor(
    private _productsService: ProductsService,
    private _router: Router
  ) {
    this._productsService.productsObservable.subscribe( (products) => {
    this.products = products
  })
}

  ngOnInit() {
    this.newProduct = new Product()
  }
  create(){
    this.products.push(this.newProduct);
    this._productsService.updateProducts(this.products)
    this.newProduct = new Product();
    this._router.navigate(['/products/list'])
  }

//createProduct(){
//this.products.Service.changestring(string)
}
