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
  index= 0

  constructor(private _productsService: ProductsService,
              private _router: Router,
              private _route: ActivatedRoute
            ) {
              this._route.params.subscribe(param =>{
                this.index=(param.idx)
                this._productsService.getOneProduct()
                console.log("minhstart")
                console.log(this._productsService.getOneProduct())
                console.log("minhend")
              })
            }




  ngOnInit() {
    this._productsService.productsObservable.subscribe( (products) => {
    this.products = products;
  })

  }


update(){
  this._productsService.updateProducts(this.products);
  this.product= new Product();
  this._router.navigate(['/products/list'])
}


delete(index){
  this.products.splice(index, 1);
  this._router.navigate(['/products/list'])

}







}
