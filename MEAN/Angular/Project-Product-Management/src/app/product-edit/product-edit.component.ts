import { Component, OnInit } from '@angular/core';
import { Product } from '../product';
import { ProductsService } from '../products.service'
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-edit',
  templateUrl: './product-edit.component.html',
  styleUrls: ['./product-edit.component.css']
})
export class ProductEditComponent implements OnInit {
  products: Array<Product> = [];
  product = new Product();

  constructor(private _productsService: ProductsService,
              private _router: Router,
              private _route: ActivatedRoute
            ) {
              this._route.params.subscribe(param =>{
                this.product = this._productsService.getOneProduct(param.idx)
                console.log(this.product)
              })
            }




  ngOnInit() {
    this._productsService.productsObservable.subscribe( (products) => {
    this.products = products;
    console.log(products);
  })

  }
}
