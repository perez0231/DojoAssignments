import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../products.service'
import { Product } from '../product';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: Array<Product> =[]

  constructor(private _productsService: ProductsService) { }

  ngOnInit() {
    this._productsService.productsObservable.subscribe((products) => {
      this.products = products;
    });
  }
//
// delete(product){
//   const idx =this.products.indexOf(product)
//   this.products.splice(idx, 1);
//   this._productsService.updateProducts(this.products)
// }


}
